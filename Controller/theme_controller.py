import Frame.mainframe as f
import Model.Settings.theme_model as model

def goDark(event):
    f.root.after(1, model.darkTransition)

def goLight(event):
    f.root.after(1, model.lightTransition)