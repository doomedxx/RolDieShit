from serial import *

import struct

def __transmit(data):
    __init_serial()
    ser.write([data])

def __init_serial():
    ser = Serial(
            port='COM3',
            baudrate=19200,
            parity=PARITY_NONE,
            stopbits=STOPBITS_ONE,
            bytesize=EIGHTBITS,            timeout=0)

    print("connected to: " + ser.portstr)

while True:
   value = ser.readline()
   hex_val = int.from_bytes(value,byteorder='little')
   if value:
        print(hex_val)
        ser.write([0x01])