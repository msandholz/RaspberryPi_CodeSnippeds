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


https://pypi.org/project/mpu6050-raspberrypi/

https://github.com/Arijit1080/mpu6050-with-Raspberry-Pi

https://github.com/pimoroni/adxl345-python
