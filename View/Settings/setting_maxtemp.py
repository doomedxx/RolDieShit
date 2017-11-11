from tkinter import *

import Controller.maxtemp_controller as controller
import Frame.mainframe as mainframe
import View.Settings.setting_values as value


class closetempsetting(object):

    mainframe.widgetList.append("closetemp")
    def __init__(self):
        self.color = "purple2"
        self.maxtemp = 23
        self.closetempWidgetPosX = 655
        self.closetempWidgetPosY = 70
        self.closetempWidget = Frame(mainframe.root, relief=SUNKEN)

        self.closetempWidget.bind("<Enter>", controller.onEnter)
        self.closetempWidget.bind("<Leave>", controller.onLeave)

        self.maxLabel = Label(self.closetempWidget)
        self.maxLabel.config(text="CLOSING TEMP", font=value.titleFont, bg=self.color, fg=value.titleColor)
        self.maxLabel.place(x=10, y=1)

        self.maxTip = Label(self.closetempWidget)
        self.maxTip.config(text="", font=value.tipFont, bg=self.color, fg=value.titleColor)
        self.maxTip.place(x=2, y=30)

        self.maxValue = Label(self.closetempWidget)
        self.maxValue.config(text=self.maxtemp, font=value.informationFont, bg=self.color, fg=value.titleColor)
        self.maxValue.place(x=35, y=value.widgetHeight - 95)

        self.C = Label(self.closetempWidget)
        self.C.config(text="C", font=value.informationFont, bg=self.color, fg=value.titleColor)
        self.C.place(x=85, y=value.widgetHeight - 95)

        self.maxIncrement = Button(self.closetempWidget)
        self.maxIncrement.config(text="+",font=("DIN-bold", 13), bg="gray25", fg=value.titleColor, height=-10, width=1)
        self.maxIncrement.place(x=118, y=value.widgetHeight - 80)
        self.maxIncrement.bind("<Button-1>", controller.increaseTempGo)

        self.closetempWarning = Label(self.closetempWidget)
        self.closetempWarning.config(text="",font=("DIN-bold", 8), bg=self.color, fg="gold")
        self.closetempWarning.place(x=20, y=value.widgetHeight - 40)

        self.minIncrement = Button(self.closetempWidget)
        self.minIncrement.config(text="-",font=("DIN-bold", 13), bg="gray25", fg=value.titleColor, height=-10, width=1)
        self.minIncrement.place(x=12, y=value.widgetHeight - 80)
        self.minIncrement.bind("<Button-1>", controller.decreaseTempGo)

    def setTemp(self, temperature):
        self.maxTemp = temperature
        self.maxValue.config(text=temperature, font=value.informationFont, bg=self.color, fg=value.titleColor)

    def getTemp(self):
        return self.maxtemp

    def addBlock(self):
        self.closetempWidget.pack(side=LEFT)
        self.closetempWidget.place(height=value.widgetHeight, width=value.widgetWidth, x=200, y=self.closetempWidgetPosY)
        self.closetempWidget.config(bg=self.color,borderwidth= value.borderWidth, relief=value.relief)

    def setTooltip(self, tip):
        self.maxTip.config(text=tip, font=value.tipFont, bg=self.color, fg=value.tipColor)

max1 = closetempsetting()