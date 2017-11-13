from View.Settings import setting_closelight as close
from View.Settings import setting_openlight as open

light = 30

def increaseLightOpen():
    global light
    from Model.Settings.light_close_model import getLightValue
    if light >= getLightValue()-5:
        setWarning("Keep Open value higher \nthan Close value")
    elif light >= 0 and light <= 95:
        open.open1.lightDecrease.config(state='normal')
        setWarning("")
        light+=5
    else:
        setWarning("Highest value \nreached!")
        open.open1.lightIncrement.config(state='disabled')
    open.open1.setlight(light)

def decreaseLightOpen():
    global light
    if light >= 5 and light <= 100:
        setWarning("")
        light-=5
        open.open1.lightIncrement.config(state='normal')
    else:
        setWarning("Lowest value \nreached!")
        open.open1.lightDecrease.config(state='disabled')

    open.open1.setlight(light)

def setWarning(warning):
    open.open1.openlightWarning.config(text=warning, fg="white")

def getLightValue():
    global light
    return light

def onLeaveScript():
    close.close1.setTooltip("")

def getOpenLight():
    return light
