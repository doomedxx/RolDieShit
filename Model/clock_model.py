import time
import Frame.mainframe as frame
from View import clock as clock

time_string = time.strftime('%H:%M:%S')


def setTime(): ## Update de tijd elke seconde (Net als een klok dus.)
    frame.root.after(1000, setTime)
    global time_string
    time_day = time.strftime('%A')
    time_string = time.strftime('%H:%M:%S')
    clock.c.clockLabelTime.config(text=time_string)
    clock.c.clockLabelDay.config(text=time_day)
    getTime()


def getTime(): ## Returns current time
    return time_string

def getHour(): ## Returns current Hour
    hour_string = time.strftime('%H')
    return hour_string

def getMinute(): ## Returns current Minute
    minute_string = time.strftime('%M')
    return minute_string
