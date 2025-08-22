'''
 * Filename    : 3-27-autimaticFan
 * Thonny      : Thonny 4.1.4
 * Author      : http://www.keyestudio.com
'''
#import I2C and Pin from machine module
from machine import I2C, Pin
#import AHT20 from aht20 library
from aht20 import AHT20
import time
#create an I2C object and add SDA and SCL pins
i2c = I2C(scl=Pin(22), sda=Pin(21))
#create an AHT20 object, initialize I2C object to communication with AHT20 sensor via I2C bus
sensor = AHT20(i2c)

pir = Pin(19,Pin.IN)
#set the motor pin A to IO18
MA = Pin(18,Pin.OUT)
#set the motor pin B to IO17
MB = Pin(17,Pin.OUT)

while True:		
    try:
        #store the temperature and humidity to variable temperature and humidity
        temperature, humidity = sensor.read_temperature_humidity()
        Pir = pir.value()
        #Determine whether the PIR detects persons and temperature are greater than 28 degrees. If yes, the motor rotates; if not, the motor will not rotate
        if Pir == 1 and temperature > 28:
            MA.on()
            MB.off()
        else:
            MA.off()
            MB.off()
    #detect and read value, print “Failed to read from sensor:” if an error occurs
    except RuntimeError as e:
        print("Failed to read from sensor: ", e)
    time.sleep(1)	#delay 1S