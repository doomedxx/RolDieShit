import Frame.mainframe as f
import Model.theme_model as model
import threading
import time

color = 20
def goDark(event):
    global color
    if color > 15:
        f.root.after(1, darkTransition)

def darkTransition():
    global color
    if color >= 15:
        threading.Timer(0.000001, darkTransition).start()
        f.root.configure(background='gray{}'.format(color))
        color-=1

def goLight(event):
    global color
    if color < 80:
        f.root.after(1, lightTransition)

def lightTransition():
    global color
    if color <= 80:
        threading.Timer(0.000001, lightTransition).start()
        f.root.configure(background='gray{}'.format(color))
        color+=1

def onEnter(event):
    model.onEnterScript()

def onLeave(event):
    model.onLeaveScript()