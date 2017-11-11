from tkinter import *

import Controller.office_controller as controller
import Frame.mainframe as mainframe
import View.widgetValues as value


class officehourssetting(object):

    mainframe.widgetList.append("closetemp")
    def __init__(self):

        self.officetemp = 23
        self.officesettingPosX = 655
        self.officesettingPosY = 70
        self.officesetting = Frame(mainframe.root, relief=SUNKEN)

        self.officeOpenValue = Label(self.officesetting)
        self.officeOpenValue.config(text="08:00", font=("DIN", 15), bg=value.settingsBackground, fg=value.settingtitleColor)
        self.officeOpenValue.pack()
        self.officeOpenValue.place(x=47, y=value.settingHeight - 105)

        self.officeOpen = Label(self.officesetting)
        self.officeOpen.config(text="OPEN:", font=value.settingtitleFont, bg=value.settingsBackground, fg=value.settingtitleColor)
        self.officeOpen.pack()
        self.officeOpen.place(x=45, y=value.settingHeight - 125)

        self.incOpen = Button(self.officesetting)
        self.incOpen.config(text="+", font=("DIN-bold", 8), bg=value.settingButtonColor, fg=value.settingtitleColor, height=-50, width=1)
        self.incOpen.pack()
        self.incOpen.place(x=110, y=value.settingHeight - 100)
        self.incOpen.bind("<Button-1>", controller.increaseOpenTime)

        self.decOpen = Button(self.officesetting)
        self.decOpen.config(text="-", font=("DIN-bold", 8), bg=value.settingButtonColor, fg=value.settingtitleColor, height=-50, width=1)
        self.decOpen.pack()
        self.decOpen.place(x=20, y=value.settingHeight - 100)
        self.decOpen.bind("<Button-1>", controller.decreaseOpenTime)

        self.incClose = Button(self.officesetting)
        self.incClose.config(text="+", font=("DIN-bold", 8), bg=value.settingButtonColor, fg=value.settingtitleColor, height=-50, width=1)
        self.incClose.pack()
        self.incClose.place(x=110, y=value.settingHeight - 48)
        self.incClose.bind("<Button-1>", controller.increaseCloseTime)

        self.decClose = Button(self.officesetting)
        self.decClose.config(text="-", font=("DIN-bold", 8), bg=value.settingButtonColor, fg=value.settingtitleColor, height=-50, width=1)
        self.decClose.pack()
        self.decClose.place(x=20, y=value.settingHeight - 48)
        self.decClose.bind("<Button-1>", controller.decreaseCloseTime)

        self.officeCloseValue = Label(self.officesetting)
        self.officeCloseValue.config(text="17:00", font=("DIN", 15), bg=value.settingsBackground, fg=value.settingtitleColor)
        self.officeCloseValue.pack()
        self.officeCloseValue.place(x=47, y=value.settingHeight - 54)

        self.officeClose = Label(self.officesetting)
        self.officeClose.config(text="CLOSE:", font=value.settingtitleFont, bg=value.settingsBackground, fg=value.settingtitleColor)
        self.officeClose.pack()
        self.officeClose.place(x=45, y=value.settingHeight - 78)

        self.officeLabel = Label(self.officesetting)
        self.officeLabel.config(text="OFFICE HOURS", font=value.settingtitleFont, bg=value.settingsBackground, fg=value.settingtitleColor)
        self.officeLabel.pack()
        self.officeLabel.place(x=12, y=1)

        self.officeTip = Label(self.officesetting)
        self.officeTip.config(text="At what light level should \n the rollucks close?", font=value.tipFont, bg=value.tipBackground, fg=value.settingtitleColor, anchor="c")
        self.officeTip.pack()
        self.officeTip.place(x=0, y=value.tipY, width=150)

    def setTemp(self, temperature):
        self.officeTemp = temperature
        self.officeValue.config(text=temperature, font=value.settingInformationFont, bg=value.settingsBackground, fg=value.settingtitleColor)

    def getTemp(self):
        return self.officetemp

    def addBlock(self):
        self.officesetting.pack(side=LEFT)
        self.officesetting.place(height=value.settingHeight, width=value.settingWidth, x=550, y=self.officesettingPosY)
        self.officesetting.config(bg=value.settingsBackground,borderwidth= value.borderWidth, relief=value.relief)

    def setTooltip(self, tip):
        self.officeTip.config(text=tip, font=value.tipFont, bg=value.settingsBackground, fg=value.tipColor)

office1 = officehourssetting()