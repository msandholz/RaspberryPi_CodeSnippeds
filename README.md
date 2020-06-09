# RaspberryPi_Sensors

Hallo, dies ist ein Test!

![](GPIO-Pinout-Diagram-2.png)

## How to use the I2C-Interface

1. Enable the I2C-Interface with `sudo raspi-config` and select `4. Interfacing Options` and `P5 I2C`

2. Install two packages to use I2C: 
    - `sudo apt-get install i2c-tools`
    - `sudo apt-get install python-smbus`

3. Add the pi-user to the I2C-Access group with `sudo adduser pi i2c` and reboot the system with `sudo reboot`

4. Test the software with `i2cdetect -y 1` and `i2cdetect -F 1` to see if there is anything connected.

5. Reading Verion I2C-Dump with: `i2cdump -V`

6. Dump Device-Registers with `i2cdump 1 0x53`
```
No size specified (using byte-data access)
WARNING! This program can confuse your I2C bus, cause data loss and worse!
I will probe file /dev/i2c-1, address 0x53, mode byte
Continue? [Y/n] y
     0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f    0123456789abcdef
00: e5 00 00 00 00 00 00 00 00 00 00 00 00 00 00 4a    ?..............J
10: 00 00 10 00 00 00 00 00 00 00 00 00 00 00 00 00    ..?.............
20: 00 00 00 00 00 00 00 00 00 00 00 00 0a 00 00 00    ............?...
30: 02 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00    ?...............
40: e5 00 00 00 00 00 00 00 00 00 00 00 00 00 00 4a    ?..............J
50: 00 00 10 00 00 00 00 00 00 00 00 00 00 00 00 00    ..?.............
60: 00 00 00 00 00 00 00 00 00 00 00 00 0a 00 00 00    ............?...
70: 02 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00    ?...............
80: e5 00 00 00 00 00 00 00 00 00 00 00 00 00 00 4a    ?..............J
90: 00 00 10 00 00 00 00 00 00 00 00 00 00 00 00 00    ..?.............
a0: 00 00 00 00 00 00 00 00 00 00 00 00 0a 00 00 00    ............?...
b0: 02 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00    ?...............
c0: e5 00 00 00 00 00 00 00 00 00 00 00 00 00 00 4a    ?..............J
d0: 00 00 10 00 00 00 00 00 00 00 00 00 00 00 00 00    ..?.............
e0: 00 00 00 00 00 00 00 00 00 00 00 00 0a 00 00 00    ............?...
f0: 02 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00    ?...............
```




https://pypi.org/project/mpu6050-raspberrypi/

https://github.com/Arijit1080/mpu6050-with-Raspberry-Pi

https://github.com/pimoroni/adxl345-python
