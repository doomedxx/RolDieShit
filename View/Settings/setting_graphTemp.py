from tkinter import *

import Controller.maxlight_controller as controller
import Frame.mainframe as mainframe
import View.Settings.setting_values as value


class tempGraphSetting(object):

    mainframe.widgetList.append("closetemp")
    def __init__(self):
        self.color = "gray30"
        self.tempGraphSettingPosY = 280
        self.tempGraphSetting = Frame(mainframe.root, relief=SUNKEN)

        self.tempGraphlabel = Label(self.tempGraphSetting)
        self.tempGraphlabel.config(text="Temp Graph \nDetail", font=value.titleFont, bg=self.color, fg=value.titleColor, anchor="c")
        self.tempGraphlabel.pack()
        self.tempGraphlabel.place(width=125, x=10, y=1)


    def setTemp(self, temperature):
        self.maxTemp = temperature
        self.maxValue.config(text=temperature, font=value.informationFont, bg=self.color, fg=value.titleColor)

    def getTemp(self):
        return self.maxtemp

    def addBlock(self):
        self.tempGraphSetting.pack(side=LEFT)
        self.tempGraphSetting.place(height=value.widgetHeight, width=value.widgetWidth, x=375, y=self.tempGraphSettingPosY)
        self.tempGraphSetting.config(bg=self.color,borderwidth= value.borderWidth, relief=value.relief)

    def setTooltip(self, tip):
        self.maxTip.config(text=tip, font=value.tipFont, bg=self.color, fg=value.tipColor)

t1 = tempGraphSetting()