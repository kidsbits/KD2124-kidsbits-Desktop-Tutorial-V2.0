'''
 * Filename    : 7-14-servo
 * Thonny      : Thonny 4.1.4
 * Auther      : http//www.keyestudio.com
'''
import machine
import time
#import Servo from servo library
from servo import Servo

servo = Servo(pin=25)  # connect servo to pin

while True:
    # set angle
    servo.set_angle(0)  # rotate servo to 0 degree
    time.sleep(1)
    servo.set_angle(90)  # rotate servo to 90 degree
    time.sleep(1)
    servo.set_angle(180)  # rotate servo to 180 degree
    time.sleep(1)
