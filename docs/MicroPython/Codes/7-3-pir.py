'''
 * Filename    : 7-3-pir
 * Thonny      : Thonny 4.1.4
 * Auther      : http//www.keyestudio.com
'''
from machine import Pin
import time

PIR = Pin(19, Pin.IN)  # set pin IO19 to the pir input pin
while True:				
    PIR_value = PIR.value()	#read Pir sensor value and assign it to variable value
    print(PIR_value, end = " ") #print PIR_value without wrapping
    if PIR_value == 1:		#determine whether PIR_value = 1
        print("Some body is in this area!")#if PIR_value = 1, execute the code
    else:	#or else
        print("No one!")
    time.sleep(0.1)	#delay 0.1S(100ms)