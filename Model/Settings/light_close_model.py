from View.Settings import setting_closelight as close
from View.Settings import setting_openlight as open

light = 50

def increaseLightClose():
    global light
    if light >= 0 and light <= 95:
        close.close1.lightDecrease.config(state='normal')
        setWarning("")
        light+=5
    else:
        setWarning("Highest value \nreached!")
        close.close1.lightIncrement.config(state='disabled')
    close.close1.setlight(light)

def decreaseLightClose():
    global light
    if light >= 5 and light <= 100:
        setWarning("")
        light-=5
        close.close1.lightIncrement.config(state='normal')
    else:
        setWarning("Lowest value \nreached!")
        close.close1.lightDecrease.config(state='disabled')

    close.close1.setlight(light)
def setWarning(warning):
    close.close1.closelightWarning.config(text=warning)

def onLeaveScript():
    close.close1.setTooltip("")