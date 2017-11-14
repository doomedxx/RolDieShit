from tkinter import *

import Controller.light_open_controller as controller
import Frame.mainframe as mainframe
import View.widgetValues as value


class openlightsetting(object):

    mainframe.widgetList.append("openlight")
    def __init__(self): ## Creates the settings for the light percentage where the rollucks shoul open
        self.maxlight = 30
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
        self.lightValue.place(x=35, y=value.settingHeight - 115, width = 75)

        self.lightIncrement = Button(self.openlightWidget)
        self.lightIncrement.config(text="+", font=("DIN-bold", 13), bg=value.settingButtonColor, fg=value.settingtitleColor, height=-10, width=1)
        self.lightIncrement.place(x=118, y=value.settingHeight - 100)
        self.lightIncrement.bind("<Button-1>", controller.increaselightOpenGo)

        self.lightDecrease = Button(self.openlightWidget)
        self.lightDecrease.config(text="-", font=("DIN-bold", 13), bg=value.settingButtonColor, fg=value.settingtitleColor, height=-10, width=1)
        self.lightDecrease.place(x=12, y=value.settingHeight - 100)
        self.lightDecrease.bind("<Button-1>", controller.decreaselightOpenGo)

        self.lightsettingTip = Label(self.openlightWidget)
        self.lightsettingTip.config(text="At what light level should \nthe rollucks open?", font=value.tipFont, bg=value.tipBackground, fg=value.settingtitleColor, anchor="c")
        self.lightsettingTip.pack()
        self.lightsettingTip.place(x=0, y=value.tipY, width=150)

        self.openlightWarning = Label(self.openlightWidget)
        self.openlightWarning.config(text="",font=("DIN-bold", 8), bg=value.settingsBackground, fg=value.tipColor, anchor="c")
        self.openlightWarning.place(x=0, y=value.settingHeight - 40, width=150)

    def setlight(self, lighterature):
        self.maxlight = lighterature
        self.lightValue.config(text=lighterature, font=value.settingInformationFont, bg=value.settingsBackground, fg=value.settingtitleColor)

    def getlight(self):
        return self.maxlight

    def addBlock(self):
        self.openlightWidget.pack(side=LEFT)
        self.openlightWidget.place(height=value.settingHeight, width=value.settingWidth, x=200, y=self.openlightWidgetPosY)
        self.openlightWidget.config(bg=value.settingsBackground,borderwidth= value.borderWidth, relief=value.relief)

open1 = openlightsetting()