'''
 * Filename    : 3-15-rgbLed
 * Thonny      : Thonny 4.1.4
 * Auther      : http//www.keyestudio.com
'''
#Import Pin, neopiexl and time modules.
from machine import Pin
import neopixel
import time

pin = Pin(16, Pin.OUT)	#define SK6812 control pin to IO16
num_pixels = 12			#set the number of SK6812 beads to 12
#initialize SK6812 beads
np = neopixel.NeoPixel(pin, num_pixels)

red = [255,0,0]	#set display color to red

while True:
    np[0] = red		#the first bead lights up in red. 12 beads: number from 0-11
    np.write()		#refresh to display the set color
    