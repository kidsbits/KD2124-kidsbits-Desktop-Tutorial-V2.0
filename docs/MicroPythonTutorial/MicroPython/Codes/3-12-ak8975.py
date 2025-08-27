'''
 * Filename    : 3-12-ak8975
 * Thonny      : Thonny 4.1.4
 * Auther      : http//www.keyestudio.com
'''
from machine import Pin
#import ak8975c from AK8975C
from AK8975C import ak8975c
import time

scl = Pin(22)
sda = Pin(21)
#create an ak8975c object, initialize I2C bus and SCL and SDA pin
Triaxial = ak8975c(scl, sda)

while True:
    Triaxial.measure()  # measure values
    print('x:',Triaxial.X,'y:',Triaxial.Y,'z:',Triaxial.Z)  # Print the geomagnetic strength of the XYZ axis
    if Triaxial.AK8975_GET_AZIMUTH(Triaxial.X, Triaxial.Y) == True:  # Print the value of the course Angle only if the Angle can be calculated
        print('degree:', Triaxial.angle_val,'°')