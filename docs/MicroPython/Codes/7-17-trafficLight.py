'''
 * Filename    : 7-17-trafficLight
 * Thonny      : Thonny 4.1.4
 * Auther      : http//www.keyestudio.com
'''
from machine import Pin
import time

redLED = Pin(23,Pin.OUT)	#set red LED to IO23
greenLED = Pin(27,Pin.OUT)	#set green LED to IO27
yellowLED = Pin(26,Pin.OUT)	#set yellow LED to IO26

#turn off three led
redLED.off()
greenLED.off()
yellowLED.off()

#green led on for 5S; yellow led blink for 3; red led on for 5S; in a loop
while True:
    greenLED.on()
    time.sleep(5)
    greenLED.off()
    for i in range(0,3):
        yellowLED.on()
        time.sleep(0.5)
        yellowLED.off()
        time.sleep(0.5)
    redLED.on()
    time.sleep(5)
    redLED.off()