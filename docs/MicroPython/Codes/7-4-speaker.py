'''
 * Filename    : 7-4-speaker
 * Thonny      : Thonny 4.1.4
 * Auther      : http//www.keyestudio.com
 
-----------------------------
| Pitch names |  Frequency  |
|---------------------------|
|    C(Do)    |     523     |
|    D(Re)    |     587     |
|    E(Mi)    |     659     |
|    F(Fa)    |     698     |
|    G(So)    |     784     |
|    A(La)    |     880     |
|    B(Si)    |     988     |
-----------------------------

'''
from machine import Pin, PWM
import time

#set pin IO32 to PWM output pin, frequency is 5000 Hz, duty cycle is 50% (The median value of 8-bit resolution is 128, the duty cycle ranges from 0-255)
trumpet = PWM(Pin(32), freq=5000, duty=128) 


a = [523,587,659,698,784,880,988] #define an array to store frequency

for i in a:				#for loop array "a", If there are n sets of data, cycle n times
    trumpet.duty(10)	#control PWM duty cycle （0-255）, sound volume is adjustable
    trumpet.freq(i)		#set frequency, emit sound by controlling frequency
    time.sleep(0.5)		#delay 0.5S
    trumpet.duty(0)		#set duty cycle to 0 to turn off the amplifier
