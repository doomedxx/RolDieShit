from serial import *

ser ='';

def transmit_msg(message):
    init_serial()
    ser.write([message])
    return

def init_serial():
    ser = Serial(
            port='COM3',
            baudrate=19200,
            parity=PARITY_NONE,
            stopbits=STOPBITS_ONE,
            bytesize=EIGHTBITS,            timeout=0)

    print("connected to: " + ser.portstr)
    return