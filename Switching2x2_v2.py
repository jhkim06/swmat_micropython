import pcf8575
from PICOI2C import PICOI2C
import utime

switch_to_pcf_map = {
        0: 8, 1: 8,  2: 8,  3: 8,  4: 8,  5: 8,  6: 8,  7: 8,
        8: 8, 9: 8, 10: 8, 11: 8, 12: 8, 13: 8, 14: 8, 15: 8,
}

i2c_to_pcf_map = {
        # key format: <Pico I2C controller#>_<ADDRESS>
        # currently only '1_32' available
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
        # TODO use error handle for the case no i2c found
        self.disable_all_switches()

    def __init_pcfs(self):
        for i2c_id, i2c, address in self.pico_i2c.get_all_address():
            pcf_id = i2c_to_pcf_map[str(i2c_id) + '_' + str(address)]
            self.PCFs[pcf_id] = pcf8575.PCF8575(i2c, address)

    def _switch_to_pin_num(self, switch_num):
        pin_num = switch_num % 16
        if pin_num > 7:
            pin_num += 2
        return pin_num

    def print_connected_pcfs(self):
        for key in self.PCFs:
            print(f'#{key} PCF is connected')

    def print_pin_status_on_pcf(self, pcf_id=8):
        self.PCFs[pcf_id].print_pins()

    # report all switch status
    def report_switch_status(self):
        for key in self.PCFs:
            print(f'#{key} PCF pin status')
            self.print_pin_status_on_pcf(key)

    def enable_switch(self, nsw, exclusive=True):
        if exclusive:
            self.disable_all_switches()
        pin_num = self._switch_to_pin_num(nsw)
        self.PCFs[switch_to_pcf_map[nsw]].pin(pin_num, ON)

    def disable_switch(self, nsw):
        pin_num = self._switch_to_pin_num(nsw)
        self.PCFs[switch_to_pcf_map[nsw]].pin(pin_num, OFF)

    def disable_all_switches(self):
        for key in self.PCFs:
            self.PCFs[key].port = 0x0000

