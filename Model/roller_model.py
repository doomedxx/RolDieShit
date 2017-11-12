from View import rollercontrol as view
from tkinter import *
from Frame import mainframe as mainframe
rollucks = {1:"Open", 2:"Closed", 3:"Open"}

#lightInput = light.getLight()
closeLight = 30     #lightClose.getCloseLight()
openLight = 70      #lightOpen.getOpenLight()


def checkTime():
    from Model.Settings import office_model as office
    openTime = office.getOpenTime()
    closeTime = office.getCloseTime()
    if bool(openTime) == True & bool(closeTime) == True:
        checkLight()


def checkLight(): ## Checks the light value and executes a fitting function when a certain threshold is met
    from Model import light_model as light
    from Model.Settings import light_open_model as lightOpen
    from Model.Settings import light_close_model as lightClose
    closeLight = lightClose.getCloseLight()
    openLight = lightOpen.getOpenLight()
    lightInput = light.getLight()

    if lightInput < closeLight:
        autoClose()
    elif lightInput > openLight:
        autoOpen()

def autoOpen():
    print("open")

def autoClose():
    print("dicht")


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
    if rollucks[rolluck] == "Open": ## If the rollucks are open, close it!
        eval("view.r1.rollerLabel" + str(rolluck) + "Status.config" + "(text='Status: in motion')")
        eval("view.r1.rollerStatus" + str(rolluck) + ".config(image=view.r1.motionImage)")
        eval("view.r1.roller" + str(rolluck) + "Toggle.config(state=DISABLED)")
        mainframe.root.after(3000, close, rolluck)

    elif rollucks[rolluck] == "Closed": ## If the rollucks closed, open it!
        eval("view.r1.rollerLabel" + str(rolluck) + "Status.config" + "(text='Status: in motion')")
        eval("view.r1.rollerStatus" + str(rolluck) + ".config(image=view.r1.motionImage)")
        eval("view.r1.roller" + str(rolluck) + "Toggle.config(state=DISABLED)")
        mainframe.root.after(3000, open, rolluck)

def All(toggle):
    ## Function argument receives a ''Close all'' or ''Open All'' signal. Then, depending on the status of the rolluck,
    ## closes or opens it.
    ## The parameters "Open" or "Closed" can be used.
    for k in rollucks.keys():
        v = rollucks[k]
        if v == toggle:
            rollucks[k] = toggle
            rollToggleStart(k)
