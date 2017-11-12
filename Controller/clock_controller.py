
import Model.clock_model as model

def updateClock():
    model.setTime()

def onEnter(event):
    model.onEnterScript()

def onLeave(event):
    model.onLeaveScript()