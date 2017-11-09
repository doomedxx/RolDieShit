import Model.Settings.office_model as model

def onEnter(event):
    model.onEnterScript()

def increaseOpenTime(event):
    model.increaseOpenTimeScript()

def decreaseOpenTime(event):
    model.decreaseOpenTimeScript()

def increaseCloseTime(event):
    model.increaseCloseTimeScript()

def decreaseCloseTime(event):
    model.decreaseCloseTimeScript()



def onLeave(event):
    model.onLeaveScript()