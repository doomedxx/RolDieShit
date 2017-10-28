import time
from tkinter import *

import Frame.mainframe as mainframe
import View_Widgets.widgetValues as value

class clockwidget(object):
    mainframe.widgetList.append("Clock")
    def __init__(self):
        self.clockWidgetPosX = 655
        self.clockWidgetPosY = 70
        self.clockWidget = Frame(mainframe.root, relief=SUNKEN)

        self.image = PhotoImage(file="images/clock.png")
        self.clockIcon = Label(self.clockWidget, image=self.image, bg="light sky blue")
        self.clockIcon.pack()
        self.clockIcon.place(x=value.widgetWidth -80, y=value.widgetHeight /2 - 30)


        self.clockLabel = Label(self.clockWidget)
        self.clockLabel.config(text="TIME",font=value.titlefont, bg="light sky blue", fg=value.titleColor)
        self.clockLabel.pack()
        self.clockLabel.place(x=5, y=1)

        self.clockLabelDay = Label(self.clockWidget, text="Friday")
        self.clockLabelDay.config(font=("DIN-bold", 14), bg="light sky blue", fg=value.indicatorColor)
        self.clockLabelDay.pack()
        self.clockLabelDay.place(x=8, y=24)

        self.clockLabelTime = Label(self.clockWidget, text="10:35PM")
        self.clockLabelTime.config(font=("DIN-bold", 20), bg="light sky blue", fg=value.indicatorColor)
        self.clockLabelTime.pack()
        self.clockLabelTime.place(x=8, y=48)

        self.clockWidget.pack(side=LEFT)
        self.clockWidget.place(height=value.widgetHeight, width=value.widgetWidth, x=self.clockWidgetPosX, y=self.clockWidgetPosY)
        self.clockWidget.config(bg="light sky blue",borderwidth= value.borderWidth, relief=value.relief)

        self.timeString()
    def timeString(self):
        self.time_day = time.strftime('%A')
        self.time_string = time.strftime('%H:%M:%S')
        self.clockLabelTime.config(text=self.time_string)
        self.clockLabelDay.config(text=self.time_day)
        self.clockLabelTime.after(1000, self.timeString)
def replace():
        c.clockWidget.place(height=value.widgetHeight, width=value.widgetWidth, x=c.clockWidgetPosX, y=c.clockWidgetPosY)


c = clockwidget()