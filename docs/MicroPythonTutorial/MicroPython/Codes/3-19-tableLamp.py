'''
 * Filename    : 3-19-tableLamp
 * Thonny      : Thonny 4.1.4
 * Auther      : http//www.keyestudio.com
'''
from machine import Pin,ADC
import time

led = Pin(23,Pin.OUT)
key = ADC(Pin(33))			#set ADC input pin to GPIO 33
key.atten(ADC.ATTN_11DB)	#set voltage range to 0-3.3V
key.width(ADC.WIDTH_12BIT)	#set ADC resolution
#define a variable to shift the state of led
ledState = False

while True:
    keyVal = key.read()	#read the analog value of button
    if keyVal > 3500:	#if value > 3500: red button is pressed
        #reverse the value of ledState: if False（1）, it changes to True（0）; True becomes False
        ledState = not ledState
        time.sleep_ms(500)
    #led.value() is different from led.on() / led.off(), in led.value(), 0(led off) or 1(led on) need to be filled in.
    led.value(ledState)
