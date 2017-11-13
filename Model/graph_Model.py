from View import lightgraph as light
from View import graph2 as tempgraph
from View.Settings import setting_graphTemp as tempSetting

def increaselightX():
    pass
def decreaselightX():
    pass
def increaselightY():
    pass
def decreaselightY():
    pass

tempx=100
tempy=50
def increasetempX():
    global tempx
    tempx+=5
    updateValues()

def decreasetempX():
    global tempx
    tempx-=5
    updateValues()

def increasetempY():
    global tempy
    tempy+=5
    updateValues()

def decreasetempY():
    global tempy
    tempy-=5
    updateValues()

def updateValues():
    global tempy
    global tempx
    tempSetting.t1.tempXValue.config(text=str(tempx))
    tempSetting.t1.tempYValue.config(text=str(tempy))