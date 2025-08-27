'''
 * Filename    : 3-5-lighr
 * Thonny      : Thonny 4.1.4
 * Auther      : http//www.keyestudio.com
'''
# Import Pin, ADC and DAC modules.
from machine import ADC,Pin,DAC
import time

adc=ADC(Pin(36))			#set pin GPIO 36 to ADC input pin
adc.atten(ADC.ATTN_11DB)	#set voltage range to 0-3.3V
adc.width(ADC.WIDTH_12BIT)	#set ADC resolution

while True:				
    adcVal=adc.read()	#read the sensor value and assign it to variable adcVal
    print("ADC Val:",adcVal)	#print the adcVal value
    time.sleep(0.5)				#delay 0.5s