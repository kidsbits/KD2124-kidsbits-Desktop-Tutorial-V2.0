import machine
import time

class Servo:
    def __init__(self, pin, freq=50, min_us=500, max_us=2500, angle=180):
        self.pin = pin
        self.freq = freq
        self.min_us = min_us
        self.max_us = max_us
        self.angle = angle
        self.pwm = machine.PWM(machine.Pin(self.pin), freq=self.freq)
        
    def set_angle(self, angle):
        if angle < 0 or angle > self.angle:
            raise ValueError("Angle out of range")
        us = self.min_us + (self.max_us - self.min_us) * angle / self.angle
        duty = int(us * 1024 * self.freq / 1000000)
        self.pwm.duty(duty)

# 创建舵机实例

