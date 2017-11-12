from tkinter import *

from Controller.graphlight_controller import increaselightXGo as increaseX
from Controller.graphlight_controller import increaselightYGo as increaseY
from Controller.graphlight_controller import decreaselightXGo as decreaseX
from Controller.graphlight_controller import decreaselightXGo as decreaseY
import Frame.mainframe as mainframe
import View.widgetValues as value


class lightgraphSetting(object):

    mainframe.widgetList.append("closetemp")
    def __init__(self):
        self.lightGraphSettingPosY = 70
        self.lightGraphSetting = Frame(mainframe.root, relief=SUNKEN)

        self.lightgraphlabel = Label(self.lightGraphSetting)
        self.lightgraphlabel.config(text="Light Graph Detail", font=value.settingtitleFontSmall, bg=value.settingsBackground, fg=value.settingtitleColor, anchor="c")
        self.lightgraphlabel.place(width=150, x=0, y=1)

        self.lightsettingTip = Label(self.lightGraphSetting)
        self.lightsettingTip.config(text="Change Light Graph \nX/Y scales", font=value.tipFont, bg=value.tipBackground, fg=value.settingtitleColor, anchor="c")
        self.lightsettingTip.place(x=0, y=value.tipY, width=150)


        self.lightXValue = Label(self.lightGraphSetting)
        self.lightXValue.config(text="100", font=value.settingInformationFont, bg=value.settingsBackground, fg=value.settingtitleColor, anchor="c")
        self.lightXValue.place(x=35, y=value.settingHeight - 145, width = 75)

        self.lightXIncrement = Button(self.lightGraphSetting)
        self.lightXIncrement.config(text="+", font=("DIN-bold", 13), bg=value.settingButtonColor, fg=value.settingtitleColor, height=-10, width=1)
        self.lightXIncrement.place(x=118, y=value.settingHeight - 130)
        self.lightXIncrement.bind("<Button-1>", increaseX)

        self.lightXDecrease = Button(self.lightGraphSetting)
        self.lightXDecrease.config(text="-", font=("DIN-bold", 13), bg=value.settingButtonColor, fg=value.settingtitleColor, height=-10, width=1)
        self.lightXDecrease.place(x=12, y=value.settingHeight - 130)
        self.lightXDecrease.bind("<Button-1>", decreaseX)

        self.Xlabel = Label(self.lightGraphSetting)
        self.Xlabel.config(text="X-axis", font=value.tipFont, bg=value.settingsBackground, fg=value.settingtitleColor, anchor="c")
        self.Xlabel.place(x=35, y=70, width = 75)

        self.lightYValue = Label(self.lightGraphSetting)
        self.lightYValue.config(text="100", font=value.settingInformationFont, bg=value.settingsBackground, fg=value.settingtitleColor, anchor="c")
        self.lightYValue.place(x=35, y=150, width = 75)

        self.lightYIncrement = Button(self.lightGraphSetting)
        self.lightYIncrement.config(text="+", font=("DIN-bold", 13), bg=value.settingButtonColor, fg=value.settingtitleColor, height=-10, width=1)
        self.lightYIncrement.place(x=118, y=165)
        self.lightYIncrement.bind("<Button-1>", increaseY)

        self.lightYDecrease = Button(self.lightGraphSetting)
        self.lightYDecrease.config(text="-", font=("DIN-bold", 13), bg=value.settingButtonColor, fg=value.settingtitleColor, height=-10, width=1)
        self.lightYDecrease.place(x=12, y=165)
        self.lightYDecrease.bind("<Button-1>", decreaseY)

        self.Ylabel = Label(self.lightGraphSetting)
        self.Ylabel.config(text="Y-axis", font=value.tipFont, bg=value.settingsBackground, fg=value.settingtitleColor, anchor="c")
        self.Ylabel.place(x=35, y=140, width = 75)


    def addBlock(self):
            self.lightGraphSetting.place(height=value.settingHeight, width=value.settingWidth, x=375, y=self.lightGraphSettingPosY)
            self.lightGraphSetting.config(bg=value.settingsBackground,borderwidth= value.borderWidth, relief=value.relief)

l1 = lightgraphSetting()