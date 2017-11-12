from tkinter import *

import Controller.light_close_controller as controller
import Frame.mainframe as mainframe
import View.widgetValues as value


class closelightsetting(object):

    mainframe.widgetList.append("closelight")
    def __init__(self):
        self.maxlight = 70
        self.closelightWidgetPosX = 655
        self.closelightWidgetPosY = 70
        self.closelightWidget = Frame(mainframe.root, relief=SUNKEN)

        self.lightLabel = Label(self.closelightWidget)
        self.lightLabel.config(text="CLOSING LIGHT", font=value.settingtitleFont, bg=value.settingsBackground, fg=value.settingtitleColor)
        self.lightLabel.place(x=10, y=1)

        self.lightTip = Label(self.closelightWidget)
        self.lightTip.config(text="", font=value.tipFont, bg=value.settingsBackground, fg=value.settingtitleColor)
        self.lightTip.place(x=2, y=30)

        self.lightValue = Label(self.closelightWidget)
        self.lightValue.config(text=self.maxlight, font=value.settingInformationFont, bg=value.settingsBackground, fg=value.settingtitleColor, anchor="c")
        self.lightValue.place(x=35, y=value.settingHeight - 95, width = 75)

        self.lightIncrement = Button(self.closelightWidget)
        self.lightIncrement.config(text="+", font=("DIN-bold", 13), bg=value.settingButtonColor, fg=value.settingtitleColor, height=-10, width=1)
        self.lightIncrement.place(x=118, y=value.settingHeight - 80)
        self.lightIncrement.bind("<Button-1>", controller.increaselightCloseGo)

        self.lightDecrease = Button(self.closelightWidget)
        self.lightDecrease.config(text="-", font=("DIN-bold", 13), bg=value.settingButtonColor, fg=value.settingtitleColor, height=-10, width=1)
        self.lightDecrease.place(x=12, y=value.settingHeight - 80)
        self.lightDecrease.bind("<Button-1>", controller.decreaselightCloseGo)

        self.lightsettingTip = Label(self.closelightWidget)
        self.lightsettingTip.config(text="At what light level should \nthe rollucks close?", font=value.tipFont, bg=value.tipBackground, fg=value.settingtitleColor, anchor="c")
        self.lightsettingTip.pack()
        self.lightsettingTip.place(x=0, y=value.tipY, width=150)

        self.closelightWarning = Label(self.closelightWidget)
        self.closelightWarning.config(text="",font=("DIN-bold", 8), bg=value.settingsBackground, fg=value.tipColor, anchor="c")
        self.closelightWarning.place(x=0, y=value.settingHeight - 40, width=150)

    def setlight(self, lighterature):
        self.maxlight = lighterature
        self.lightValue.config(text=lighterature, font=value.settingInformationFont, bg=value.settingsBackground, fg=value.settingtitleColor)

    def getlight(self):
        return self.maxlight

    def addBlock(self):
        self.closelightWidget.pack(side=LEFT)
        self.closelightWidget.place(height=value.settingHeight, width=value.settingWidth, x=200, y=self.closelightWidgetPosY)
        self.closelightWidget.config(bg=value.settingsBackground,borderwidth= value.borderWidth, relief=value.relief)

    def setTooltip(self, tip):
        self.lightTip.config(text=tip, font=value.tipFont, bg=value.settingsBackground, fg=value.tipColor)

close1 = closelightsetting()