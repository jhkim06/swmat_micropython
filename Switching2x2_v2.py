import pcf8575
from PICOI2C import PICOI2C

switch_to_pcf_map = {
        0: 8, 1: 8,  2: 8,  3: 8,  4: 8,  5: 8,  6: 8,  7: 8,
        8: 8, 9: 8, 10: 8, 11: 8, 12: 8, 13: 8, 14: 8, 15: 8,

        16: 1, 17: 1, 18: 1, 19: 1, 20: 1, 21: 1, 22: 1, 23: 1,
        24: 1, 25: 1, 26: 1, 27: 1, 28: 1, 29: 1, 30: 1, 31: 1,
}

i2c_to_pcf_map = {
        '0_32': 0, '0_33': 1, '0_34':  2, '0_35':  3, '0_36':  4, '0_37':  5, '0_38':  6, '0_37':  7,
        '1_32': 8, '1_33': 9, '1_34': 10, '1_35': 11, '1_36': 12, '1_37': 13, '1_38': 14, '1_37': 15,
}

ON = 1
OFF = 0

# pcf0, from  0~15
# pcf1, from 16~31

class Switching2x2_v2:
    def __init__(self):
        self.PCFs = {}  # will use 16 PCF8575 chips in the end
        self.pico_i2c = PICOI2C() 

        self.__init_pcfs()

    def __init_pcfs(self):
        for i2c_id, i2c, address in self.pico_i2c.get_all_address():
            pcf_id = i2c_to_pcf_map[str(i2c_id) + '_' + str(address)]
            self.PCFs[pcf_id] = pcf8575.PCF8575(i2c, address)

    def __switch_num_to_pin_num(self, switch_num):
        pin_num = switch_num % 16
        if pin_num > 7:
            pin_num += 2
        return pin_num

    def print_connected_pcfs(self):
        for key in self.PCFs:
            print(f'#{key} PCF is connected')

    def enable_switch(self, nsw):
        pin_num = self.__switch_num_to_pin_num(nsw)
        self.PCFs[switch_to_pcf_map[nsw]].pin(pin_num, ON)

    def disable_switch(self, nsw):
        pin_num = self.__switch_num_to_pin_num(nsw)
        self.PCFs[switch_to_pcf_map[nsw]].pin(pin_num, OFF)

    def print_pin_status_on_pcf(self, pcf_id=8):
        self.PCFs[pcf_id].print_pins()
