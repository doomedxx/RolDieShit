from tkinter import *
import Controller.clock_controller as controller
import Frame.mainframe as mainframe
import View_Settings.settingValues as value

class clocksettingwidget(object):
    mainframe.widgetList.append("clocksetting")
    def __init__(self):
        self.clocksettingwidgetPosX = 655
        self.clocksettingwidgetPosY = 280
        self.tooltip = ""
        self.color = "DodgerBlue4"
        self.clocksettingwidget = Frame(mainframe.root, relief=SUNKEN)
        self.clocksettingwidget.bind("<Enter>", controller.onEnter)
        self.clocksettingwidget.bind("<Leave>", controller.onLeave)

        self.clocksettingLabel = Label(self.clocksettingwidget)
        self.clocksettingLabel.config(text="CLOCK MODE", font=value.titleFont, bg=self.color, fg=value.titleColor)
        self.clocksettingLabel.pack()
        self.clocksettingLabel.place(x=20, y=1)

        self.clocksettingTip = Label(self.clocksettingwidget)
        self.clocksettingTip.config(text=self.tooltip, font=value.tipFont, bg=self.color, fg=value.titleColor)
        self.clocksettingTip.pack()
        self.clocksettingTip.place(x=20, y=28)

        self.clocksettingDark = Button(self.clocksettingwidget)
        self.clocksettingDark.config(text="24-HOUR", font=value.titleFont, bg="DodgerBlue3", fg=value.titleColor, borderwidth= 1, relief="raised")
        self.clocksettingDark.bind("<Button-1>", "nothing")
        self.clocksettingDark.pack()
        self.clocksettingDark.place(x=15, y=value.widgetHeight - 105, width=120)

        self.clocksettingLight = Button(self.clocksettingwidget)
        self.clocksettingLight.config(text="12-HOUR", font=value.titleFont, bg="DodgerBlue3", fg=value.titleColor, borderwidth= 1, relief="raised")
        self.clocksettingLight.bind("<Button-1>", "nothing")
        self.clocksettingLight.pack()
        self.clocksettingLight.place(x=15, y=value.widgetHeight - 55, width=120)

    def addBlock(self):
        self.clocksettingwidget.pack(side=LEFT)
        self.clocksettingwidget.place(height=value.widgetHeight, width=value.widgetWidth, x=25, y=self.clocksettingwidgetPosY)
        self.clocksettingwidget.config(bg=self.color,borderwidth= value.borderWidth, relief=value.relief)

    def setTooltip(self, tip):
        self.clocksettingTip.config(text=tip, font=value.tipFont, bg=self.color, fg=value.tipColor)

c1 = clocksettingwidget()