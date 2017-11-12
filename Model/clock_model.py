import time
import Frame.mainframe as frame
from View import clock as clock
from View.Settings import setting_clock as clock_setting

time_string = time.strftime('%H:%M:%S')


def setTime(): ##
    frame.root.after(1000, setTime)
    global time_string
    time_day = time.strftime('%A')
    time_string = time.strftime('%H:%M:%S')
    clock.c.clockLabelTime.config(text=time_string)
    clock.c.clockLabelDay.config(text=time_day)
    getTime()


def getTime():
    return time_string

def getHour():
    hour_string = time.strftime('%H')
    return hour_string

def getMinute():
    minute_string = time.strftime('%M')
    return minute_string
