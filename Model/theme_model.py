import threading

import Frame.mainframe as f
from View_Widgets import setting_theme as theme

color = 20

def lightTransition():
    global color
    if color <= 80:
        threading.Timer(0.000001, lightTransition).start()
        f.root.configure(background='gray{}'.format(color))
        color+=3

def darkTransition():
    global color
    if color >= 15:
        threading.Timer(0.000001, darkTransition).start()
        f.root.configure(background='gray{}'.format(color))
        color-=3

def onEnterScript():
    theme.t1.setTooltip("Change the appearance of \n the interface")

def onLeaveScript():
    theme.t1.setTooltip("")