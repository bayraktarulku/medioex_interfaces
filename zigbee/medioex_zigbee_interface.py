from serial import Serial
import requests
import zigbee_interface
from time import sleep
import json

API_BASE_URL = 'http://127.0.0.1:5000/api'


class MedIOExInterface(zigbee_interface.ZigbeeService):

    def __init__(self, *args, **kwargs):
        super(MedIOExInterface, self).__init__(
            data_handler=self._data_handler, *args, **kwargs)

    def _data_handler(self, message):
        commands = message.split(',')
        for c in commands:
            if c[0] == 'D':
                pin = int(c[1], 16) + 1
                val = int(c[2])
                requests.get(API_BASE_URL + '/do',
                             params={'pin': pin, 'val': val})

            elif c[0] == 'R':
                pin = int(c[1], 16) + 13
                val = int(c[2])
                requests.get(API_BASE_URL + '/ro',
                             params={'pin': pin, 'val': val})

            elif c[0] == 'A':
                pin = int(c[1])
                val = int(c[2:], 16)
                requests.get(API_BASE_URL + '/ao',
                             params={'pin': pin, 'val': val})
            elif c[0] == 'N':
                continue
            elif c[0] == 'I':
                continue
            sleep(0.1)

        di_values = []
        for i in range(16, 0, -1):
            r = requests.get(API_BASE_URL + '/di', params={'pin': i})
            di_values.append(r.json()['value'])
        di_values = hex(int(''.join(di_values), 2))[2:].zfill(4)

        ai_values = []
        for i in range(4):
            r = requests.get(API_BASE_URL + '/ai', params={'pin': i + 1})
            ai_values.append(r.json()['value'])
        ai_values = [hex(ai_values[1])[2:].zfill(3)
                     for i in range(4)]
        return di_values + str.join('', ai_values)
