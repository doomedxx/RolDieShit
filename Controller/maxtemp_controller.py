import Model.Settings.maxtemp_model as model
def increaseTempGo(event):
    model.increaseTemp()

def decreaseTempGo(event):
    model.decreaseTemp()

def onEnter(event):
    model.onEnterScript()

def onLeave(event):
    model.onLeaveScript()