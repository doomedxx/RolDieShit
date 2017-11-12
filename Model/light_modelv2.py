from View_Widgets import light as view
from Serial import *											//import				
import Frame.mainframe as f
import threading
import random
import struct													//import


ser = serial.Serial('COM3', 9600, timeout=0)					//waarde van lichtsensor Arduino naar variabele ser
while True:
	value = ser.readline()										//functie van pyserial
	toFloat = struct.unpack('!f', bytes.fromhex(value))[0]		//waarde omzetten van hex naar float


lightNum = toFloat												//lightnum is % light
def updateTick():
    global lightNum
    f.root.after(1000, updateTick)
    upordown = random.randint(0,1)
    if upordown == 0:
        lightNum-=1
    else:
        lightNum+=1
    view.l1.lightLabelCount.config(text=lightNum)
