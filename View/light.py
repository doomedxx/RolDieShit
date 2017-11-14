from tkinter import *

import Frame.mainframe as mainframe
import View.widgetValues as value
from Controller import light_controller as controller


class lightWidget(object): ## Block to present the current light percentage
    mainframe.widgetList.append("Light Widget")
    lightWidget = Frame(mainframe.root, relief=SUNKEN)
    lightWidgetPosX = 235
    lightWidgetPosY = 70


    lightLabelCount = Label(lightWidget, text="50")
    lightLabelCount.config(font=(value.informationFont), bg="olivedrab", fg=value.indicatorColor,justify=RIGHT)
    lightLabelCount.place(width= 105,x=14, y=16)

    lightLabelPreset = Label(lightWidget, text="(Preset here)")
    lightLabelPreset.config(font=(value.informationInfoFont ), bg="olivedrab", fg=value.indicatorColor,anchor="c")
    lightLabelPreset.place(width= 105,x=25, y=77)

    lightWidget.pack(side=LEFT)
    lightWidget.place(height=value.widgetHeight, width=value.widgetWidth, x=lightWidgetPosX, y=lightWidgetPosY)
    lightWidget.config(bg="olivedrab",borderwidth= value.borderWidth, relief=value.relief)

    lightLabel = Label(lightWidget, text="LIGHT LEVEL")
    lightLabel.config(font=(value.titlefont), bg="olivedrab", fg=value.titleColor)
    lightLabel.place(x=5, y=1)

    tempImage = PhotoImage(file="images/light.png")
    lightIcon = Label(lightWidget, image=tempImage, bg="olivedrab")
    lightIcon.pack()
    lightIcon.place(x=value.widgetWidth -80, y=value.widgetHeight /2 - 30)

def replace(): ## Wanneer er terug word geschakeld van Settings naar View, word de widget opnieuw geplaatst
    l1.lightWidget.place(height=value.widgetHeight, width=value.widgetWidth, x=l1.lightWidgetPosX, y=l1.lightWidgetPosY)

l1 = lightWidget()
controller.update()
