from serial import Serial
from random import randint

s = Serial('/dev/ttyUSB0', 9600)

msg_id = input('Message ID (Empty for random):')
if not msg_id:
    msg_id = hex(randint(0, 4095))[2:]
message = input('Type your data:\n')
path = input('Type path:')


raw_data = '{}|{}|{}|{}\n'.format(msg_id, 'C', path, message)

s.write(raw_data.encode())
s.close()
