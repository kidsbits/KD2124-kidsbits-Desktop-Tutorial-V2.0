'''
 * Filename    : 7-11-bmp388
 * Thonny      : Thonny 4.1.4
 * Auther      : http//www.keyestudio.com
'''
import machine
#import BMP388 from BMP388 library
from bmp388 import BMP388 
import time

# create BMP388 object and set SDA and SCL pin, set IIC frequency to 100KHz
i2c = machine.SoftI2C(scl=machine.Pin(22), sda=machine.Pin(21), freq=100000)

# create a BMP388 object, pass the previously created i2c object to it, and communicate with the BMP388 sensor via the I2C bus, set BMP388 IIC address to 0x76
bmp = BMP388(i2c, i2c_addr=0x76)

while True:
    # read the temperature value
    temperature = bmp.read_temperature()
    # read the pressure value
    pressure = bmp.read_pressure()
    # print the read value
    print("Temperature:", temperature, "C "," Pressure:", pressure, "Pa")
    time.sleep(1)

