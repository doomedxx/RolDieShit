from tkinter import *

import Frame.mainframe as mainframe
import View_Widgets.widgetValues as value
from Controller import light_controller as controller


class lightWidget(object):
    mainframe.widgetList.append("Light Widget")
    lightWidget = Frame(mainframe.root, relief=SUNKEN)
    lightWidgetPosX = 235
    lightWidgetPosY = 70

    lightLabel = Label(lightWidget, text="LIGHT LEVEL")
    lightLabel.config(font=(value.titlefont), bg="olivedrab", fg=value.titleColor)
    lightLabel.pack()
    lightLabel.place(x=5, y=1)

    lightLabelCount = Label(lightWidget, text="120")
    lightLabelCount.config(font=(value.informationFont), bg="olivedrab", fg=value.indicatorColor,justify=RIGHT)
    lightLabelCount.pack()
    lightLabelCount.place(width= 105,x=25, y=23)

    lightWidget.pack(side=LEFT)
    lightWidget.place(height=value.widgetHeight, width=value.widgetWidth, x=lightWidgetPosX, y=lightWidgetPosY)
    lightWidget.config(bg="olivedrab",borderwidth= value.borderWidth, relief=value.relief)

    tempImage = PhotoImage(file="images/light.png")
    lightIcon = Label(lightWidget, image=tempImage, bg="olivedrab")
    lightIcon.pack()
    lightIcon.place(x=value.widgetWidth -80, y=value.widgetHeight /2 - 30)

def replace():
    l1.lightWidget.place(height=value.widgetHeight, width=value.widgetWidth, x=l1.lightWidgetPosX, y=l1.lightWidgetPosY)

def update():
    controller.update(0.2)
l1 = lightWidget()
#update()