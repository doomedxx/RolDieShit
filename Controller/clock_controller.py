import time
import threading
import Model.clock_model as model
def timeString():
    time_string = time.strftime('%H:%M:%S')
    threading.Timer(1, timeString).start()
    return time_string

def onEnter(event):
    model.onEnterScript()

def onLeave(event):
    model.onLeaveScript()