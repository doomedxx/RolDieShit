from View.Settings import setting_mintemp as min

temp = 27

def increaseTemp():
    global temp
    if temp >= 14 and temp <= 35:
        setWarning("")
        temp+=1
        min.min1.minIncrement.config(state='normal')
    else:
        setWarning("Highest temperature \nreached!")
        min.min1.maxIncrement.config(state='disabled')
    min.min1.setTemp(temp)

def decreaseTemp():
    global temp
    if temp >= 15 and temp <= 36:
        setWarning("")
        min.min1.maxIncrement.config(state='normal')
        temp-=1
    else:
        setWarning("Lowest temperature \nreached!")
        min.min1.minIncrement.config(state='disabled')
    min.min1.setTemp(temp)

def setWarning(warning):
    min.min1.opentempWarning.config(text=warning)

def getMinTemp():
    return temp
