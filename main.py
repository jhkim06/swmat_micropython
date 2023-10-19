import utime
from Switching2x2_v1 import Switching2x2_v1

def main():
    swm = Switching2x2_v1()
    swm.enable()

    utime.sleep(1)

    for i in range(100):
        swm.select_mux(i%6)
        utime.sleep(1)

    sw.reset_all_sw()
    sw.disable()

if __name__ == "__main__":
    main()

