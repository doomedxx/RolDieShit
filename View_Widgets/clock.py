import time
from tkinter import *

import Frame.mainframe as mainframe
import View_Widgets.widgetValues as value

class clockwidget(object):
    mainframe.widgetList.append("Clock")
    def __init__(self):
        self.clockWidgetPosX = 445
        self.clockWidgetPosY = 70
        self.color = "royalblue"
        self.clockWidget = Frame(mainframe.root, relief=SUNKEN)

        self.image = PhotoImage(file="images/clock.png")
        self.clockIcon = Label(self.clockWidget, image=self.image, bg=self.color)
        self.clockIcon.pack()
        self.clockIcon.place(x=value.widgetWidth -80, y=value.widgetHeight /2 - 30)

        self.clockLabelTime = Label(self.clockWidget, text="10:35PM")
        self.clockLabelTime.config(font=("DIN-bold", 20), bg=self.color, fg=value.indicatorColor)
        self.clockLabelTime.pack()
        self.clockLabelTime.place(x=2, y=53)

        self.clockLabelDay = Label(self.clockWidget, text="")
        self.clockLabelDay.config(font=("DIN-bold", 20), bg=self.color, fg=value.indicatorColor)
        self.clockLabelDay.pack()
        self.clockLabelDay.place(x=2, y=25)

        self.clockLabel = Label(self.clockWidget)
        self.clockLabel.config(text="TIME",font=value.titlefont, bg=self.color, fg=value.titleColor)
        self.clockLabel.pack()
        self.clockLabel.place(x=2, y=1)

        self.clockWidget.pack(side=LEFT)
        self.clockWidget.place(height=value.widgetHeight, width=value.widgetWidth, x=self.clockWidgetPosX, y=self.clockWidgetPosY)
        self.clockWidget.config(bg=self.color,borderwidth= value.borderWidth, relief=value.relief)

        self.timeString()
    def timeString(self):
        self.time_day = time.strftime('%A')
        self.time_string = time.strftime('%H:%M:%S')
        self.clockLabelTime.config(text=self.time_string)
        self.clockLabelDay.config(text=self.time_day.upper(), bg=self.color, fg=value.indicatorColor)
        self.clockLabelTime.after(1000, self.timeString)
def replace():
        c.clockWidget.place(height=value.widgetHeight, width=value.widgetWidth, x=c.clockWidgetPosX, y=c.clockWidgetPosY)


c = clockwidget()