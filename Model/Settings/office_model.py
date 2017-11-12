from View.Settings import settings_officehours as office


##########################################################################
## ALLES IS HARTSTIKKE OMSLACHTIG EN KAN NETTER. #########################
##########################################################################
def onEnterScript():
    office.office1.setTooltip("Rollucks will close \noutside these hours")


def onLeaveScript():
    office.office1.setTooltip("")


closehour = 17
closeminute = 0
openhour = 8
openminute = 0

def increaseOpenTimeScript():
    global openhour
    global openminute
    if openhour == 23 and openminute == 30:
        openhour = 0
        openminute = 0
        time = "{}:{}0".format(openhour,openminute)
    elif openminute == 30:
        openminute = 0
        openhour+=1
        time = "{}:{}0".format(openhour, openminute)
    else:
        openminute+= 30
        time = "{}:{}".format(openhour, openminute)
    office.office1.officeOpenValue.config(text=time)


def decreaseOpenTimeScript():
    global openhour
    global openminute
    if openminute >= 30:
        openminute -= 30
        if openminute == 0:
            time = "{}:{}0".format(openhour, openminute)
        else:
            time = "{}:{}".format(openhour,openminute)
    elif openhour > 0 and openminute == 0:
        openminute = 30
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
    if closehour == 23 and closeminute == 30:
        closehour = 0
        closeminute = 0
        time = "{}:{}0".format(closehour,closeminute)
    elif closeminute == 30:
        closeminute = 0
        closehour+=1
        time = "{}:{}0".format(closehour,closeminute)
    else:
        closeminute+= 30
        time = "{}:{}".format(closehour,closeminute)
    office.office1.officeCloseValue.config(text=time)


def decreaseCloseTimeScript():
    global closehour
    global closeminute
    if closeminute >= 30:
        closeminute -= 30
        if closeminute == 00:
            time = "{}:{}0".format(closehour,closeminute)
        else:
            time = "{}:{}".format(closehour, closeminute)
    elif closehour > 0 and closeminute == 0:
        closehour-=1
        closeminute = 30
        time = "{}:{}".format(closehour,closeminute)
    elif closehour == 0 and closeminute == 0:
        closehour = 23
        closeminute = 30
        time = "{}:{}".format(closehour, closeminute)
    office.office1.officeCloseValue.config(text=time)

def getOpenTime():
    from Model import clock_model as clock
    hour = int(clock.getHour())
    minute = int(clock.getMinute())
    if hour >= openhour:
        if hour <= closehour:
            if openminute == 0:
                if hour >= openhour & minute >= openminute:
                    return True
            elif openminute == 30:
                    if hour > openhour:
                        return True
                    elif hour == openhour:
                        if minute >= openminute:
                            return True


def getCloseTime():
    from Model import clock_model as clock
    hour = int(clock.getHour())
    minute = int(clock.getMinute())
    if closeminute == 0:
        if hour < closehour:
            return True
        elif hour == closehour:
            if minute <= closeminute:
                return True
    if closeminute == 30:
        if hour < closehour:
            return True
        elif hour == closehour:
            if minute <= closeminute:
              return True
