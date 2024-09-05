'''
 * Filename    : 7-31-remoteControlServo
 * Thonny      : Thonny 4.1.4
 * Auther      : http//www.keyestudio.com
'''
from machine import Pin,ADC
import machine 
import time
#import Servo from servo library
from servo import Servo

servo = Servo(pin=25)  # set servo pins

rocker_x=ADC(Pin(35))	#set joystick axis x input to IO35
rocker_x.atten(ADC.ATTN_11DB)
rocker_x.width(ADC.WIDTH_12BIT)

while True:
    val = rocker_x.read()
    print(val)
    if val > 3500:
        servo.set_angle(0)
    elif val < 500:
        servo.set_angle(180)
    time.sleep(1)

