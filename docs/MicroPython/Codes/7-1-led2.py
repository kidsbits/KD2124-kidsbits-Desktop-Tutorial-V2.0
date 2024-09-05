'''
 * Filename    : 7-1-led2
 * Thonny      : Thonny 4.1.4
 * Auther      : http//www.keyestudio.com
'''
from machine import Pin
import time

led = Pin(23,Pin.OUT) 	# connect the led to pin IO23, set it to output

while True:					
    led.on()				#red led on
    time.sleep_ms(200)		#delay 200mS
    led.off()				#red led off
    time.sleep_ms(200)		#delay 200mS

