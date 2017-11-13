from View import light as view
#from View import graph1 as graph1
from View import lightgraph as graph
import Frame.mainframe as f
from serial import *
from random import randint
from Model.roller_model import checkMode as checkMode
from Model.temp_model import printTemp as printTemp
lightInput = 0
connection = True
counter = 50
count = 1

try:
    ser = Serial(
        port='COM3',
        baudrate=19200,
        parity=PARITY_NONE,
        stopbits=STOPBITS_ONE,
        bytesize=EIGHTBITS,
        timeout=0)
    print("Light Connected")
    connection = True
except:
    print("Light Disconnected")
    connection = False

def getConnection():
    return connection

def totalLight():
    average = round(counter/count,1)
    #graph1.g1.averagetempvalue.config(text="{}%".format(average))
    return average

light = 50 # Voor simulatie doeleinde
def updateTick():
    global light
    global lightInput
    global counter
    global count
    f.root.after(1000, updateTick)
    f.root.after(1000, checkMode)
    f.root.after(1000, printTemp)
    try:
        value = ser.read()

        min = 25                #min light value
        max = 60                #max light value
        if value:
            lightNum = int.from_bytes(value, byteorder='little')
            #print(lightNum)
            lightToPercentage = round((lightNum - min) * 100 / (max - min))
            lightInput = lightToPercentage
            counter += lightInput
            count += 1
            #print(lightToPercentage)
            view.l1.lightLabelCount.config(text="{}%".format(lightToPercentage))
            average = round(counter / count, 1)
            graph1.g1.averagetempvalue.config(text="{}%".format(average))
            checkPreset(lightToPercentage)
            updateGraph(lightToPercentage)
            getLight()
            totalLight()
    except:
        rand = randint(0,1)
        if rand == 1:
            light+=1
        elif rand == 0:
            light-=1
        view.l1.lightLabelCount.config(text=light)
        updateGraph(light)
        view.l1.lightLabelPreset.config(text="[Restart]")

def getLight():
    #print(lightInput)
    return lightInput

def getLightSimu():
    return light


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
xSet = 100
def updateGraph(light):
    global averageList
    global xSet
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
    if cycle == xSet:
        print(xSet)
        xSet+=100
        print(xSet)
        graph.update(xSet)
