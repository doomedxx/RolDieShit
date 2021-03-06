import time
from tkinter import *
import tkinter as tk
import Frame.mainframe as mainframe
import View.widgetValues as value
from Controller.clock_controller import updateClock as clock

class clockwidget(tk.Tk):
    mainframe.widgetList.append("Clock")
    def __init__(self): ## Create clock on view
        self.clockWidgetPosX = 445
        self.clockWidgetPosY = 70
        self.color = "royalblue3"
        self.clockWidget = Frame(mainframe.root, relief=SUNKEN)

        self.image = PhotoImage(file="images/clock.png")
        self.clockIcon = Label(self.clockWidget, image=self.image, bg=self.color)
        self.clockIcon.pack()
        self.clockIcon.place(x=value.widgetWidth -80, y=value.widgetHeight /2 - 30)

        self.clockLabelTime = Label(self.clockWidget)
        self.clockLabelTime.config(font=("DIN-bold", 20), bg=self.color, fg=value.indicatorColor)
        self.clockLabelTime.pack()
        self.clockLabelTime.place(x=2, y=53)

        self.clockLabelDay = Label(self.clockWidget, text="LOADING")
        self.clockLabelDay.config(font=("DIN-bold", 14), bg=self.color, fg=value.indicatorColor,anchor="w")
        self.clockLabelDay.pack()
        self.clockLabelDay.place(width=105,x=2, y=33)

        self.clockLabel = Label(self.clockWidget)
        self.clockLabel.config(text="TIME",font=value.titlefont, bg=self.color, fg=value.titleColor)
        self.clockLabel.pack()
        self.clockLabel.place(x=2, y=1)

        self.clockWidget.pack(side=LEFT)
        self.clockWidget.place(height=value.widgetHeight, width=value.widgetWidth, x=self.clockWidgetPosX, y=self.clockWidgetPosY)
        self.clockWidget.config(bg=self.color,borderwidth= value.borderWidth, relief=value.relief)

def replace():
        c.clockWidget.place(height=value.widgetHeight, width=value.widgetWidth, x=c.clockWidgetPosX, y=c.clockWidgetPosY)


c = clockwidget()
clock()