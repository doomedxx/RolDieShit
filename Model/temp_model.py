import View.temperature as view
import View.graph2 as graph
import Frame.mainframe as f
from random import randint
from serial import *
from time import sleep

tempInput = 0
connection = True
counter = 21
count = 1
list_of_temps = []
temp = 22

## Checks if the Arduino is connected
try:
    ser = Serial(
        port='COM4',
        baudrate=19200,
        parity=PARITY_NONE,
        stopbits=STOPBITS_ONE,
        bytesize=EIGHTBITS,
        timeout=0)
    print("Temp Connected")
    connection = True
except:
    print("Temp disconnected")
    connection = False

def getConnection(): ## Returns if Temp sensor is connected or not
    return connection

def totalTemp(): ##Returns the average temp of all temps measured
    average = round(counter/count,1)
    return average

def printTemp(): ## Reads the input from arduino and converts it to a decimal number, added some testing code to animate temperature changes
    global tempInput
    global counter
    global count
    global temp
    try:
        value = ser.readline()
        tempNum = int.from_bytes(value,byteorder='little')
        if value:
            #print(tempNum)
            ser.write([0x01])
            counter += tempNum
            tempInput = tempNum
            count +=1
            view.t1.tempLabelCount.config(text="  {}C".format(tempNum))
            if tempNum not in list_of_temps:
                list_of_temps.append(tempNum)
            updateGraph(tempNum)
            getTemp()
        else:
            rand = randint(0,1)
            if rand == 1:
                temp += 0.5
            elif rand == 0:
                temp -= 0.5
            sleep(2)
            tempRound = int(round(temp,0))
            #view.t1.tempLabelCount.config(text="  {}C".format(tempRound))
            if tempRound not in list_of_temps:
                list_of_temps.append(tempRound)
            updateGraph(temp)
            getTemp()
    except:
        view.t1.tempLabelCount.config(text="N/A")

def getTemp(): ## Return current temperature
    return tempInput

def maxTemp():  ## Returns the maximum temperature measured
    return max(list_of_temps)

def minTemp():  ## Retruns the minimum temperature measured
    return min(list_of_temps)

averageList = [0,0,0,0,0,0,0,0,0,0,0]
cycle = 0
xSet = 100
def updateGraph(temp): ## Updates the temperature graph
    global averageList
    global xSet
    global cycle
    graph.g2.x.append(cycle)
    graph.g2.y.append(temp)
    cycle+=1
    average = round(sum(graph.g2.y) / len(graph.g2.y))
    averageList.append(average)
    # print(len(graph.g2.x))
    if cycle >= 11:
        graph.g2.line2.set_xdata(graph.g2.x)
        graph.g2.line2.set_ydata(averageList)


    graph.g2.line.set_ydata(graph.g2.y)
    graph.g2.line.set_xdata(graph.g2.x)
    graph.g2.canvas.draw()
    if cycle == xSet:
        xSet+=100
        graph.update(xSet)

    graph.g2.line.set_ydata(graph.g2.y)
    graph.g2.line.set_xdata(graph.g2.x)
    graph.g2.canvas.draw()