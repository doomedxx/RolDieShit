from tkinter import *

import Frame.mainframe as mainframe
import View_Widgets.widgetValues as value


class tempwidget:
    mainframe.widgetList.append("Temperature")
    tempWidgetPosX = 25
    tempWidgetPosY = 70
    tempWidget = Frame(mainframe.root, relief=SUNKEN)

    image = PhotoImage(file="images/temperature.png")
    tempIcon = Label(tempWidget, image=image, bg="mediumseagreen")
    tempIcon.pack()
    tempIcon.place(x=value.widgetWidth -80, y=value.widgetHeight /2 - 30)


    tempLabel = Label(tempWidget)
    tempLabel.config(text="TEMPERATURE",font=value.titlefont, bg="mediumseagreen", fg=value.titleColor)
    tempLabel.pack()
    tempLabel.place(x=5, y=1)

    tempLabelCount = Label(tempWidget, text="  23C")
    tempLabelCount.config(font=value.informationFont, bg="mediumseagreen", fg=value.indicatorColor)
    tempLabelCount.pack()
    tempLabelCount.place(x=0, y=22)

    tempWidget.pack(side=LEFT)
    tempWidget.place(height=value.widgetHeight, width=value.widgetWidth, x=tempWidgetPosX, y=tempWidgetPosY)
    tempWidget.config(bg="mediumseagreen",borderwidth= value.borderWidth, relief=value.relief)

def replace():
    t1.tempWidget.place(height=value.widgetHeight, width=value.widgetWidth, x=t1.tempWidgetPosX, y=t1.tempWidgetPosY)

t1 = tempwidget()