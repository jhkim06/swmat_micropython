import pcf8575
from machine import I2C


def setup_i2c(i2c_block=1):
    i2c = I2C(i2c_block)
    # check if there is connected device
    i2c.scan() # a list of 7-bit addresses
    # create PCF objects for all address
    # will use 16 PCF8575 in the end
    # 16 pad for each PCF8575
    # 0~15
    return i2c

def pcf(i2c, addr):
    # pcfs = []
    # sw.select_switch(switch_number)
    # sw.diable_switch()
    # matching pcf address and sensor number
    '''
    module for 16 sensor and use 16 module?
    sensor_pcf = {0: '0x20', 1: '0x20', ... 255: '0x27'}
    '''
    pcf = pcf8575.PCF8575(i2c, addr)
    return pcf
