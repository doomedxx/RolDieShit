from tkinter import *

import Controller.mintemp_controller as controller
import Frame.mainframe as mainframe
import View.widgetValues as value


class opentempsetting(object):
    mainframe.widgetList.append("opentemp")
    def __init__(self):
        self.opentemp = 27
        self.opentempsettingPosX = 550
        self.opentempsettingPosY = 320
        self.opentempsetting = Frame(mainframe.root, relief=SUNKEN)

        self.openLabel = Label(self.opentempsetting)
        self.openLabel.config(text="OPENING TEMP", font=value.settingtitleFont, bg=value.settingsBackground, fg=value.settingtitleColor)
        self.openLabel.pack()
        self.openLabel.place(x=10, y=1)

        self.openValue = Label(self.opentempsetting)
        self.openValue.config(text=self.opentemp, font=value.settingInformationFont, bg=value.settingsBackground, fg=value.settingtitleColor)
        self.openValue.pack()
        self.openValue.place(x=35, y=value.settingHeight - 95)

        self.C = Label(self.opentempsetting)
        self.C.config(text="C", font=value.settingInformationFont, bg=value.settingsBackground, fg=value.settingtitleColor)
        self.C.pack()
        self.C.place(x=85, y=value.settingHeight - 95)

        self.maxIncrement = Button(self.opentempsetting)
        self.maxIncrement.config(text="+", font=("DIN-bold", 13), bg=value.settingButtonColor, fg="white", height=-10, width=1)
        self.maxIncrement.pack()
        self.maxIncrement.place(x=118, y=value.settingHeight - 80)
        self.maxIncrement.bind("<Button-1>", controller.increaseTempGo)

        self.opentempWarning = Label(self.opentempsetting)
        self.opentempWarning.config(text="",font=("DIN-bold", 8), bg=value.settingsBackground, fg="gold")
        self.opentempWarning.pack()
        self.opentempWarning.place(x=20, y=value.settingHeight - 40)

        self.opentempTip = Label(self.opentempsetting)
        self.opentempTip.config(text="At what temperature \nshould the rollucks open?", font=value.tipFont, bg=value.tipBackground, fg=value.settingtitleColor)
        self.opentempTip.pack()
        self.opentempTip.place(x=0, y=value.tipY, width=150)

        self.minIncrement = Button(self.opentempsetting)
        self.minIncrement.config(text="-", font=("DIN-bold", 13), bg=value.settingButtonColor, fg="white", height=-10, width=1)
        self.minIncrement.pack()
        self.minIncrement.place(x=12, y=value.settingHeight - 80)
        self.minIncrement.bind("<Button-1>", controller.decreaseTempGo)

    def setTemp(self, temperature):
        print(temperature)
        self.openTemp = temperature
        self.openValue.config(text=temperature, font=value.settingInformationFont, bg=value.settingsBackground, fg=value.settingtitleColor)

    def getTemp(self):
        return self.opentemp

    def addBlock(self):
        self.opentempsetting.pack(side=LEFT)
        self.opentempsetting.place(height=value.settingHeight, width=value.settingWidth, x=self.opentempsettingPosX, y=self.opentempsettingPosY)
        self.opentempsetting.config(bg=value.settingsBackground,borderwidth= value.borderWidth, relief=value.relief)

    def setTooltip(self, tip):
        self.opentempTip.config(text=tip, font=value.tipFont, bg=value.settingsBackground, fg=value.tipColor)

min1 = opentempsetting()