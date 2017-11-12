
import Model.clock_model as model

def updateClock():
    model.updateClock()
    print("Ik werk")

def onEnter(event):
    model.onEnterScript()

def onLeave(event):
    model.onLeaveScript()

def go12(event):
    model.go12