'''
 * Filename    : 7-16-oled
 * Thonny      : Thonny 4.1.4
 * Auther      : http//www.keyestudio.com
-----------------------------------------
oled.clear()
clear display. If you want to display new content, you have to clear the last display; or the two content will be overlapped

oled.oled.show()
refresh to display the new content on OLED

oled.show_text("******", X,Y)
set code. input content to be displayed in the double quotation marks,
and set value of X，Y to control the starting position of the display.
'''
import machine
from oled import OLED

# Initialize I2C interface
i2c = machine.SoftI2C(scl=machine.Pin(22), sda=machine.Pin(21))

# create OLED example
oled = OLED(i2c)

# clear display
oled.clear()

# show text
oled.show_text("KEYESTUTDIO", 20, 0)

# show text
oled.show_text("Hello World!", 20, 10)
oled.show_text("MicroPython", 20, 20)

# show
oled.oled.show()
