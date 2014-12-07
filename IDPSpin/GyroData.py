#The class for the gyrometer

try:
    import smbus
except:
    print "no smbus"
import math
import time

class GyroData(object):

    def __init__(self):
        try:
            #Set ports and address
            self.power_mgmt_1 = 0x6b
            self.power_mgmt_2 = 0x6c
            self.bus = smbus.SMBus(1)
            self.address = 0x68
            self.bus.write_byte_data(self.address, self.power_mgmt_1, 0)
            self.xDegree = 0
            self.yDegree = 0
        except:
            pass
        
    def read_byte(self, adr):
        return bus.read_byte_data(self.address, adr)
    
    def read_word(self, adr):
        high = self.bus.read_byte_data(self.address, adr)
        low = self.bus.read_byte_data(self.address, adr+1)
        val = (high << 8) + low
        return val

    #Read data and converts it to two's complement
    def read_word_2c(self, adr):
        val = self.read_word(adr)
        if(val >= 0x8000):
            return -((65535 - val) + 1)
        else:
            return val

    def dist(self, a, b):
        return math.sqrt((a*a)+(b*b))

    #Calculates x rotation and returns in degrees
    def get_x_rotation(self,x,y,z):
        radians = math.atan2(y, self.dist(y, z))
        return math.degrees(radians)

    #Calculates y rotation and returns in degrees
    def get_y_rotation(self, x, y, z):
        radians = math.atan2(y, self.dist(x, z))
        return math.degrees(radians)

    def get_z_rotation(self, x, y, z):
        radians = math.atan2(z, self.dist(x, y))
        return math.degrees(radians)
    

    def printGyroData(self):
        gyro.xout = self.read_word_2c(0x43)
        gyro_yout = self.read_word_2c(0x45)
        gyro_zout = self.read_word_2c(0x47)
        print "gyro_xout: ", gyro_xout, " scaled: ", (gyro_xout / 131)
        print "gyro_yout: ", gyro_yout, " scaled: ", (gyro_yout / 131)
        print "gyro_zout: ", gyro_zout, " scaled: ", (gyro_zout / 131)

    #Calculates the rotation in degrees
    def calculateAngle(self):
        #Get gyro data and parameter
        accel_xout = self.read_word_2c(0x3b)
        accel_yout = self.read_word_2c(0x3d)
        accel_zout = self.read_word_2c(0x3f)

        #Scale the raw data
        accel_xout_scaled = accel_xout / 16384.0
        accel_yout_scaled = accel_yout / 16384.0
        accel_zout_scaled = accel_zout / 16384.0

        #Calculate in degrees
        self.xDegree = self.get_x_rotation(accel_xout_scaled,
                                      accel_yout_scaled, accel_zout_scaled)
        self.yDegree = self.get_y_rotation(accel_xout_scaled,
                                      accel_yout_scaled, accel_zout_scaled)
        self.zDegree = self.get_y_rotation(accel_xout_scaled,
                                      accel_yout_scaled, accel_zout_scaled)


    #Get x degree
    def getXDegrees(self):
        self.calculateAngle()
        xString = '%d' %(self.xDegree)
        return xString

    #Get y degree
    def getYDegrees(self):
        self.calculateAngle()
        yString = '%d' %(self.yDegree)
        return yString

    #Get z degree
    def getYDegrees(self):
        self.calculateAngle()
        zString = '%d' %(self.zDegree)
        return zString

    def getDegrees(self):
        return self.getXDegrees() + "|" + self.getYDegrees()
