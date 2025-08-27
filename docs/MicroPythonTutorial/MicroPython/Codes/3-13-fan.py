'''
 * Filename    : 3-13-fan
 * Thonny      : Thonny 4.1.4
 * Auther      : http//www.keyestudio.com
---------------------------------------------
motor rotation logic table:
---------------------------------------------
  IO18(MA) 	| IO17(MB)  |     motor state		|
---------------------------------------------
  HIGH 		|   LOW   	|       forward rotate 		|
---------------------------------------------
   LOW 		|  HIGH  	|       reverse rotate 		|
---------------------------------------------
  HIGH 		|  HIGH  	|  stop (a gradual stop) |
---------------------------------------------
   LOW 		|   LOW   	|   brake (a brake stop)	|
---------------------------------------------
'''

from machine import Pin
import time

#set motor control pin A to IO18
MA = Pin(18,Pin.OUT)
#set motor control pin B to IO17
MB = Pin(17,Pin.OUT)

while True:
    #forward rotate
    MA.on()
    MB.off()
    time.sleep(2)
    #reverse rotate
    MA.off()
    MB.on()
    time.sleep(2)
    #stop
    MA.off()
    MB.off()
    time.sleep(2)