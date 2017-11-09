from tkinter import *

import Controller.mintemp_controller as controller
import Frame.mainframe as mainframe
import View.Settings.setting_values as value


class opentempsetting(object):
    mainframe.widgetList.append("opentemp")
    def __init__(self):
        self.opentemp = 27
        self.opentempsettingPosX = 655
        self.opentempsettingPosY = 280
        self.color = "dark slate blue"
        self.opentempsetting = Frame(mainframe.root, relief=SUNKEN)
        self.opentempsetting.bind("<Enter>", controller.onEnter)
        self.opentempsetting.bind("<Leave>", controller.onLeave)

        self.openLabel = Label(self.opentempsetting)
        self.openLabel.config(text="OPENING TEMP", font=value.titleFont, bg=self.color, fg=value.titleColor)
        self.openLabel.pack()
        self.openLabel.place(x=10, y=1)

        self.openValue = Label(self.opentempsetting)
        self.openValue.config(text=self.opentemp, font=value.informationFont, bg=self.color, fg=value.titleColor)
        self.openValue.pack()
        self.openValue.place(x=35, y=value.widgetHeight - 95)

        self.C = Label(self.opentempsetting)
        self.C.config(text="C", font=value.informationFont, bg=self.color, fg=value.titleColor)
        self.C.pack()
        self.C.place(x=85, y=value.widgetHeight - 95)

        self.maxIncrement = Button(self.opentempsetting)
        self.maxIncrement.config(text="+",font=("DIN-bold", 13), bg="gray25", fg=value.titleColor, height=-10, width=1)
        self.maxIncrement.pack()
        self.maxIncrement.place(x=118, y=value.widgetHeight - 80)
        self.maxIncrement.bind("<Button-1>", controller.increaseTempGo)

        self.opentempWarning = Label(self.opentempsetting)
        self.opentempWarning.config(text="",font=("DIN-bold", 8), bg=self.color, fg="gold")
        self.opentempWarning.pack()
        self.opentempWarning.place(x=20, y=value.widgetHeight - 40)

        self.opentempTip = Label(self.opentempsetting)
        self.opentempTip.config(text="", font=value.tipFont, bg=self.color, fg=value.titleColor)
        self.opentempTip.pack()
        self.opentempTip.place(x=2, y=30)

        self.minIncrement = Button(self.opentempsetting)
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
        self.opentempsetting.pack(side=LEFT)
        self.opentempsetting.place(height=value.widgetHeight, width=value.widgetWidth, x=200, y=self.opentempsettingPosY)
        self.opentempsetting.config(bg=self.color,borderwidth= value.borderWidth, relief=value.relief)

    def setTooltip(self, tip):
        self.opentempTip.config(text=tip, font=value.tipFont, bg=self.color, fg=value.tipColor)

min1 = opentempsetting()