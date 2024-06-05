from machine import I2C


class PICOI2C:
    def __init__(self):
        self.i2c = {}
        self.i2c[0] = I2C(0)
        self.i2c[1] = I2C(1)

    def scan(self,i2c_id=0):
        self.i2c[i2c_id].scan()

    def get_all_address(self):
        for i2c_id in [0, 1]:
            addresses = self.i2c[i2c_id].scan()
            for addr in addresses:
                yield i2c_id, self.i2c[i2c_id], addr

