from View import light as view
from View import lightgraph as graph
from View import graph2 as graph2
#from View import statswidget as stats
import Frame.mainframe as f
from serial import *
from random import randint
from Model.roller_model import checkMode as checkMode
from Model.temp_model import printTemp as printTemp
lightInput = 0
connection = True
counter = 50
count = 1
list_of_light = [50]

## Checks serial connection
try:
    ser = Serial(
        port='COM5',
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

def getConnection(): ## Returns the value of connection
    return connection

def totalLight(): ## Returns the average temperature
    average = round(counter/count,1)
    return average

def updateTick(): ## Updates light value
    global light
    global lightInput
    global counter
    global count
    f.root.after(200, updateTick)
    f.root.after(1000, checkMode)
    f.root.after(1000, printTemp)
    try:
        value = ser.read()
        min = 35                #min light value
        max = 60                #max light value
        if value: ## Checks if value is recieved and converts it to decimal number
            lightNum = int.from_bytes(value, byteorder='little')
            #print(lightNum)
            lightToPercentage = round((lightNum - min) * 100 / (max - min))
            lightInput = lightToPercentage
            counter += lightInput
            count += 1
            #print(lightToPercentage)
            if lightInput not in list_of_light:
                list_of_light.append(lightInput)
            view.l1.lightLabelCount.config(text="{}%".format(lightToPercentage))
            checkPreset(lightToPercentage)
            updateGraph(lightToPercentage)
            getLight()
            totalLight()
    except:
        view.l1.lightLabelCount.config(text="N/A")
        view.l1.lightLabelPreset.config(text="[Restart]")

def getLight(): ## returns current light percentage
    return lightInput

def getLightSimu():
    return light

def maxLight(): ## returns maximum light percentage measured
    f.root.after(1000,maxLight)
    return max(list_of_light)

def minLight(): ##returns minimum light percentage measured
    f.root.after(1000, minLight)
    return min(list_of_light)

def checkPreset(light): ## sets a preset based on the current light percentage
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
SetX = 100
def updateGraph(light): ##Updates the graph for light input
    global averageList
    global SetX
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
    if cycle == SetX:
        SetX+=50
        graph.update(SetX)
