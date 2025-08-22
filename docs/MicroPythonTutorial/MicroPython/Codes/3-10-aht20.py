'''
 * Filename    : 3-10-aht20
 * Thonny      : Thonny 4.1.4
 * Auther      : http//www.keyestudio.com
'''
#import I2C and Pin from machine
from machine import I2C, Pin
#import AHT20 from aht20 library
from aht20 import AHT20
import time
#create an I2C object and define SDA and SCL pin
i2c = I2C(scl=Pin(22), sda=Pin(21))
#create an AHT20 object, initialize I2C object to communicate through I2C bus and AHT20 sensor
sensor = AHT20(i2c)

while True:		
    try:
        #Store the values of temperature and humidity in the temperature and humidity variables
        temperature, humidity = sensor.read_temperature_humidity()
        #Formatted output variable value of temperature and humidity, keep two decimal places
        print("Temperature: {:.2f} C, Humidity: {:.2f} %".format(temperature, humidity))
    #Read the detect value, if there is an error, print “Failed to read from sensor:”
    except RuntimeError as e:
        print("Failed to read from sensor: ", e)
    time.sleep(1)	#delay 1S
