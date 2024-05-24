# example from https://www.instructables.com/Raspberry-Pi-Pico-MX7219-Eight-Digits-of-Seven-Seg/

# clk -> GPIO16 10
# DIN -> GPIO17 11
# cs  -> GPIO19 13

import time

import max7219_8digit
from machine import Pin, SPI

def ex_upcount():
    count = 9950
    spi = SPI(0, baudrate=10000000, polarity=1, phase=0, sck=Pin(16), mosi=Pin(17))
    ss = Pin(19, Pin.OUT)
    display = max7219_8digit.Display(spi, ss)

    while True:
        temp = "UP -" + str(count)
        display.write_to_buffer(temp)
        display.display()

        count += 1
        if count == 10000:
            count = 0

        time.sleep(0.2)

    return

def display(line):
    spi = SPI(1, baudrate=10000000, polarity=1, phase=0, sck=Pin(10), mosi=Pin(11))
    ss = Pin(13, Pin.OUT)

    display = max7219_8digit.Display(spi, ss)
    display.write_to_buffer(line)
    display.display()

    time.sleep(1.0)

    return
