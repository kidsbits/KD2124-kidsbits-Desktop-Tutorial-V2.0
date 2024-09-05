'''
 * Filename    : 7-18-gradientLight
 * Thonny      : Thonny 4.1.4
 * Auther      : http//www.keyestudio.com
'''
from machine import Pin, PWM  
import time  
  
# set PWM pin and frequency   
pwm_pin = Pin(23, Pin.OUT)  
pwm = PWM(pwm_pin, freq=1000)  # set frequency to 1000Hz  
  
# breathing LED    
while True:  
    for duty in range(0, 1024, 5):  # gradually light up 
        pwm.duty(duty)  
        time.sleep_ms(10)  # add a delay for better observing  
    for duty in range(1023, -1, -5):  # gradually dim out 
        pwm.duty(duty)  
        time.sleep_ms(10)