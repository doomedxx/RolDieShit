import threading
from Controller.Module_controller import *
from View import rollercontrol as view
from tkinter import *
from Frame import mainframe as mainframe

rollucks = {1: "Open", 2: "Closed", 3: "Open"}
controller = Modulecontroller()

def close(rollID):
    controller.close_screen()
    eval("view.r1.rollerStatus" + str(rollID) + ".config(image=view.r1.closeImage)")
    eval("view.r1.rollerLabel" + str(rollID) + "Status.config" + "(text='Status: closed')")
    eval("view.r1.roller" + str(rollID) + "Toggle.config(state=NORMAL)")
    rollucks[rollID] = "Closed"
    print("ik sluit")


def open(rollID):
    controller.init_transmit()
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


def All(toggle):
    for k in rollucks.keys():
        v = rollucks[k]
        if v == toggle:
            rollucks[k] = toggle
            rollToggleStart(k)
