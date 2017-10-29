from View_Settings import maxtemp as max
temp = 23

def increaseTemp():
    global temp
    if temp >= 14 and temp <= 35:
        setWarning("")
        temp+=1
    else:
        setWarning("Highest temperature \nreached!")
    max.max1.setTemp(temp)

def decreaseTemp():
    global temp
    if temp >= 15 and temp <= 36:
        setWarning("")
        temp-=1
    else:
        setWarning("Lowest temperature \nreached!")


    max.max1.setTemp(temp)

def setWarning(warning):
    max.max1.closetempWarning.config(text=warning)

def onEnterScript():
    max.max1.setTooltip("At what temperature should \n the rollucks close?")

def onLeaveScript():
    max.max1.setTooltip("")