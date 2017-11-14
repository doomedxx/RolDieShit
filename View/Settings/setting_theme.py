from tkinter import *

import Controller.theme_controller as controller
import Frame.mainframe as mainframe
import View.widgetValues as value


class themewidget(object):
    mainframe.widgetList.append("theme")
    def __init__(self): ## Settings for light/dark theme
        self.themeWidgetPosX = 655
        self.themeWidgetPosY = 70
        self.themeWidget = Frame(mainframe.root, relief=SUNKEN)

        self.themeLabel = Label(self.themeWidget)
        self.themeLabel.config(text="THEME", font=value.settingtitleFont, bg=value.settingsBackground, fg=value.settingtitleColor)
        self.themeLabel.pack()
        self.themeLabel.place(x=40, y=1)

        self.themeTip = Label(self.themeWidget)
        self.themeTip.config(text="Change the appearance \nof the interface", font=value.tipFont, bg=value.tipBackground, fg=value.settingtitleColor, anchor="c")
        self.themeTip.place(x=0, y=value.tipY, width=150)

        self.themeDark = Button(self.themeWidget)
        self.themeDark.config(text="Dark Theme", font=value.settingtitleFont, bg=value.settingButtonColor, fg=value.settingtitleColor, borderwidth= 1, relief="raised")
        self.themeDark.bind("<Button-1>", controller.goDark)
        self.themeDark.pack()
        self.themeDark.place(x=15, y=value.settingHeight - 105, width=120)

        self.themeLight = Button(self.themeWidget)
        self.themeLight.config(text="Light Theme", font=value.settingtitleFont, bg=value.settingButtonColor, fg=value.settingtitleColor, borderwidth= 1, relief="raised")
        self.themeLight.bind("<Button-1>", controller.goLight)
        self.themeLight.pack()
        self.themeLight.place(x=15, y=value.settingHeight - 55, width=120)

    def addBlock(self):
        self.themeWidget.pack(side=LEFT)
        self.themeWidget.place(height=value.settingHeight, width=value.settingWidth, x=25, y=self.themeWidgetPosY)
        self.themeWidget.config(bg=value.settingsBackground,borderwidth= value.borderWidth, relief=value.relief)


t1 = themewidget()