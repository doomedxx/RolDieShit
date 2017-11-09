from View import light as view
from View import lightgraph as graph
import Frame.mainframe as f
from Model.clock_model import getTime as currentTime
import threading
import random

lightNum = 50
def updateTick():
    global lightNum
    f.root.after(100, updateTick)
    upordown = random.randint(0,1)
    if upordown == 0:
        lightNum-=2
    else:
        lightNum+=2
    if lightNum >= 100:
        lightNum = 95
    if lightNum <= 0:
        lightNum = 5
    checkPreset(lightNum)
    updateGraph(lightNum)
    view.l1.lightLabelCount.config(text="{}%".format(lightNum))

def checkPreset(light):
    if light < -10:
        view.l1.lightLabelPreset.config(text="[ Get help! ]")
    elif light < 0:
        view.l1.lightLabelPreset.config(text="[ Wtf!? ]")
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
    print(len(graph.g3.x))
    if cycle >= 11:
        graph.g3.line2.set_xdata(graph.g3.x)
        graph.g3.line2.set_ydata(averageList)


    graph.g3.line.set_ydata(graph.g3.y)
    graph.g3.line.set_xdata(graph.g3.x)
    graph.g3.canvas.draw()
