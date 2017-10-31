from View_Widgets import light as view
import threading
import random

lightNum = 100
def updateTick(tick):
    global lightNum
    upordown = random.randint(0,1)
    if upordown == 0:
        lightNum-=1
    else:
        lightNum+=1
    view.l1.lightLabelCount.config(text=lightNum)
    threading.Timer(tick, view.update).start()