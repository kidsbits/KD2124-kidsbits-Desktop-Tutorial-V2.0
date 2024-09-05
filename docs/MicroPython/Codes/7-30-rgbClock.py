'''
 * Filename    : 7-30-rgbClock
 * Thonny      : Thonny 4.1.4
 * Auther      : http//www.keyestudio.com
'''
from machine import Pin
import neopixel
import time  
  
hour = 10 	#set hour
minute = 30 #set minute
second = 40	#set second

pin = Pin(16, Pin.OUT)	#set SK6812 control pin to IO16
num_pixels = 12			#set SK6812灯 pixels to 12
#initialize SK6812
np = neopixel.NeoPixel(pin, num_pixels)

red = [255,0,0]	#red-hour
green = [0,255,0]#green-minute
blue = [0,0,255]	#blue-second
  
def setClock():  
    global hour, minute, second  # Use the global keyword to modify global variables
    second += 1  
    if second > 59:  
        second = 0  
        minute += 1  
        if minute > 59:  
            minute = 0  
            hour += 1  
            if hour > 12:  
                hour = 1  
    print(f"{hour:02d}:{minute:02d}:{second:02d}")  # Print time, format output 
    time.sleep(1)  
  
while True:  
    setClock() 
    if second // 5 == 0:
        for i in range(0,11):	#clear second
            np[i] = 0,0,0
        np[11] = blue
        np.write()		#refresh display
    else:
        np[int(second // 5 - 1)] = blue
        np.write()		#refresh display
    if minute // 5 == 0:
        np[11] = green
        np.write()		#refresh display
    else:
        np[int(minute // 5 - 1)] = green
        np.write()		#refresh display
    np[(hour-1)] = red
    np.write()		#refresh display