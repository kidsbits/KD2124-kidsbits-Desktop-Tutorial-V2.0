'''
 * Filename    : 3-22-hallwayLight
 * Thonny      : Thonny 4.1.4
 * Auther      : http//www.keyestudio.com
'''
from machine import Pin,ADC
import time

light = ADC(Pin(36))
light.atten(ADC.ATTN_11DB)	#set voltage range to 0-3.3V
light.width(ADC.WIDTH_12BIT)	#set ADC resolution

sound = ADC(Pin(34))
sound.atten(ADC.ATTN_11DB)	#set voltage range to 0-3.3V
sound.width(ADC.WIDTH_12BIT)	#set ADC resolution

led = Pin(23,Pin.OUT)

while True:
    #read light sensor value and determine whether it is less than 500. If not, exit the loop
    while light.read() < 500:
        #read the sound sensor value and determine whether it is greater than 200. If yes, turn on led for 5s
        if sound.read() > 200:
            led.on()
            time.sleep(5)
            led.off()