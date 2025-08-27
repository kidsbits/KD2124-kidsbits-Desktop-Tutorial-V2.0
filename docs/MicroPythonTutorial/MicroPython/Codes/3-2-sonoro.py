'''
 * Filename    : 3-2-sound
 * Thonny      : Thonny 4.1.4
 * Auther      : http//www.keyestudio.com
'''
# Import Pin, ADC and DAC modules.
from machine import ADC,Pin
import time

adc=ADC(Pin(34))			#set pin GPIO 34 as ADC input pin
adc.atten(ADC.ATTN_11DB)	#voltage range 0-3.3V
adc.width(ADC.WIDTH_12BIT)	#set ADC resolution

# Read ADC value once every 0.1seconds, convert ADC value to DAC value and output it, and print these data to “Shell”.
while True:				
        adcVal = adc.read()				#read the analog value of the sound sensor and assign it to variable to adcVal
        print("Sonoro ADC Val:",adcVal) #serial monitor prints adcVal value
        time.sleep_ms(50)					#delay 50mS
