from tkinter import *

import Frame.mainframe as mainframe
import View.widgetValues as value
from Controller import temp_controller as controller

class tempwidget:
    mainframe.widgetList.append("Temperature")
    tempWidgetPosX = 25
    tempWidgetPosY = 70
    tempWidget = Frame(mainframe.root, relief=SUNKEN)

    image = PhotoImage(file="images/temperature.png")
    tempIcon = Label(tempWidget, image=image, bg="mediumseagreen")
    tempIcon.place(x=value.widgetWidth -80, y=value.widgetHeight /2 - 30)

    tempLabelCount = Label(tempWidget, text="  23C")
    tempLabelCount.config(font=value.informationFont, bg="mediumseagreen", fg=value.indicatorColor)
    tempLabelCount.place(x=0, y=16)

    tempLabel = Label(tempWidget)
    tempLabel.config(text="TEMPERATURE",font=value.titlefont, bg="mediumseagreen", fg=value.titleColor)
    tempLabel.place(x=5, y=1)

    tempWidget.place(height=value.widgetHeight, width=value.widgetWidth, x=tempWidgetPosX, y=tempWidgetPosY)
    tempWidget.config(bg="mediumseagreen",borderwidth= value.borderWidth, relief=value.relief)

def replace(): ## Wanneer er terug word geschakeld van Settings naar View, word de widget opnieuw geplaatst
    t1.tempWidget.place(height=value.widgetHeight, width=value.widgetWidth, x=t1.tempWidgetPosX, y=t1.tempWidgetPosY)

t1 = tempwidget()
controller.update()