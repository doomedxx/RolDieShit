from tkinter import *

import Frame.mainframe as mainframe
import View.widgetValues as value


class clocksettingwidget(object):
    mainframe.widgetList.append("clocksetting")
    def __init__(self): ## Creates the settings for 12/24 hour clock
        self.clocksettingwidgetPosX = 655
        self.clocksettingwidgetPosY = 320
        self.clocksettingwidget = Frame(mainframe.root, relief=SUNKEN)

        self.clocksettingLabel = Label(self.clocksettingwidget)
        self.clocksettingLabel.config(text="CLOCK MODE", font=value.settingtitleFont, bg=value.settingsBackground, fg=value.settingtitleColor)
        self.clocksettingLabel.place(x=20, y=1)

        self.clocksettingTip = Label(self.clocksettingwidget)
        self.clocksettingTip.config(text="Werkt niet, hi-ha-ho \ntry again later!", font=value.tipFont, bg=value.tipBackground, fg=value.settingtitleColor, anchor="c")
        self.clocksettingTip.place(x=0, y=value.tipY, width=150)

        self.clocksettingDark = Button(self.clocksettingwidget)
        self.clocksettingDark.config(text="24-HOUR", font=value.settingtitleFont, bg=value.settingButtonColor, fg=value.settingtitleColor, borderwidth= 1, relief="raised")
        self.clocksettingDark.bind("<Button-1>", "nothing")
        self.clocksettingDark.place(x=15, y=value.settingHeight - 105, width=120)

        self.clocksettingLight = Button(self.clocksettingwidget)
        self.clocksettingLight.config(text="12-HOUR", font=value.settingtitleFont, bg=value.settingButtonColor, fg=value.settingtitleColor, borderwidth= 1, relief="raised")
        self.clocksettingLight.bind("<Button-1>", "nothing")
        self.clocksettingLight.place(x=15, y=value.settingHeight - 55, width=120)


    def addBlock(self):
        self.clocksettingwidget.pack(side=LEFT)
        self.clocksettingwidget.place(height=value.settingHeight, width=value.settingWidth, x=25, y=self.clocksettingwidgetPosY)
        self.clocksettingwidget.config(bg=value.settingsBackground,borderwidth= value.borderWidth, relief=value.relief)

c1 = clocksettingwidget()