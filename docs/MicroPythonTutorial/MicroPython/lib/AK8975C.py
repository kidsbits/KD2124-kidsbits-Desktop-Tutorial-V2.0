'''
AK8975C 1.0
'''

from machine import Pin
from machine import I2C
#import numpy as np
import time
import math

AK8975C_I2C_ADDR = 0x0E    
CHIP_ID = 0x48
WIA_AKM_ID = 0x00        #设备ID
INFO_AKM = 0x01        #设备信息
Status_1 = 0x02        #数据状态寄存器 0：正常 1：数据已准备
HXL = 0x03        #X轴L数据
HXH = 0x04        #X轴H数据
HYL = 0x05        #Y轴L数据
HYH = 0x06        #Y轴H数据
HZL = 0x07        #Z轴L数据
HZH = 0x08        #Z轴H数据
Status_2 = 0x09        #数据状态寄存器
Stu_DERR = 0x04        #读取STU2寄存器，进行数据判断 0：正常 1：数据读取错误
Stu_HOFL = 0x08        #读取STU2寄存器，进行数据判断 0：正常 1：传感器发生溢出
CNTL = 0x0A        #操作模式设置
MODE_PWR_DOWM = 0x00        #"0000"：掉电模式
MODE_SING_MEA = 0x01        #"0001"：单一测量模式
MODE_SELF_TEST = 0x08        #"1000"：自检模式
MODE_FUSE_ROM = 0x0F        #"1111"：保险丝ROM访问模式
                #当寄存器被写入时，从02H到09H的寄存器被初始化
ASTC = 0x0C        #自我检测控制
SELF = 0x40
ASAX = 0x10        #灵敏度调整值X
ASAY = 0x11        #灵敏度调整值X
ASAZ = 0x12        #灵敏度调整值X
                    #灵敏度调整公式
                    #Hadj = H * (((ASA - 128) * 0.5)/128 + 1)
                    #其中H为读出的测量值，ASA为灵敏度调整值，Hadj为调整后的测量数据

WHO_AM_I_REG = 0x0F

CTRL_REG1 = 0x20
CTRL_REG2 = 0x21
CTRL_REG3 = 0x22
CTRL_REG4 = 0x23
ADDR_STATUS_REG = 0x27
OUT_X_L_REG = 0x28
OUT_X_H_REG = 0x29
OUT_Y_L_REG = 0x2A
OUT_Y_H_REG = 0x2B
OUT_Z_L_REG = 0x2C
OUT_Z_H_REG = 0x2D


tumble_count = 0
#sensor_event report = []


class ak8975c:
    def __init__(self,scl, sda):
    #def __init__(self, bus, scl, sda):
        #self.bus = bus
        self.scl = scl
        self.sda = sda
        self.tumble_count = 0
        self._mode = MODE_PWR_DOWM
        self._ASAX = 0
        self._ASAY = 0
        self._ASAZ = 0
        self.X = 0
        self.Y = 0
        self.Z = 0
        self.slvAddr = 0
        self.range = 1229
        self.angle_val = -1

        #time.sleep(1)
        #self.i2c = I2C(self.bus, scl = self.scl, sda = self.sda, freq = 10000)
        self.i2c = I2C(scl = self.scl, sda = self.sda, freq = 10000)
        slv = self.i2c.scan()
        print(slv)
        for s in slv:
            buf = self.i2c.readfrom_mem(s, WIA_AKM_ID, 1)
            print(buf[0])
            if(buf[0] == 0x48):
                self.slvAddr = s
                print('ak8975c found')
                print(self.slvAddr)
                break
        while self.selfTest() == False:
            print('ak8975c self test not ok!')
        print('ak8975c self test ok!')
        self.writeByte(ASTC, 0)#在ASTC寄存器SELF上写0
        #自检结束
        #time.sleep(1)

    def selfTest(self):
        time.sleep(0.1)
        while self.AK8975_MODE_SET(MODE_FUSE_ROM) == False:
            time.sleep(0.01)  
        time.sleep(0.1)  
        buf = self.i2c.readfrom_mem(self.slvAddr, ASAX, 3)
        self._ASAX = buf[0]
        self._ASAY = buf[1]
        self._ASAZ = buf[2]
        time.sleep(0.1)  
        while self.AK8975_MODE_SET(MODE_PWR_DOWM) == False:
            time.sleep(0.01)  
        time.sleep(0.1) 
        self.writeByte(ASTC,0x40)    
        time.sleep(0.1) 
        buf = self.i2c.readfrom_mem(self.slvAddr, ASTC, 1)
        while self.AK8975_MODE_SET(MODE_SELF_TEST) == False:
            time.sleep(0.01)  
        time.sleep(0.1)        
        if self.AK89e75_CHK_DATA_RDY() == True:
            buf = self.i2c.readfrom_mem(self.slvAddr, HXL, 6)
            buff0 = buf[0]
            buff1 = buf[1]
            buff2 = buf[2]
            buff3 = buf[3]
            buff4 = buf[4]
            buff5 = buf[5]

            # 判断符号位
            twos_complement = buff0 + buff1*256
            sign_bit = twos_complement & 0xF000  # 0xF000 是16位补码的符号位掩码
            # 如果是正数，直接返回
            if sign_bit == 0:
                decimal_value = twos_complement
            else:    
                # 如果是负数，进行补码到原始值的转换
                inverted_bits = twos_complement ^ 0xFFFF  # 0xFFFF 是16位补码的按位取反掩码
                decimal_value = -(inverted_bits + 1)
            # self.X = (decimal_value/4095)*self.range
            self.X = (decimal_value * (((self._ASAX - 128) * 0.5) / 128 + 1)) * 0.3

            # 判断符号位
            twos_complement = buff2 + buff3*256
            sign_bit = twos_complement & 0xF000  # 0xF000 是16位补码的符号位掩码
            # 如果是正数，直接返回
            if sign_bit == 0:
                decimal_value = twos_complement
            else:    
                # 如果是负数，进行补码到原始值的转换
                inverted_bits = twos_complement ^ 0xFFFF  # 0xFFFF 是16位补码的按位取反掩码
                decimal_value = -(inverted_bits + 1)
            # self.Y = (decimal_value/4095)*self.range
            self.Y =  (decimal_value * (((self._ASAY - 128) * 0.5) / 128 + 1)) * 0.3

            # 判断符号位
            twos_complement = buff4 + buff5*256
            sign_bit = twos_complement & 0xF000  # 0xF000 是16位补码的符号位掩码
            # 如果是正数，直接返回
            if sign_bit == 0:
                decimal_value = twos_complement
            else:    
                # 如果是负数，进行补码到原始值的转换
                inverted_bits = twos_complement ^ 0xFFFF  # 0xFFFF 是16位补码的按位取反掩码
                decimal_value = -(inverted_bits + 1)
            # self.Z = (decimal_value/4095)*self.range
            self.Z =  (decimal_value * (((self._ASAZ - 128) * 0.5) / 128 + 1)) * 0.3

            #串口打印
            print('pre-calibration:')
            print('_ASAX:',self._ASAX,'_ASAY:',self._ASAY,'_ASAZ:',self._ASAZ)
            print('X:',self.X,'Y:',self.Y,'Z:',self.Z)         
            
            if 100 >= self.X and self.X >= -100 and 100 >= self.Y and self.Y >= -100 and -300 >= self.Z and self.Z >= -1000:
                print('error self-test!')
                return False
            else:
                return True
                
    def measure(self):
        time.sleep(0.1)
        self.AK8975_MODE_SET(MODE_FUSE_ROM)
        time.sleep(0.1)
        buf = self.i2c.readfrom_mem(self.slvAddr, ASAX, 3)
        self._ASAX = buf[0]
        self._ASAY = buf[1]
        self._ASAZ = buf[2]
        time.sleep(0.1)
        self.AK8975_MODE_SET(MODE_PWR_DOWM)
        time.sleep(0.1)
        self.AK8975_MODE_SET(MODE_SING_MEA)
        time.sleep(0.1)
        if self.AK89e75_CHK_DATA_RDY() == True:
            buf = self.i2c.readfrom_mem(self.slvAddr, HXL, 6)
            buff0 = buf[0]
            buff1 = buf[1]
            buff2 = buf[2]
            buff3 = buf[3]
            buff4 = buf[4]
            buff5 = buf[5]

            buf = self.i2c.readfrom_mem(self.slvAddr, Status_2, 1)
            if buf[0] == 0x00:
                # 判断符号位
                twos_complement = buff0 + buff1*256
                sign_bit = twos_complement & 0xF000  # 0xF000 是16位补码的符号位掩码
                # 如果是正数，直接返回
                if sign_bit == 0:
                    decimal_value = twos_complement
                else:    
                    # 如果是负数，进行补码到原始值的转换
                    inverted_bits = twos_complement ^ 0xFFFF  # 0xFFFF 是16位补码的按位取反掩码
                    decimal_value = -(inverted_bits + 1)
                # self.X = (decimal_value/4095)*self.range
                self.X = (decimal_value * (((self._ASAX - 128) * 0.5) / 128 + 1)) * 0.3

                # 判断符号位
                twos_complement = buff2 + buff3*256
                sign_bit = twos_complement & 0xF000  # 0xF000 是16位补码的符号位掩码
                # 如果是正数，直接返回
                if sign_bit == 0:
                    decimal_value = twos_complement
                else:    
                    # 如果是负数，进行补码到原始值的转换
                    inverted_bits = twos_complement ^ 0xFFFF  # 0xFFFF 是16位补码的按位取反掩码
                    decimal_value = -(inverted_bits + 1)
                # self.Y = (decimal_value/4095)*self.range
                self.Y =  (decimal_value * (((self._ASAY - 128) * 0.5) / 128 + 1)) * 0.3

                # 判断符号位
                twos_complement = buff4 + buff5*256
                sign_bit = twos_complement & 0xF000  # 0xF000 是16位补码的符号位掩码
                # 如果是正数，直接返回
                if sign_bit == 0:
                    decimal_value = twos_complement
                else:    
                    # 如果是负数，进行补码到原始值的转换
                    inverted_bits = twos_complement ^ 0xFFFF  # 0xFFFF 是16位补码的按位取反掩码
                    decimal_value = -(inverted_bits + 1)
                # self.Z = (decimal_value/4095)*self.range
                self.Z =  (decimal_value * (((self._ASAZ - 128) * 0.5) / 128 + 1)) * 0.3
            else:
                self.X = 0
                self.Y = 0
                self.Z = 0
        else:
            self.X = 0
            self.Y = 0
            self.Z = 0   

    def AK8975_GET_AZIMUTH(self,x,y):
        if x > 0 and y > 0:
            self.angle_val = math.atan(y / x) * 180.0 / 3.14
            return True
        elif x > 0 and y < 0:
            self.angle_val = math.atan(y / x) * 180.0 / 3.14 + 360
            return True
        elif x < 0 and y != 0:
            self.angle_val = math.atan(y / x) * 180.0 / 3.14 + 180
            return True
        elif x==0 and y > 0:
            self.angle_val = 90.0
            return True
        elif x==0 and y < 0:
            self.angle_val = 270.0
            return True
        else:
            return False

    def AK8975_MODE_SET(self, mode):
        self._mode = MODE_PWR_DOWM
        if mode != MODE_PWR_DOWM and mode != MODE_SING_MEA and mode != MODE_SELF_TEST and mode !=MODE_FUSE_ROM:
            return False
        else:
            self._mode = mode 
            self.writeByte(CNTL,self._mode) 
            return True

    def AK89e75_CHK_DATA_RDY(self):
        time.sleep(0.1)
        buf = self.i2c.readfrom_mem(self.slvAddr, Status_1, 1)
        while buf[0] == 0:
            buf = self.i2c.readfrom_mem(self.slvAddr, Status_1, 1)
        if  buf[0] & 0x01 == 0x01:
            return True
        else:
            return False

    def writeByte(self, addr, data):
        d = bytearray([data])
        self.i2c.writeto_mem(self.slvAddr, addr, d)
        
    def readByte(self, addr):
        return self.i2c.readfrom_mem(self.slvAddr, addr, 1)
    
    # def tumble_handle(self):
    #     x,y,z = self.readXYZ() 
    #     result = math.sqrt(x**2 + y**2 +z**2)
            
    #     angle_x = (math.atan(x / math.sqrt(y**2 + z**2))) * 180 / 3.14  #PI = 3.14
    #     angle_y = (math.atan(y / math.sqrt(x**2 + z**2))) * 180 / 3.14
    #     angle_z = (math.atan(z / math.sqrt(y**2 + x**2))) * 180 / 3.14
    #     #print('angle_x:',angle_x,'angle_y:',angle_y,'angle_z:',angle_z)
        
    #     if (abs(angle_x) > 45 or abs(angle_y) > 45) or angle_z < 0:
    #         self.tumble_count += 1
    #         if self.tumble_count >= 3:
    #             print('tumble')
    #             #self.tumble_count = 0
    #     else:
    #         self.tumble_count = 0
    #         print('no tumble')
        
    #     return self.tumble_count
    #     #if self.tumble_count >= 3:
    #         #print('tumble')
    #         #self.tumble_count = 0
