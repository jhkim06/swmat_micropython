import serial
from serial.tools import list_ports

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
    print (comm.listports())
    comm.connect("/dev/cu.usbmodem13301")
    ret = comm.send_data(3)
    print (ret)


if __name__ == "__main__":
    main()
