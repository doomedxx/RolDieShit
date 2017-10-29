from View_Settings import officehours as office
from Controller import office_controller
import time

##########################################################################
## ALLES IS HARTSTIKKE OMSLACHTIG EN KAN NETTER. #########################
##########################################################################
def onEnterScript():
    office.office1.setTooltip("Rollucks will close outside\nthese hours")

def onLeaveScript():
    office.office1.setTooltip("")

openhour = 8
openminute = 0

closehour = 17
closeminute = 0

def increaseOpenTimeScript():
    global openhour
    global openminute
    if openminute == 50:
        openminute = 0
        openhour+=1
        time = "{}:{}0".format(openhour,openminute)
    else:
        openminute+= 10
        time = "{}:{}".format(openhour,openminute)
    office.office1.officeOpenValue.config(text=time)

def decreaseOpenTimeScript():
    global openhour
    global openminute
    if openminute == 10:
        openminute = 0
        time = "{}:{}0".format(openhour,openminute)
    elif openminute <= 0:
        openhour-=1
        openminute = 50
        time = "{}:{}".format(openhour,openminute)
    else:
        openminute-= 10
        time = "{}:{}".format(openhour,openminute)

    office.office1.officeOpenValue.config(text=time)

def increaseCloseTimeScript():
    global closehour
    global closeminute
    if closeminute == 50:
        closeminute = 0
        closehour+=1
        time = "{}:{}0".format(closehour,closeminute)
    else:
        closeminute+= 10
        time = "{}:{}".format(closehour,closeminute)
    office.office1.officeCloseValue.config(text=time)

def decreaseCloseTimeScript():
    global closehour
    global closeminute
    if closeminute == 10:
        closeminute = 0
        time = "{}:{}0".format(closehour,closeminute)
    elif closeminute <= 0:
        closehour-=1
        closeminute = 50
        time = "{}:{}".format(closehour,closeminute)
    else:
        closeminute-= 10
        time = "{}:{}".format(closehour,closeminute)
    office.office1.officeCloseValue.config(text=time)
