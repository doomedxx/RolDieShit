from tkinter import *

import Frame.mainframe as mainframe
import View_Settings.settingValues as value
import Controller.mintemp_controller as controller


class opentempsetting(object):
    mainframe.widgetList.append("opentemp")
    def __init__(self):
        self.opentemp = 23
        self.opentempWidgetPosX = 655
        self.opentempWidgetPosY = 280
        self.color = "dark slate blue"
        self.opentempWidget = Frame(mainframe.root, relief=SUNKEN)

        self.openLabel = Label(self.opentempWidget)
        self.openLabel.config(text="OPENING TEMP", font=value.titleFont, bg=self.color, fg=value.titleColor)
        self.openLabel.pack()
        self.openLabel.place(x=10, y=1)

        self.openValue = Label(self.opentempWidget)
        self.openValue.config(text=self.opentemp, font=value.informationFont, bg=self.color, fg=value.titleColor)
        self.openValue.pack()
        self.openValue.place(x=35, y=value.widgetHeight - 95)

        self.C = Label(self.opentempWidget)
        self.C.config(text="C", font=value.informationFont, bg=self.color, fg=value.titleColor)
        self.C.pack()
        self.C.place(x=85, y=value.widgetHeight - 95)

        self.maxIncrement = Button(self.opentempWidget)
        self.maxIncrement.config(text="+",font=("DIN-bold", 13), bg="gray25", fg=value.titleColor, height=-10, width=1)
        self.maxIncrement.pack()
        self.maxIncrement.place(x=118, y=value.widgetHeight - 80)
        self.maxIncrement.bind("<Button-1>", controller.increaseTempGo)

        self.minIncrement = Button(self.opentempWidget)
        self.minIncrement.config(text="-",font=("DIN-bold", 13), bg="gray25", fg=value.titleColor, height=-10, width=1)
        self.minIncrement.pack()
        self.minIncrement.place(x=12, y=value.widgetHeight - 80)
        self.minIncrement.bind("<Button-1>", controller.decreaseTempGo)

    def setTemp(self, temperature):
        print(temperature)
        self.openTemp = temperature
        self.openValue.config(text=temperature, font=value.informationFont, bg=self.color, fg=value.titleColor)

    def getTemp(self):
        return self.opentemp

    def addBlock(self):
        self.opentempWidget.pack(side=LEFT)
        self.opentempWidget.place(height=value.widgetHeight, width=value.widgetWidth, x=200, y=self.opentempWidgetPosY)
        self.opentempWidget.config(bg=self.color,borderwidth= value.borderWidth, relief=value.relief)

open1 = opentempsetting()