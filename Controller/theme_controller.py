import Frame.mainframe as f
import Model.theme_model as model

def goDark(event):
    f.root.after(1, model.darkTransition)

def goLight(event):
    f.root.after(1, model.lightTransition)

def onEnter(event):
    model.onEnterScript()

def onLeave(event):
    model.onLeaveScript()