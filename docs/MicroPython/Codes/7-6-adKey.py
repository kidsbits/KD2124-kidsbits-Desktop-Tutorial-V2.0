'''
 * Filename    : 7-6-adKey
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
    adcVal = adc.read() 	#read AD button value and assign it to adcVal
    print("adcVal:",adcVal)	#print the adcVal value
    time.sleep(0.3)			#delay 0.3S