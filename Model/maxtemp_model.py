from View_Settings import maxtemp as max
temp = 23

def increaseTemp():
    global temp
    temp+=1
    max.max1.setTemp(temp)

def decreaseTemp():
    global temp
    temp-=1
    max.max1.setTemp(temp)

def onEnterScript():
    max.max1.setTooltip("At what temperature should \n the rollucks close?")

def onLeaveScript():
    max.max1.setTooltip("")