from View import light as view
from View import graph3 as graph
import Frame.mainframe as f
import threading
import random

lightNum = 100
def updateTick():
    global lightNum
    f.root.after(500, updateTick)
    upordown = random.randint(0,1)
    if upordown == 0:
        lightNum-=1
    else:
        lightNum+=1
    view.l1.lightLabelCount.config(text=lightNum)