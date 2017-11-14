from tkinter import *

from Controller.graphtemp_controller import increasetempXGo as increaseX
from Controller.graphtemp_controller import increasetempYGo as increaseY
from Controller.graphtemp_controller import decreasetempXGo as decreaseX
from Controller.graphtemp_controller import decreasetempYGo as decreaseY

import Frame.mainframe as mainframe
import View.widgetValues as value


class tempGraphSetting(object):

    mainframe.widgetList.append("closetemp")
    def __init__(self): ## Creates the settings for changing X/Y axles for the temp graph
        self.tempGraphSettingPosY = 320
        self.tempGraphSetting = Frame(mainframe.root, relief=SUNKEN)

        self.tempGraphlabel = Label(self.tempGraphSetting)
        self.tempGraphlabel.config(text="Temp Graph Detail", font=value.settingtitleFontSmall, bg=value.settingsBackground, fg=value.settingtitleColor, anchor="c")
        self.tempGraphlabel.pack()
        self.tempGraphlabel.place(width=150, x=0, y=1)

        self.tempsettingTip = Label(self.tempGraphSetting)
        self.tempsettingTip.config(text="Change Temp Graph \nX/Y scales", font=value.tipFont, bg=value.tipBackground, fg=value.settingtitleColor, anchor="c")
        self.tempsettingTip.place(x=0, y=value.tipY, width=150)

        self.tempXValue = Label(self.tempGraphSetting)
        self.tempXValue.config(text="100", font=value.settingInformationFont, bg=value.settingsBackground, fg=value.settingtitleColor, anchor="c")
        self.tempXValue.place(x=35, y=value.settingHeight - 145, width = 75)

        self.tempXIncrement = Button(self.tempGraphSetting)
        self.tempXIncrement.config(text="+", font=("DIN-bold", 13), bg=value.settingButtonColor, fg=value.settingtitleColor, height=-10, width=1)
        self.tempXIncrement.place(x=118, y=value.settingHeight - 130)
        self.tempXIncrement.bind("<Button-1>", increaseX)

        self.tempXDecrease = Button(self.tempGraphSetting)
        self.tempXDecrease.config(text="-", font=("DIN-bold", 13), bg=value.settingButtonColor, fg=value.settingtitleColor, height=-10, width=1)
        self.tempXDecrease.place(x=12, y=value.settingHeight - 130)
        self.tempXDecrease.bind("<Button-1>", decreaseX)

        self.Xlabel = Label(self.tempGraphSetting)
        self.Xlabel.config(text="X-axis", font=value.tipFont, bg=value.settingsBackground, fg=value.settingtitleColor, anchor="c")
        self.Xlabel.place(x=35, y=70, width = 75)

        self.tempYValue = Label(self.tempGraphSetting)
        self.tempYValue.config(text="100", font=value.settingInformationFont, bg=value.settingsBackground, fg=value.settingtitleColor, anchor="c")
        self.tempYValue.place(x=35, y=150, width = 75)

        self.tempYIncrement = Button(self.tempGraphSetting)
        self.tempYIncrement.config(text="+", font=("DIN-bold", 13), bg=value.settingButtonColor, fg=value.settingtitleColor, height=-10, width=1)
        self.tempYIncrement.place(x=118, y=165)
        self.tempYIncrement.bind("<Button-1>", increaseY)

        self.tempYDecrease = Button(self.tempGraphSetting)
        self.tempYDecrease.config(text="-", font=("DIN-bold", 13), bg=value.settingButtonColor, fg=value.settingtitleColor, height=-10, width=1)
        self.tempYDecrease.place(x=12, y=165)
        self.tempYDecrease.bind("<Button-1>", decreaseY)

        self.Ylabel = Label(self.tempGraphSetting)
        self.Ylabel.config(text="Y-axis", font=value.tipFont, bg=value.settingsBackground, fg=value.settingtitleColor, anchor="c")
        self.Ylabel.place(x=35, y=140, width = 75)

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