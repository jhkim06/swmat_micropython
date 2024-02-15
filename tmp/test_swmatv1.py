from machine import Pin
import utime

pin_adg633_1 = []
pin_adg633_2 = []
pin_adg1406_1 = []
pin_led = Pin("LED", mode=Pin.OUT)

pin_adg633_1.append(Pin(0, mode=Pin.OUT))
pin_adg633_1.append(Pin(1, mode=Pin.OUT))
pin_adg633_1.append(Pin(3, mode=Pin.OUT))
pin_adg633_1.append(Pin(4, mode=Pin.OUT))

pin_adg633_2.append(Pin(5, mode=Pin.OUT))
pin_adg633_2.append(Pin(6, mode=Pin.OUT))
pin_adg633_2.append(Pin(8, mode=Pin.OUT))
pin_adg633_2.append(Pin(9, mode=Pin.OUT))

pin_adg1406_1.append(Pin(20, mode=Pin.OUT))
pin_adg1406_1.append(Pin(21, mode=Pin.OUT))
pin_adg1406_1.append(Pin(23, mode=Pin.OUT))
pin_adg1406_1.append(Pin(24, mode=Pin.OUT))
pin_adg1406_1.append(Pin(25, mode=Pin.OUT))

while 1:
    pin_led.toggle()
    pin_adg633_1[0].toggle()
    utime.sleep(0.1)
