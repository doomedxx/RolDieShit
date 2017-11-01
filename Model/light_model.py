from View_Widgets import light as view
import threading
import random

lightNum = 100
def updateTick():
    global lightNum
    threading.Timer(1, view.update)._is_stopped
    upordown = random.randint(0,1)
    if upordown == 0:
        lightNum-=1
    else:
        lightNum+=1
    view.l1.lightLabelCount.config(text=lightNum)
    threading.Timer(1, view.update).start()