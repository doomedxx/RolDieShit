from View.Settings import setting_closelight as close
from View.Settings import setting_openlight as open

light = 70

def increaseLightClose(): ## Increases the value of when the rollucks should close depening on Light value
    global light
    if light >= 0 and light <= 95:
        close.close1.lightDecrease.config(state='normal')
        setWarning("")
        light+=5
    else:
        setWarning("Highest value \nreached!")
        close.close1.lightIncrement.config(state='disabled')
    close.close1.setlight(light)

def decreaseLightClose(): # Decreases the value of when the rollucks should close depening on Light value
    global light
    from Model.Settings.light_open_model import getLightValue as getCloseValue
    if light <= getCloseValue()+5:
        setWarning("Keep Close Value higher \nthan Opening Value")
    elif light >= 5 and light <= 100:
        setWarning("")
        light-=5
        close.close1.lightIncrement.config(state='normal')
    else:
        setWarning("Lowest value \nreached!")
        close.close1.lightDecrease.config(state='disabled')

    close.close1.setlight(light)

def getLightValue():
    global light
    return light

def setWarning(warning): # Display error message when the light value is above 100%
    close.close1.closelightWarning.config(text=warning, fg="white")

def onLeaveScript():
    close.close1.setTooltip("")

def getCloseLight():
    return light
