'''
 * Filename    : 7-6-adKey2
 * Thonny      : Thonny 4.1.4
 * Auther      : http//www.keyestudio.com
'''
# Import Pin and ADC modules.
from machine import ADC,Pin
import time 

adc=ADC(Pin(33))			#set pin GPIO 33 to ADC input pin
adc.atten(ADC.ATTN_11DB)	#set voltage range to 0-3.3V
adc.width(ADC.WIDTH_12BIT)	#set ADC resolution

while True:					
    itme = adc.read() 	#read analog value of AD button and assign it to item
    if itme > 3500:	#determine whether itme > 3500, if yes, print “Red”
        print("Red")
    elif (itme > 2000) and (itme < 3000):	#determine whether 2000<itme<3000, if yes, print “Yellow”
        print("Yellow")
    elif itme > 900 and itme < 1500:	#determine whether 900<itme<1500, if yes, print “Green”
        print("Green")
    time.sleep(0.3)		#delay 0.3S
