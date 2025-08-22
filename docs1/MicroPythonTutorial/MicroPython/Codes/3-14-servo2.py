'''
 * Filename    : 3-14-servo2
 * Thonny      : Thonny 4.1.4
 * Auther      : http//www.keyestudio.com
'''
import machine
import time
#import Servo from servo library
from servo import Servo

servo = Servo(pin=25)  # connect servo to pin

while True:
    #rotate servo from 0 degree to 180 degree
    for angle in range(0,180):
        servo.set_angle(angle)  # rotate servo to 180 degree
        time.sleep_ms(10)		#delay 10ms
    #rotate servo from 180 degree to 0 degree
    for angle in range(180,-1,-1):
        servo.set_angle(angle)  # rotate servo to 0 degree
        time.sleep_ms(10)

