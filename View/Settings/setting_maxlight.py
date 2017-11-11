from tkinter import *

import Controller.maxlight_controller as controller
import Frame.mainframe as mainframe
import View.Settings.setting_values as value


class closelightsetting(object):

    mainframe.widgetList.append("closelight")
    def __init__(self):
        self.color = "gray30"
        self.maxlight = 50
        self.closelightWidgetPosX = 655
        self.closelightWidgetPosY = 70
        self.closelightWidget = Frame(mainframe.root, relief=SUNKEN)

        self.closelightWidget.bind("<Enter>", controller.onEnter)
        self.closelightWidget.bind("<Leave>", controller.onLeave)

        self.lightLabel = Label(self.closelightWidget)
        self.lightLabel.config(text="CLOSING LIGHT", font=value.titleFont, bg=self.color, fg=value.titleColor)
        self.lightLabel.place(x=10, y=1)

        self.lightTip = Label(self.closelightWidget)
        self.lightTip.config(text="", font=value.tipFont, bg=self.color, fg=value.titleColor)
        self.lightTip.place(x=2, y=30)

        self.lightValue = Label(self.closelightWidget)
        self.lightValue.config(text=self.maxlight, font=value.informationFont, bg=self.color, fg=value.titleColor, anchor="c")
        self.lightValue.place(x=35, y=value.widgetHeight - 95, width = 75)

        self.lightIncrement = Button(self.closelightWidget)
        self.lightIncrement.config(text="+",font=("DIN-bold", 13), bg="gray40", fg=value.titleColor, height=-10, width=1)
        self.lightIncrement.place(x=118, y=value.widgetHeight - 80)
        self.lightIncrement.bind("<Button-1>", controller.increaselightGo)

        self.closelightWarning = Label(self.closelightWidget)
        self.closelightWarning.config(text="",font=("DIN-bold", 8), bg=self.color, fg=value.tipColor)
        self.closelightWarning.place(x=38, y=value.widgetHeight - 40)

        self.lightDecrease = Button(self.closelightWidget)
        self.lightDecrease.config(text="-",font=("DIN-bold", 13), bg="gray40", fg=value.titleColor, height=-10, width=1)
        self.lightDecrease.place(x=12, y=value.widgetHeight - 80)
        self.lightDecrease.bind("<Button-1>", controller.decreaselightGo)

    def setlight(self, lighterature):
        self.maxlight = lighterature
        self.lightValue.config(text=lighterature, font=value.informationFont, bg=self.color, fg=value.titleColor)

    def getlight(self):
        return self.maxlight

    def addBlock(self):
        self.closelightWidget.pack(side=LEFT)
        self.closelightWidget.place(height=value.widgetHeight, width=value.widgetWidth, x=200, y=self.closelightWidgetPosY)
        self.closelightWidget.config(bg=self.color,borderwidth= value.borderWidth, relief=value.relief)

    def setTooltip(self, tip):
        self.lightTip.config(text=tip, font=value.tipFont, bg=self.color, fg=value.tipColor)

max1 = closelightsetting()