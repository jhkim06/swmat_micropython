import utime
import usbcomm
from Switching2x2_v1 import Switching2x2_v1
from ledctl import LED
from seg7ctl import display


def main():
    swm = Switching2x2_v1() 
    swm.enable()

    led = LED()
    led.on()
    utime.sleep(0.5)
    led.off()
    
    utime.sleep(1) 

    swm.reset_all_sw()

    pre = "CH "
    
    while True:
        try:
            Nsw = usbcomm.listen()
            Nsw = int(Nsw)

            led.indicate_sw(Nsw) 
            swm.select_switch(Nsw) # TODO handle index error
            line = pre + f"{Nsw}" 

            display(line)

            utime.sleep(1.0)
        except KeyboardInterrupt:
            break
        except:
            print('error')
            led.indicate_error()


if __name__ == "__main__":
    main()
