print ("Start measuring 3d printer!")

from time import sleep
import adxl345_lib

GY291 = adxl345_lib.ADXL345()

i = 1
while i < 10:
    i += 1
    sleep(0.5)
    axes = GY291.getAxes(True)
    print "ADXL345 on address 0x%x:" % (GY291.device_address)
    print "   x = %.3fG" % ( axes['x'] )
    print "   y = %.3fG" % ( axes['y'] )
    print "   z = %.3fG" % ( axes['z'] )
 
