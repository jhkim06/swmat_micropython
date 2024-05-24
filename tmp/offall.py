import utime
from Switching2x2_v1 import Switching2x2_v1

def main():
    swm = Switching2x2_v1()
    swm.enable()

    utime.sleep(0.1)

    """
    for i in range(100):
        nch = i % 6 + 1
        print (nch)
        swm.select_mux(nch)
        #print(f"failed to select_mux #{nch}")
        utime.sleep(1)
        """
    
    swm.ADG633[0].set_pins("0000")
    swm.ADG633[1].set_pins("0000")

    swm.ADG1406[0].set_pins("00000")

if __name__ == "__main__":
    main()

