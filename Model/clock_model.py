import time
import builtins
import Frame.mainframe as frame
from View import clock as clock
from View.Settings import setting_clock as clock_setting

timeMode = "12-hour"
time_string = time.strftime('%H:%M:%S')
def updateClock():
    frame.root.after(1000, setTime)

def setTime():
    global time_string
    time_day = time.strftime('%A')
    time_string = time.strftime('%H:%M:%S')
    clock.c.clockLabelTime.config(text=time_string)
    clock.c.clockLabelDay.config(text=time_day)
    getTime()
    updateClock()


def getTime():
    return time_string

def onEnterScript():
    clock_setting.c1.setTooltip("Change clock format")

def onLeaveScript():
    clock_setting.c1.setTooltip("")

def go12():
    print("Werkt")