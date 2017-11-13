import View.temperature as view

import Frame.mainframe as f
from serial import *
tempInput = 0

try:
    ser = Serial(
        port='COM4',
        baudrate=19200,
        parity=PARITY_NONE,
        stopbits=STOPBITS_ONE,
        bytesize=EIGHTBITS,
        timeout=0)
    print("Temp Connected")

except:
    print("Temp disconnected")

def printTemp():
    global tempInput
    try:
        value = ser.read()
        #print(value)
        if value:
            tempNum = int.from_bytes(value, byteorder='little')
         #   print(tempNum)
            tempInput = tempNum
            view.t1.tempLabelCount.config(text="  {}C".format(tempNum))
            #checkPreset(lightToPercentage)
            #updateGraph(lightToPercentage)
            getTemp()
    except:
        pass    #print("doei")


def getTemp():
    #print(lightInput)
    return tempInput

'''
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
'''