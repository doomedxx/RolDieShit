from View import light as view
from View import lightgraph as graph
import Frame.mainframe as f
from serial import *
from Model.roller_model import checkLight as checkLight
from Model.roller_model import checkTime as checkTime
from Model.clock_model import getTime as currentTime
import threading
import random
lightInput = 0

try:
    ser = Serial(
        port='COM5',
        baudrate=19200,
        parity=PARITY_NONE,
        stopbits=STOPBITS_ONE,
        bytesize=EIGHTBITS,
        timeout=0)
except:
    print("Disconnected")

def updateTick():
    global lightInput
    f.root.after(1000, updateTick)
    f.root.after(1000, checkTime)
    try:
        value = ser.read()
        min = 25                #min light value
        max = 60                #max light value
        if value:
            lightNum = int.from_bytes(value, byteorder='little')
            #print(lightNum)
            lightToPercentage = round((lightNum - min) * 100 / (max - min))
            lightInput = lightToPercentage
            #print(lightToPercentage)
            view.l1.lightLabelCount.config(text="{}%".format(lightToPercentage))
            checkPreset(lightToPercentage)
            updateGraph(lightToPercentage)
            getLight()
    except:
        view.l1.lightLabelCount.config(text="N/A")
        view.l1.lightLabelPreset.config(text="[Restart]")

def getLight():
    #print(lightInput)
    return lightInput


def checkPreset(light):
    if light >= 0 and light <= 20:
        view.l1.lightLabelPreset.config(text="[Very Dark]")
    elif light >= 20 and light < 40:
        view.l1.lightLabelPreset.config(text="[Dark]")
    elif light >= 40 and light < 50:
        view.l1.lightLabelPreset.config(text="[Dimmed]")
    elif light >= 50 and light < 80:
        view.l1.lightLabelPreset.config(text="[Bright]")
    elif light >= 80 and light < 99:
        view.l1.lightLabelPreset.config(text="[Very Bright]")
    elif light >= 99:
        view.l1.lightLabelPreset.config(text="[Full Bright]")

averageList = [0,0,0,0,0,0,0,0,0,0,0]
cycle = 0
def updateGraph(light):
    global averageList
    global cycle
    graph.g3.x.append(cycle)
    graph.g3.y.append(light)
    cycle+=1
    average = round(sum(graph.g3.y) / len(graph.g3.y))
    averageList.append(average)
   # print(len(graph.g3.x))
    if cycle >= 11:
        graph.g3.line2.set_xdata(graph.g3.x)
        graph.g3.line2.set_ydata(averageList)


    graph.g3.line.set_ydata(graph.g3.y)
    graph.g3.line.set_xdata(graph.g3.x)
    graph.g3.canvas.draw()
