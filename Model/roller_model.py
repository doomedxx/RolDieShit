from View_Widgets import rollercontrol as view
from tkinter import *
from time import sleep
import threading
rollucks = {1:"Open", 2:"Closed", 3:"Open"}

def close(rollID):
    eval("view.r1.rollerStatus" + str(rollID) + ".config(image=view.r1.closeImage)")
    eval("view.r1.rollerLabel" + str(rollID) + "Status.config" + "(text='Status: closed')")
    eval("view.r1.roller" + str(rollID) + "Toggle.config(state=NORMAL)")
    rollucks[rollID] = "Closed"

def open(rollID):
    eval("view.r1.rollerLabel" + str(rollID) + "Status.config" + "(text='Status: Open')")
    eval("view.r1.rollerStatus" + str(rollID) + ".config(image=view.r1.openImage)")
    eval("view.r1.roller" + str(rollID) + "Toggle.config(state=NORMAL)")
    rollucks[rollID] = "Open"

def rollToggleStart(rolluck):
    if rollucks[rolluck] == "Open":
        eval("view.r1.rollerLabel" + str(rolluck) + "Status.config" + "(text='Status: in motion')")
        eval("view.r1.rollerStatus" + str(rolluck) + ".config(image=view.r1.motionImage)")
        eval("view.r1.roller" + str(rolluck) + "Toggle.config(state=DISABLED)")
        threading.Timer(3, close, [rolluck]).start()

    elif rollucks[rolluck] == "Closed":
        eval("view.r1.rollerLabel" + str(rolluck) + "Status.config" + "(text='Status: in motion')")
        eval("view.r1.rollerStatus" + str(rolluck) + ".config(image=view.r1.motionImage)")
        eval("view.r1.roller" + str(rolluck) + "Toggle.config(state=DISABLED)")
        threading.Timer(3, open, [rolluck]).start()

def openAll():
    for k in rollucks.keys():
        rollucks[k] = "Closed"
        rollToggleStart(k)

def closeAll():
    for k in rollucks.keys():
        rollucks[k] = "Open"
        rollToggleStart(k)