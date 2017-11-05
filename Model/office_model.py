from View_Widgets import settings_officehours as office


##########################################################################
## ALLES IS HARTSTIKKE OMSLACHTIG EN KAN NETTER. #########################
##########################################################################
def onEnterScript():
    office.office1.setTooltip("Rollucks will close outside\nthese hours")


def onLeaveScript():
    office.office1.setTooltip("")


closehour = 23
closeminute = 0
openhour = 8
openminute = 0

def increaseOpenTimeScript():
    global openhour
    global openminute
    if openhour == 23 and openminute == 50:
        openhour = 0
        openminute = 0
        time = "{}:{}0".format(openhour,openminute)
    elif openminute == 50:
        openminute = 0
        openhour+=1
        time = "{}:{}0".format(openhour, openminute)
    else:
        openminute+= 10
        time = "{}:{}".format(openhour, openminute)
    office.office1.officeOpenValue.config(text=time)


def decreaseOpenTimeScript():
    global openhour
    global openminute
    if openminute >= 10:
        openminute -= 10
        if openminute == 0:
            time = "{}:{}0".format(openhour, openminute)
        else:
            time = "{}:{}".format(openhour,openminute)
    elif openhour > 0 and openminute == 0:
        openminute = 50
        openhour -= 1
        time = "{}:{}".format(openhour,openminute)
    elif openhour == 0 and openminute == 0:
        openhour = 23
        openminute = 50
        time = "{}:{}".format(openhour, openminute)
    office.office1.officeOpenValue.config(text=time)


def increaseCloseTimeScript():
    global closehour
    global closeminute
    if closehour == 23 and closeminute == 50:
        closehour = 0
        closeminute = 0
        time = "{}:{}0".format(closehour,closeminute)
    elif closeminute == 50:
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
    if closeminute >= 10:
        closeminute -= 10
        if closeminute == 00:
            time = "{}:{}0".format(closehour,closeminute)
        else:
            time = "{}:{}".format(closehour, closeminute)
    elif closehour > 0 and closeminute == 0:
        closehour-=1
        closeminute = 50
        time = "{}:{}".format(closehour,closeminute)
    elif closehour == 0 and closeminute == 0:
        closehour = 23
        closeminute = 50
        time = "{}:{}".format(closehour, closeminute)
    office.office1.officeCloseValue.config(text=time)
