import serial
from serial.tools import list_ports
import argparse

parser = argparse.ArgumentParser(description='Send an integer to pico')
parser.add_argument('integer', type=int, nargs='?', default=1, help='an interger to send to pico')
args = parser.parse_args()

class usbcomm:
    ser = []

    def __init__(self):
        pass

    def connect(self, port):
        self.ser = serial.Serial(port=port, baudrate=115200, timeout=1)

    def listports(self):
        l = list_ports.comports() 
        connected = [] 
        for i in l:
            connected.append(i.device)

        return connected

    def send_data(self, data):
        self.ser.write(f"{data}\r".encode())
        mes = self.ser.read_until().strip()
        return mes.decode()


def main():
    comm = usbcomm()
    # print (comm.listports())
    # comm.connect("/dev/cu.usbmodem13301")
    comm.connect("COM3")
    print('Send ', args.integer)
    ret = comm.send_data(args.integer)
    print (ret)


if __name__ == "__main__":
    main()
