import utime
import usbcomm
from Switching2x2_v1 import Switching2x2_v1

def main():
    swm = Switching2x2_v1() 
    swm.enable()
    
    utime.sleep(1) 

    swm.reset_all_sw()

    while True:
        Nsw = usbcomm.listen()
        swm.select_switch(Nsw)

if __name__ == "__main__":
    main()

