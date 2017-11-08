from View import setting_clock as clock_setting
from View import clock as clock
import Frame.mainframe as frame
import time
import threading

timeMode = "12-hour"

def updateClock():
    frame.root.after(10, setTime)

def setTime():
    time_day = time.strftime('%A')
    time_string = time.strftime('%H:%M:%S')
    clock.c.clockLabelTime.config(text=time_string)
    clock.c.clockLabelDay.config(text=time_day)
    updateClock()

def onEnterScript():
    clock_setting.c1.setTooltip("Change clock format")

def onLeaveScript():
    clock_setting.c1.setTooltip("")

def go12():
    print("Werkt")