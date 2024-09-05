'''
 * Filename    : 7-1-led
 * Thonny      : Thonny 4.1.4
 * Auther      : http//www.keyestudio.com
'''
from machine import Pin
import time

led = Pin(23,Pin.OUT) 	# Set IO23 as the red LED control pin

#Infinite loop, so that the code can be repeatedly executed
while True:
    led.on()			#The red LED light is on
    time.sleep(1)		#Delay of 1 second
    led.off()			#The red LED light is off
    time.sleep(1)		#Delay of 1 second