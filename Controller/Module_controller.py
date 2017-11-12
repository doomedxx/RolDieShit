import serial


class Modulecontroller:
    def __init__(self):
        self.ser = serial.Serial(port='COM1', baudrate=19200, )

    # setup serialconnection
    def init_transmit(self):
        self.ser = serial.Serial(port='COM3', baudrate=19200, )
        print("connected to: " + self.ser.portstr)

    # Stuur data naar de arduino
    def transmit(self, msg):
        self.ser.write([msg])

    # ontvang data van de arduino
    def receive(self):
        while True:
            self.s = self.ser.read()
            value = int.from_bytes(self.s, byteorder='little')
            print(value)

    # scherm inklappen
    def open_screen(self):
        self.ser.write([1])

    # scherm openen
    def close_screen(self):
        self.ser.write([2])

        # def setMaxDistance(self, value):
