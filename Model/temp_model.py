import View.temperature as view
import View.graph2 as graph
import Frame.mainframe as f
from random import randint
from serial import *
tempInput = 0
connection = True
counter = 21
count = 1
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

def getConnection():
    return connection

def totalTemp():
    average = round(counter/count,1)
    return average


temp =  25 #Simulatie doeleinde
def printTemp():
    global tempInput
    global counter
    global count
    try:
        value = ser.read()
        #print(value)
        if value:
            tempNum = int.from_bytes(value, byteorder='little')
         #   print(tempNum)
            tempInput = tempNum
            counter += tempInput
            count +=1
            view.t1.tempLabelCount.config(text="  {}C".format(tempNum))
            getTemp()
    except:
        global temp
        rand = randint(0,1)
        if rand == 1:
            temp+=1
        if rand == 0:
            temp-=1
            updateGraph(temp)
        view.t1.tempLabelCount.config(text=temp)



def getTemp():
    #print(lightInput)
    return tempInput

averageList = [0,0,0,0,0,0,0,0,0,0,0]
cycle = 0
xSet = 100
def updateGraph(temp):
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