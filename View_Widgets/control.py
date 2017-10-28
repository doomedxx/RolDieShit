from tkinter import *

import Frame.mainframe as mainframe
import View_Widgets.widgetValues as value


class controlwidget(object):
    mainframe.widgetList.append("Control Widget")
    controlWidgetPosX = 445
    controlWidgetPosY = 70
    controlWidget = Frame(mainframe.root, relief=SUNKEN)
    controlImage = PhotoImage(file='images/gear.png')
    controlIcon = Label(controlWidget, image=controlImage, bg="royalblue")
    controlIcon.pack()
    controlIcon.place(x=value.widgetWidth -80, y=value.widgetHeight /2 - 30)

    controlLabel = Label(controlWidget, text="CONTROLLER")
    controlLabel.config(font=(value.titlefont), bg="royalblue", fg=value.titleColor)
    controlLabel.pack()
    controlLabel.place(x=5, y=1)

    controlButtonCloseAll = Button(controlWidget, text="Close all")
    controlButtonCloseAll.config(font=(value.font, 15), bg="royalblue", fg=value.indicatorColor,borderwidth= 1, relief="raised")
    controlButtonCloseAll.pack()
    controlButtonCloseAll.place(height=25, width=100,x=5, y=35)

    controlButtonOpenAll = Button(controlWidget, text="Open all")
    controlButtonOpenAll.config(font=(value.font, 15), bg="royalblue", fg=value.indicatorColor,borderwidth= 1, relief="raised")
    controlButtonOpenAll.pack()
    controlButtonOpenAll.place(height=25, width=100,x=5, y=65)

    controlWidget.pack(side=LEFT)
    controlWidget.place(height=value.widgetHeight, width=value.widgetWidth, x=controlWidgetPosX, y=controlWidgetPosY)
    controlWidget.config(bg="royalblue",borderwidth= value.borderWidth, relief=value.relief)

def replace():
    c1.controlWidget.place(height=value.widgetHeight, width=value.widgetWidth, x=c1.controlWidgetPosX, y=c1.controlWidgetPosY)

c1 = controlwidget()