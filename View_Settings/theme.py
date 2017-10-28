from tkinter import *

import Controller.theme_controller as controller
import Frame.mainframe as mainframe
import View_Settings.settingValues as value



class themewidget(object):
    mainframe.widgetList.append("theme")
    def __init__(self):
        self.themeWidgetPosX = 655
        self.themeWidgetPosY = 70
        self.tooltip = ""
        self.themeWidget = Frame(mainframe.root, relief=SUNKEN)
        self.themeWidget.bind("<Enter>", controller.onEnter)
        self.themeWidget.bind("<Leave>", controller.onLeave)

        self.themeLabel = Label(self.themeWidget)
        self.themeLabel.config(text="THEME", font=value.titleFont, bg="royalblue", fg=value.titleColor)
        self.themeLabel.pack()
        self.themeLabel.place(x=40, y=1)

        self.themeTip = Label(self.themeWidget)
        self.themeTip.config(text=self.tooltip, font=value.tipFont, bg="royalblue", fg=value.titleColor)
        self.themeTip.pack()
        self.themeTip.place(x=5, y=28)

        self.themeDark = Button(self.themeWidget)
        self.themeDark.config(text="Dark Theme", font=value.titleFont, bg="gray25", fg=value.titleColor, borderwidth= 1, relief="raised")
        self.themeDark.bind("<Button-1>", controller.goDark)
        self.themeDark.pack()
        self.themeDark.place(x=15, y=value.widgetHeight - 105, width=120)

        self.themeLight = Button(self.themeWidget)
        self.themeLight.config(text="Light Theme", font=value.titleFont, bg="gray25", fg=value.titleColor, borderwidth= 1, relief="raised")
        self.themeLight.bind("<Button-1>", controller.goLight)
        self.themeLight.pack()
        self.themeLight.place(x=15, y=value.widgetHeight - 55, width=120)

    def addBlock(self):
        self.themeWidget.pack(side=LEFT)
        self.themeWidget.place(height=value.widgetHeight, width=value.widgetWidth, x=25, y=self.themeWidgetPosY)
        self.themeWidget.config(bg="royalblue",borderwidth= value.borderWidth, relief=value.relief)

    def setTooltip(self, tip):
        self.themeTip.config(text=tip, font=value.tipFont, bg="royalblue", fg=value.tipColor)

t1 = themewidget()