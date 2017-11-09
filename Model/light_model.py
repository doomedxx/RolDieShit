from View import light as view
from View import lightgraph as graph
import Frame.mainframe as f
from Model.clock_model import getTime as currentTime
import threading
import random

lightNum = 50
def updateTick():
    global lightNum
    f.root.after(500, updateTick)
    upordown = random.randint(0,1)
    if upordown == 0:
        lightNum-=5
    else:
        lightNum+=5
    if lightNum >= 100:
        lightNum = 100
    if lightNum <= 0:
        lightNum = 0
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

averageList = []
cycle = 0
def updateGraph(light):
    global averageList
    global cycle
    graph.g3.y.pop(0)
    graph.g3.y.append(light)

    average = round(sum(graph.g3.y) / len(graph.g3.y))
    averageList.append(average)
    if cycle >= 11:
        averageList.pop(0)
        graph.g3.line2.set_ydata(averageList)
    graph.g3.line.set_ydata(graph.g3.y)
    graph.g3.canvas.draw()

    cycle+=1