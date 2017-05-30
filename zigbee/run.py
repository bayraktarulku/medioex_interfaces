from serial import Serial
from medioex_zigbee_interface import MedIOExInterface

if __name__ == '__main__':
    serial_port = Serial('/dev/ttyUSB0', 9600)
    m = MedIOExInterface(serial_port)
    m.run()
