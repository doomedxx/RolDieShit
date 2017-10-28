from View_Settings import mintemp as min

temp = 27

def increaseTemp():
    global temp
    print(temp)
    if temp >= 18 and temp <= 35:
        setWarning("")
        temp+=1
    else:
        setWarning("Highest temperature \nreached!")
    min.min1.setTemp(temp)

def decreaseTemp():
    global temp
    if temp >= 19 and temp <= 36:
        setWarning("")
        temp-=1
    else:
        setWarning("Lowest temperature \nreached!")
    min.min1.setTemp(temp)

def setWarning(warning):
    min.min1.opentempWarning.config(text=warning)

def onEnterScript():
    min.min1.setTooltip("At what temperature should \n the rollucks open?")

def onLeaveScript():
    min.min1.setTooltip("")