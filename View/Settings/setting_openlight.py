from tkinter import *

import Controller.maxlight_controller as controller
import Frame.mainframe as mainframe
import View.widgetValues as value


class openlightsetting(object):

    mainframe.widgetList.append("openlight")
    def __init__(self):
        self.maxlight = 50
        self.openlightWidgetPosX = 655
        self.openlightWidgetPosY = 320
        self.openlightWidget = Frame(mainframe.root, relief=SUNKEN)

        self.lightLabel = Label(self.openlightWidget)
        self.lightLabel.config(text="OPENING LIGHT", font=value.settingtitleFont, bg=value.settingsBackground, fg=value.settingtitleColor)
        self.lightLabel.place(x=10, y=1)

        self.lightTip = Label(self.openlightWidget)
        self.lightTip.config(text="", font=value.tipFont, bg=value.settingsBackground, fg=value.settingtitleColor)
        self.lightTip.place(x=2, y=30)

        self.lightValue = Label(self.openlightWidget)
        self.lightValue.config(text=self.maxlight, font=value.settingInformationFont, bg=value.settingsBackground, fg=value.settingtitleColor, anchor="c")
        self.lightValue.place(x=35, y=value.settingHeight - 95, width = 75)

        self.lightIncrement = Button(self.openlightWidget)
        self.lightIncrement.config(text="+", font=("DIN-bold", 13), bg=value.settingButtonColor, fg=value.settingtitleColor, height=-10, width=1)
        self.lightIncrement.place(x=118, y=value.settingHeight - 80)
        self.lightIncrement.bind("<Button-1>", controller.increaselightGo)

        self.lightDecrease = Button(self.openlightWidget)
        self.lightDecrease.config(text="-", font=("DIN-bold", 13), bg=value.settingButtonColor, fg=value.settingtitleColor, height=-10, width=1)
        self.lightDecrease.place(x=12, y=value.settingHeight - 80)
        self.lightDecrease.bind("<Button-1>", controller.decreaselightGo)

        self.lightsettingTip = Label(self.openlightWidget)
        self.lightsettingTip.config(text="At what light level should \nthe rollucks close?", font=value.tipFont, bg=value.tipBackground, fg=value.settingtitleColor, anchor="c")
        self.lightsettingTip.pack()
        self.lightsettingTip.place(x=0, y=value.tipY, width=150)

        self.openlightWarning = Label(self.openlightWidget)
        self.openlightWarning.config(text="",font=("DIN-bold", 8), bg=value.settingsBackground, fg=value.tipColor)
        self.openlightWarning.place(x=38, y=value.settingHeight - 40)

    def addBlock(self):
        self.openlightWidget.pack(side=LEFT)
        self.openlightWidget.place(height=value.settingHeight, width=value.settingWidth, x=200, y=self.openlightWidgetPosY)
        self.openlightWidget.config(bg=value.settingsBackground,borderwidth= value.borderWidth, relief=value.relief)

open1 = openlightsetting()