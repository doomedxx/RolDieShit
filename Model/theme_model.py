from View_Settings import theme as theme

def onEnterScript():
    print("Werkt")
    theme.t1.setTooltip("Change the appearance of \n the interface")

def onLeaveScript():
    theme.t1.setTooltip("")