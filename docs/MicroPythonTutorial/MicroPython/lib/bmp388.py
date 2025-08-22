import machine
import time
from struct import unpack

class BMP388:
    BMP3_CHIP_ID_ADDR = 0x00
    BMP3_CHIP_ID = 0x50
    BMP3_PWR_CTRL_ADDR = 0x1B
    BMP3_DATA_ADDR = 0x04
    BMP3_CMD_ADDR = 0x7E
    BMP3_RESET_CMD = 0xB6
    BMP3_CALIB_DATA_ADDR = 0x31

    BMP3_PRESS_EN = 0x01
    BMP3_TEMP_EN = 0x02
    BMP3_NORMAL_MODE = 0x30

    def __init__(self, i2c, i2c_addr=0x77):
        self.i2c = i2c
        self.i2c_addr = i2c_addr
        self.calib_data = []
        self.t_fine = 0  # 用于存储补偿温度的中间变量
        if not self.init_sensor():
            raise Exception("BMP388 initialization failed")

    def init_sensor(self):
        if self.read_register(self.BMP3_CHIP_ID_ADDR, 1)[0] != self.BMP3_CHIP_ID:
            return False
        self.reset()
        self.write_register(self.BMP3_PWR_CTRL_ADDR, [self.BMP3_PRESS_EN | self.BMP3_TEMP_EN | self.BMP3_NORMAL_MODE])
        self.read_calib_data()
        return True

    def reset(self):
        self.write_register(self.BMP3_CMD_ADDR, [self.BMP3_RESET_CMD])
        time.sleep(0.01)

    def read_register(self, reg, length):
        return self.i2c.readfrom_mem(self.i2c_addr, reg, length)

    def write_register(self, reg, values):
        self.i2c.writeto_mem(self.i2c_addr, reg, bytearray(values))

    def read_calib_data(self):
        calib = self.read_register(self.BMP3_CALIB_DATA_ADDR, 21)
        self.par_t1 = unpack('<H', calib[0:2])[0] / 2**-8
        self.par_t2 = unpack('<H', calib[2:4])[0] / 2**30
        self.par_t3 = unpack('b', calib[4:5])[0] / 2**48
        self.par_p1 = (unpack('<h', calib[5:7])[0] - 2**14) / 2**20
        self.par_p2 = (unpack('<h', calib[7:9])[0] - 2**14) / 2**29
        self.par_p3 = unpack('b', calib[9:10])[0] / 2**32
        self.par_p4 = unpack('b', calib[10:11])[0] / 2**37
        self.par_p5 = unpack('<H', calib[11:13])[0] / 2**-3
        self.par_p6 = unpack('<H', calib[13:15])[0] / 2**6
        self.par_p7 = unpack('b', calib[15:16])[0] / 2**8
        self.par_p8 = unpack('b', calib[16:17])[0] / 2**15
        self.par_p9 = unpack('<H', calib[17:19])[0] / 2**48
        self.par_p10 = unpack('b', calib[19:20])[0] / 2**48
        self.par_p11 = unpack('b', calib[20:21])[0] / 2**65

    def compensate_temperature(self, raw_temp):
        partial_data1 = (raw_temp - self.par_t1)
        partial_data2 = (partial_data1 * self.par_t2)
        temp_comp = partial_data2 + (partial_data1 * partial_data1) * self.par_t3
        return temp_comp
    

    def compensate_pressure(self, raw_pres):
        partial_data1 = self.par_p6 * self.t_fine
        partial_data2 = self.par_p7 * self.t_fine ** 2.0
        partial_data3 = self.par_p8 * self.t_fine ** 3.0
        partial_out1 = self.par_p5 + partial_data1 + partial_data2 + partial_data3

        partial_data1 = self.par_p2 * self.t_fine
        partial_data2 = self.par_p3 * self.t_fine ** 2.0
        partial_data3 = self.par_p4 * self.t_fine ** 3.0
        partial_out2 = raw_pres * (self.par_p1 + partial_data1 + partial_data2 + partial_data3)

        partial_data1 = raw_pres ** 2.0
        partial_data2 = self.par_p9 + self.par_p10 * self.t_fine
        partial_data3 = partial_data1 * partial_data2
        partial_data4 = partial_data3 + raw_pres ** 3.0 * self.par_p11

        pres_comp = partial_out1 + partial_out2 + partial_data4
        return pres_comp * 1.073  # 调整补偿计算后的压力值比例

    def read_raw_temperature(self):
        data = self.read_register(self.BMP3_DATA_ADDR + 3, 3)
        return (data[2] << 16) | (data[1] << 8) | data[0]

    def read_raw_pressure(self):
        data = self.read_register(self.BMP3_DATA_ADDR, 3)
        return (data[2] << 16) | (data[1] << 8) | data[0]

    def read_temperature(self):
        raw_temp = self.read_raw_temperature()
        return self.compensate_temperature(raw_temp)

    def read_pressure(self):
        raw_pres = self.read_raw_pressure()
        return self.compensate_pressure(raw_pres)

