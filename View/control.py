from tkinter import *

import Frame.mainframe as mainframe
from Controller import control_controller as controller
import View.widgetValues as value


class controlwidget(object):
    controlWidgetPosX = 655
    controlWidgetPosY = 70
    color = "RoyalBlue"
    controlWidget = Frame(mainframe.root, relief=SUNKEN)
    controlImage = PhotoImage(file='images/gear.png')
    controlIcon = Label(controlWidget, image=controlImage, bg=color)
    controlIcon.pack()
    controlIcon.place(x=value.widgetWidth -80, y=value.widgetHeight /2 - 30)

    controlLabel = Label(controlWidget, text="CONTROLLER")
    controlLabel.config(font=(value.titlefont), bg=color, fg=value.titleColor)
    controlLabel.pack()
    controlLabel.place(x=5, y=1)
    controlButtonCloseAll = Button(controlWidget, text="CLOSE ALL")
    controlButtonCloseAll.config(font=(value.font, 12), bg=color, fg=value.indicatorColor,borderwidth= 1, relief="raised")
    controlButtonCloseAll.pack()
    controlButtonCloseAll.place(height=20, width=110,x=5, y=30)
    controlButtonCloseAll.bind("<Button-1>",lambda event: controller.All("Open"))

    controlButtonOpenAll = Button(controlWidget, text="OPEN ALL")
    controlButtonOpenAll.config(font=(value.font, 12), bg=color, fg=value.indicatorColor,borderwidth= 1, relief="raised")
    controlButtonOpenAll.pack()
    controlButtonOpenAll.place(height=20, width=110,x=5, y=55)
    controlButtonOpenAll.bind("<Button-1>",lambda event: controller.All("Closed"))

    controlButtonMode = Button(controlWidget, text="AUTOMATIC")
    controlButtonMode.config(font=(value.font, 12), bg=color, fg=value.indicatorColor, borderwidth=1,relief="raised")
    controlButtonMode.pack()
    controlButtonMode.place(height=20, width=110, x=5, y=80)
    controlButtonMode.bind("<Button-1>", controller.Mode)

    controlWidget.pack(side=LEFT)
    controlWidget.place(height=value.widgetHeight, width=value.widgetWidth, x=controlWidgetPosX, y=controlWidgetPosY)
    controlWidget.config(bg=color,borderwidth= value.borderWidth, relief=value.relief)

def replace(): ## Wanneer er terug word geschakeld van Settings naar View, word de widget opnieuw geplaatst
    c1.controlWidget.place(height=value.widgetHeight, width=value.widgetWidth, x=c1.controlWidgetPosX, y=c1.controlWidgetPosY)

c1 = controlwidget()
