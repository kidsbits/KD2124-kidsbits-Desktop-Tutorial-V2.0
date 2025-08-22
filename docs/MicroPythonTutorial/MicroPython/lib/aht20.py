import time
import struct

class AHT20:
    def __init__(self, i2c, address=0x38):
        self.i2c = i2c
        self.address = address
        self._init_sensor()

    def _init_sensor(self):
        # Initialize the sensor
        self.i2c.writeto(self.address, bytearray([0xBE, 0x08, 0x00]))
        time.sleep(0.1)

    def _trigger_measurement(self):
        self.i2c.writeto(self.address, bytearray([0xAC, 0x33, 0x00]))
        time.sleep(0.1)

    def _read_data(self):
        data = self.i2c.readfrom(self.address, 6)
        return data

    def read_temperature_humidity(self):
        self._trigger_measurement()
        data = self._read_data()
        status = data[0]
        if (status & 0x80) == 0:
            raw_temperature = ((data[3] & 0x0F) << 16) | (data[4] << 8) | data[5]
            raw_humidity = (data[1] << 12) | (data[2] << 4) | (data[3] >> 4)
            temperature = ((raw_temperature / (2**20)) * 200) - 50
            humidity = (raw_humidity / (2**20)) * 100
            return temperature, humidity
        else:
            raise RuntimeError("Measurement not ready")

# Example usage
def main():
    from machine import I2C, Pin

    i2c = I2C(scl=Pin(22), sda=Pin(21))
    sensor = AHT20(i2c)

    while True:
        try:
            temperature, humidity = sensor.read_temperature_humidity()
            print("Temperature: {:.2f} C, Humidity: {:.2f} %".format(temperature, humidity))
        except RuntimeError as e:
            print("Failed to read from sensor: ", e)
        time.sleep(2)

if __name__ == "__main__":
    main()