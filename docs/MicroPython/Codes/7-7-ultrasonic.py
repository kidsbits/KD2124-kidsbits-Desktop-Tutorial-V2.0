'''
 * Filename    : 7-7-ultrasonic
 * Thonny      : Thonny 4.1.4
 * Auther      : http//www.keyestudio.com
'''
from machine import Pin,PWM
import time


# define the control pin of the ultrasonic sensor
Trig = Pin(5, Pin.OUT) 
Echo = Pin(4, Pin.IN)

distance = 0 # define the initial value to 0
soundVelocity = 340 #Set the speed of sound.

# getDistance() measures the distance, Echo.value() reads the status of Echo pin. Use the timestamp function of the time module to calculate the high level of the Echo's duration pin, and calculate the measured distance based on the time and return the value.
def getDistance():
    # Trig pin maintains high level for 10us to enable to the ultrasonic sensor
    Trig.value(1)
    time.sleep_us(10)
    Trig.value(0)
    #start counting, the initial time of ultrasonic wave propagation in the air
    while Echo.value() == 0:
        Start = time.ticks_us()
    #The time of receiving the reflected ultrasonic wave
    while Echo.value() == 1:
        Stop = time.ticks_us()
    #The received time minus the initial time is the total time
    Time = time.ticks_diff(Stop,Start)
    #Calculate the distance according to the formula in meters.
    #Divide by 1000 to convert to centimeters.
    distance =  Time * soundVelocity //2 // 10000
    #Return the result of the calculation
    return distance

# Print the ultrasonic sensor value every 500 milliseconds
while True:    
    print('Distance: ', getDistance(), 'cm')
    time.sleep_ms(500)