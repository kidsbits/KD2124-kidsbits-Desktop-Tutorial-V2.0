'''
 * Filename    : 3-8-rfid
 * Thonny      : Thonny 4.1.4
 * Auther      : http//www.keyestudio.com
'''
import machine
import time
#import mfrc522 from mfrc522_i2c
from mfrc522_i2c import mfrc522

#i2c config
addr = 0x28		#rfid IIC communication address
scl = 22		#IIC SCL pin
sda = 21		#IIC SDA pin

#create an MFRC522 object, I2C SCL and SDA pin and device address
rc522 = mfrc522(scl, sda, addr)
#initialize MFRC522 module, this is essential to ensure working state
rc522.PCD_Init()
#show MFRC522 reader information, used to debug and ensure working state
rc522.ShowReaderDetails()        

while True:
    #detect whether there is an RFID card within the sensing area
    if rc522.PICC_IsNewCardPresent():
        #try to read the card ID. If the ID can be successfully read, return True.
        if rc522.PICC_ReadCardSerial() == True:
            #print “Card UID:” and complete UID
            print("Card UID:",rc522.uid.uidByte[0 : rc522.uid.size])