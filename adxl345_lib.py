# ADXL345 Python library for Raspberry Pi 
#
# author:  Markus Sandholz
#
# Github: https://github.com/msandholz/RaspberryPi_Sensors/wiki/ADXL345-3-axis-accelerometer

import smbus
 
class ADXL345:
 
     # ADXL345 constants
    EARTH_GRAVITY_MS2   = 9.80665
    SCALE_MULTIPLIER    = 0.004
 
    DATA_FORMAT         = 0x31
    BW_RATE             = 0x2C
    POWER_CTL           = 0x2D
 
    BW_RATE_1600HZ      = 0x0F
    BW_RATE_800HZ       = 0x0E
    BW_RATE_400HZ       = 0x0D
    BW_RATE_200HZ       = 0x0C
    BW_RATE_100HZ       = 0x0B
    BW_RATE_50HZ        = 0x0A
    BW_RATE_25HZ        = 0x09
 
    RANGE_2G            = 0x00
    RANGE_4G            = 0x01
    RANGE_8G            = 0x02
    RANGE_16G           = 0x03
 
    MEASURE             = 0x08
    AXES_DATA           = 0x32

    device_address = None
    i2cbus = None
 
    def __init__(self, address = 0x53, bandwidthrate = BW_RATE_100HZ, range = RANGE_2G):        
        
        self.device_address = address
                
        # select the correct i2c bus for this revision of Raspberry Pi
        revision = ([l[12:-1] for l in open('/proc/cpuinfo','r').readlines() if l[:8]=="Revision"]+['0000'])[0]
        self.i2cbus = smbus.SMBus(1 if int(revision, 16) >= 4 else 0)
        
        self.setBandwidthRate(bandwidthrate)
        self.setRange(range)
        self.enableMeasurement()

    def enableMeasurement(self):
        self.i2cbus.write_byte_data(self.device_address, self.POWER_CTL, self.MEASURE)
 
    def setBandwidthRate(self, rate_flag):
        self.i2cbus.write_byte_data(self.device_address, self.BW_RATE, rate_flag)
 
    # set the measurement range for 10-bit readings
    def setRange(self, range_flag):
        value = self.i2cbus.read_byte_data(self.device_address, self.DATA_FORMAT)
 
        value &= ~0x0F;
        value |= range_flag;  
        value |= 0x08;
 
        self.i2cbus.write_byte_data(self.device_address, self.DATA_FORMAT, value)
 
    # returns the current reading from the sensor for each axis
    #
    # parameter gforce:
    #    False (default): result is returned in m/s^2
    #    True           : result is returned in gs
    def getAxes(self, gforce = False):
        bytes = self.i2cbus.read_i2c_block_data(self.device_address, self.AXES_DATA, 6)
 
        x = bytes[0] | (bytes[1] << 8)
        if(x & (1 << 16 - 1)):
            x = x - (1<<16)
 
        y = bytes[2] | (bytes[3] << 8)
        if(y & (1 << 16 - 1)):
            y = y - (1<<16)
 
        z = bytes[4] | (bytes[5] << 8)
        if(z & (1 << 16 - 1)):
            z = z - (1<<16)
 
        x = x * self.SCALE_MULTIPLIER 
        y = y * self.SCALE_MULTIPLIER
        z = z * self.SCALE_MULTIPLIER
 
        if gforce == False:
            x = x * self.EARTH_GRAVITY_MS2
            y = y * self.EARTH_GRAVITY_MS2
            z = z * self.EARTH_GRAVITY_MS2
 
        x = round(x, 4)
        y = round(y, 4)
        z = round(z, 4)
 
        return {"x": x, "y": y, "z": z}