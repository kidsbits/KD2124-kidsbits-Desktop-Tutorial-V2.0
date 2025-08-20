'''
 * Filename    : 3-29-parkingSensor
 * Thonny      : Thonny 4.1.4
 * Auther      : http//www.keyestudio.com
'''
from machine import Pin,PWM
import time

#set PWM output pin to IO32, frequency to 5000 Hz, duty cycle to 50% (the middle value of 8 bit resolution is 128, duty cycle ranges from 0-255)
spk = PWM(Pin(32), freq=5000, duty=128)
redLED = Pin(23,Pin.OUT)
greenLED = Pin(27,Pin.OUT)

# Define the control pins of the ultrasonic sensor
Trig = Pin(5, Pin.OUT) 
Echo = Pin(4, Pin.IN)

distance = 0 # set initial value to 0
soundVelocity = 340 #Set the speed of sound.

# getDistance() Function is used to drive the ultrasonic module to measure distance,
# Echo.value() is used to read the status of the Echo pin of the ultrasonic module,
# The timestamp function of the time module calculates the high level of the Echo's duration pin, calculate the measured distance based on the time and returns a value.
def getDistance():
    # maintain Trig pin at a high level of 10us to enable the ultrasonic sensor
    Trig.value(1)
    time.sleep_us(10)
    Trig.value(0)
    #Start timing, the initial time of ultrasonic propagation in the air
    while Echo.value() == 0:
        Start = time.ticks_us()
    #The time of receiving the reflected ultrasonic wave
    while Echo.value() == 1:
        Stop = time.ticks_us()
    #The received time minus the initial time is the total time
    Time = time.ticks_diff(Stop,Start)
    #Calculate the distance according to the formula gives the result in meters.
    #Divide by 1000 to convert to centimeters.
    distance =  Time * soundVelocity //2 // 10000
    #return the calculated value
    return distance

# print the ultrasonic sensor value every 500ms
while True:    
    distance = getDistance()
    print('Distance: ',distance, 'cm')
    if distance > 40:	#determine whether the distance > 40. If yes, green led is on, speaker does not emit sound; If not, red led is on and speaker emits sound
        redLED.off()
        greenLED.on()
        spk.duty(0)	#speaker does not emit sound
    else:
        redLED.on()
        greenLED.off()
        spk.duty(50)	#set speaker PWM duty cycle
        spk.freq(880)	#set speaker frequency
    time.sleep_ms(300)
