'''
 * Filename    : 3-15-rgbLed2
 * Thonny      : Thonny 4.1.4
 * Auther      : http//www.keyestudio.com
 ----------------------------------------
    color = [red,green,blue]
    color stores the color values.
    red.green,blue corespond to RGB values, ranging from 0-255
    Red [255,0,0]
    set the color you want to display according to RGB color table
'''
#Import Pin, neopiexl and time modules.
from machine import Pin
import neopixel
import time

pin = Pin(16, Pin.OUT)	#define SK6812 control pin to IO16
num_pixels = 12			#set SK6812 beads to 12
#initialize SK6812
np = neopixel.NeoPixel(pin, num_pixels)
red = [255,0,0]	#red
green = [0,255,0]#green
blue = [0,0,255]	#blue

while True:
    for i in range(num_pixels):		#for loop: add i from 0 to 11
        np[i] = red		#show red at i
        np.write()		#refresh to display the set color
        time.sleep_ms(50)	#delay 50ms to change the color of the ring gradually
    time.sleep(1)	#Pause 1 second after all display
    for i in range(num_pixels):
        np[i] = green		#show green at i
        np.write()	
        time.sleep_ms(50)
    time.sleep(1)
    for i in range(num_pixels):	
        np[i] = blue		#show blue at i
        np.write()
        time.sleep_ms(50)
    time.sleep(1)
    
