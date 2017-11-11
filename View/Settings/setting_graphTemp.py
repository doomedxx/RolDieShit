from tkinter import *

import Controller.light_close_controller as controller
import Frame.mainframe as mainframe
import View.widgetValues as value


class tempGraphSetting(object):

    mainframe.widgetList.append("closetemp")
    def __init__(self):
        self.tempGraphSettingPosY = 320
        self.tempGraphSetting = Frame(mainframe.root, relief=SUNKEN)

        self.tempGraphlabel = Label(self.tempGraphSetting)
        self.tempGraphlabel.config(text="Temp Graph Detail", font=value.settingtitleFontSmall, bg=value.settingsBackground, fg=value.settingtitleColor, anchor="c")
        self.tempGraphlabel.pack()
        self.tempGraphlabel.place(width=150, x=0, y=1)

        self.tempsettingTip = Label(self.tempGraphSetting)
        self.tempsettingTip.config(text="Change Temp Graph \nX/Y scales", font=value.tipFont, bg=value.tipBackground, fg=value.settingtitleColor, anchor="c")
        self.tempsettingTip.place(x=0, y=value.tipY, width=150)

    def setTemp(self, temperature):
        self.maxTemp = temperature
        self.maxValue.config(text=temperature, font=value.settingInformationFont, bg=value.settingsBackground, fg=value.settingtitleColor)

    def getTemp(self):
        return self.maxtemp

    def addBlock(self):
        self.tempGraphSetting.pack(side=LEFT)
        self.tempGraphSetting.place(height=value.settingHeight, width=value.settingWidth, x=375, y=self.tempGraphSettingPosY)
        self.tempGraphSetting.config(bg=value.settingsBackground,borderwidth= value.borderWidth, relief=value.relief)

t1 = tempGraphSetting()