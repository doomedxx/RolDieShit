from View.Settings import setting_closelight as max

light = 50

def increaseLight():
    global light
    if light >= 0 and light <= 95:
        max.max1.lightDecrease.config(state='normal')
        setWarning("")
        light+=5
    else:
        setWarning("Highest value \nreached!")
        max.max1.lightIncrement.config(state='disabled')
    max.max1.setlight(light)

def decreaseLight():
    global light
    if light >= 5 and light <= 100:
        setWarning("")
        light-=5
        max.max1.lightIncrement.config(state='normal')
    else:
        setWarning("Lowest value \nreached!")
        max.max1.lightDecrease.config(state='disabled')

    max.max1.setlight(light)


def setWarning(warning):
    max.max1.closelightWarning.config(text=warning)

def onLeaveScript():
    max.max1.setTooltip("")