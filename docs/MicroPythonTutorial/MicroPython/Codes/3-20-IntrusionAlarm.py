'''
 * Filename    : 3-20-lntrusionAlarm
 * Thonny      : Thonny 4.1.4
 * Auther      : http//www.keyestudio.com
'''
from machine import Pin,PWM
import time

#set PWM output pin to IO32, frequency to 5000 Hz, duty cycle to 50% (8-bit resolution middle value is 128, duty cycle ranges from 0-255)
spk = PWM(Pin(32), freq=5000, duty=128)

redLED = Pin(23,Pin.OUT)
greenLED = Pin(27,Pin.OUT)
pir = Pin(19,Pin.IN)

while True:
    #read pir sensor value and assign it to variable PIR
    PIR = pir.value()
    print("pir:",PIR)	#print PIR value
    if PIR == 1:		#determine whether PIR = 1
        greenLED.off()	#green off
        redLED.on()		#red on
        spk.duty(50)	#set the PWM duty cycle of the speaker
        spk.freq(880)	#set the frequency of the speaker
    else:
        redLED.off()	#red off
        greenLED.on()	#green on
        spk.duty(0)		#set the duty cycle of the speaker to 0, stop emitting sound
    time.sleep(0.1)