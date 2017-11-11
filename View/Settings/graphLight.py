from tkinter import *

import Controller.maxtemp_controller as controller
import Frame.mainframe as mainframe
import View.Settings.setting_values as value


class lightgraphSetting(object):

    mainframe.widgetList.append("closetemp")
    def __init__(self):
        self.color = "chocolate"
        self.lightGraphSettingPosY = 70
        self.lightGraphSetting = Frame(mainframe.root, relief=SUNKEN)

        self.lightgraphlabel = Label(self.lightGraphSetting)
        self.lightgraphlabel.config(text="Light Graph \nDetail", font=value.titleFont, bg=self.color, fg=value.titleColor, anchor="c")
        self.lightgraphlabel.pack()
        self.lightgraphlabel.place(width=125, x=10, y=1)


    def setTemp(self, temperature):
        self.maxTemp = temperature
        self.maxValue.config(text=temperature, font=value.informationFont, bg=self.color, fg=value.titleColor)

    def getTemp(self):
        return self.maxtemp

    def addBlock(self):
        self.lightGraphSetting.pack(side=LEFT)
        self.lightGraphSetting.place(height=value.widgetHeight, width=value.widgetWidth, x=550, y=self.lightGraphSettingPosY)
        self.lightGraphSetting.config(bg=self.color,borderwidth= value.borderWidth, relief=value.relief)

    def setTooltip(self, tip):
        self.maxTip.config(text=tip, font=value.tipFont, bg=self.color, fg=value.tipColor)

l1 = lightgraphSetting()