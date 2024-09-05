'''
 * Filename    : 7-25-lnductionDoor
 * Thonny      : Thonny 4.1.4
 * Author      : http://www.keyestudio.com
'''
from machine import Pin
import time
from servo import Servo

pir = Pin(19,Pin.IN)
servo = Servo(pin=25)

while True:
    Pir = pir.value()
    if Pir == 1:
        servo.set_angle(0)  # rotate servo to 0 degree
    else:
        servo.set_angle(180)  # rotate servo to 180 degree
    time.sleep_ms(300)
    