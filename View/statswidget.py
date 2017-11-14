import matplotlib
matplotlib.use("TkAgg")

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure

from tkinter import *
import Frame.mainframe as mainframe
import View.widgetValues as value
from Model import light_model as light
from Model import temp_model as temp
from Controller import light_controller as controller


class graphwidget(object): ## Creates statistics from the current session
    graphWidget = Frame(mainframe.root, relief=SUNKEN)
    widgetHeight = 150
    widgetWidth = 300
    totalLight = light.totalLight()
    totalTemp = temp.totalTemp()
    maxLight = light.maxLight()
    minLight = light.minLight()


    disconnect = PhotoImage(file='images/disconnect.png')
    connect = PhotoImage(file='images/connect.png')

    graphLabel = Label(graphWidget, text="STATISTICS")
    graphLabel.config(font=(value.titlefont), bg=value.widgetBackground, fg=value.titleColor)
    graphLabel.pack()
    graphLabel.place(x=5, y=1)

    graphWidget.pack(side=LEFT)
    graphWidget.place(height=150, width=525, x=330, y=410)
    graphWidget.config(bg=value.widgetBackground,borderwidth= value.borderWidth, relief=value.relief)

    graphLabel1 = Label(graphWidget, text="GRAPH 1")
    graphLabel1.config(font=(value.titlefont), bg=value.widgetBackground, fg="white")
    graphLabel1.pack()
    graphLabel1.place(x=10, y=30)

    graphLabel2 = Label(graphWidget, text="Connected Sensors")
    graphLabel2.config(font=(value.font,10), bg=value.widgetBackground, fg="white")
    graphLabel2.pack()
    graphLabel2.place(x=10, y=30)

    graphLabelLight = Label(graphWidget, text="Light")
    graphLabelLight.config(font=(value.font, 8), bg=value.widgetBackground, fg="white")
    graphLabelLight.pack()
    graphLabelLight.place(x=10, y=50)

    ## Checks if light sensor is connected, and present appropriate image
    if light.getConnection() == True:
        graphLabelCon = Label(graphWidget, image=connect, bg=value.widgetBackground)
        graphLabelCon.pack()
        graphLabelCon.place(x=100, y=50)
    elif light.getConnection() == False:
        graphLabelCon = Label(graphWidget, image=disconnect, bg=value.widgetBackground)
        graphLabelCon.pack()
        graphLabelCon.place(x=100, y=50)

    graphLabelTemp = Label(graphWidget, text="Temperature")
    graphLabelTemp.config(font=(value.font,8), bg=value.widgetBackground,fg="white", anchor="w")
    graphLabelTemp.pack()
    graphLabelTemp.place(x=10,y=80)

    ## Checks if temperature sensor is connected, and present appropriate image
    if temp.getConnection() == True:
        graphLabelCon = Label(graphWidget, image=connect, bg=value.widgetBackground)
        graphLabelCon.pack()
        graphLabelCon.place(x=100, y=75)
    elif temp.getConnection() == False:
        graphLabelCon = Label(graphWidget, image=disconnect, bg=value.widgetBackground)
        graphLabelCon.pack()
        graphLabelCon.place(x=100, y=75)

    graphLabelDistance = Label(graphWidget, text="Distance")
    graphLabelDistance.config(font=(value.font,8), bg=value.widgetBackground,fg="white", anchor="w")
    graphLabelDistance.pack()
    graphLabelDistance.place(x=10,y=110)

    graphLabelCon = Label(graphWidget, image=disconnect, bg=value.widgetBackground)
    graphLabelCon.pack()
    graphLabelCon.place(x=100, y=105)


    averagetemp = Label(graphWidget, text="Avg temp")
    averagetemp.config(font=(value.font, 10), bg=value.widgetBackground, fg="white")
    averagetemp.pack()
    averagetemp.place(x=150, y=30)

    averagetempvalue = Label(graphWidget, text="{} °C".format(totalTemp))
    averagetempvalue.config(font=(value.font, 10), bg=value.widgetBackground, fg="white")
    averagetempvalue.pack()
    averagetempvalue.place(x=150, y=50)


    averagelight = Label(graphWidget, text="Avg light %")
    averagelight.config(font=(value.font, 10), bg=value.widgetBackground, fg="white")
    averagelight.pack()
    averagelight.place(x=225, y=30)

    averagelightvalue = Label(graphWidget, text="{} %".format(totalLight))
    averagelightvalue.config(font=(value.font, 10), bg=value.widgetBackground, fg="white")
    averagelightvalue.pack()
    averagelightvalue.place(x=225, y=50)

    maxlight = Label(graphWidget, text="Max light %")
    maxlight.config(font=(value.font, 10), bg=value.widgetBackground, fg="white")
    maxlight.pack()
    maxlight.place(x=300, y=30)

    maxlightval = Label(graphWidget, text="{}%".format(maxLight))
    maxlightval.config(font=(value.font, 10), bg=value.widgetBackground, fg="white")
    maxlightval.pack()
    maxlightval.place(x=300, y=50)

    minlight = Label(graphWidget, text="Min light %")
    minlight.config(font=(value.font, 10), bg=value.widgetBackground, fg="white")
    minlight.pack()
    minlight.place(x=300, y=70)

    minlightval = Label(graphWidget, text="{}%".format(minLight))
    minlightval.config(font=(value.font, 10), bg=value.widgetBackground, fg="white")
    minlightval.pack()
    minlightval.place(x=300, y=90)

    maxtemp = Label(graphWidget, text="Max temp")
    maxtemp.config(font=(value.font, 10), bg=value.widgetBackground, fg="white")
    maxtemp.pack()
    maxtemp.place(x=375, y=30)

    maxtempval = Label(graphWidget, text="25°C")
    maxtempval.config(font=(value.font, 10), bg=value.widgetBackground, fg="white")
    maxtempval.pack()
    maxtempval.place(x=375, y=50)

    mintemp = Label(graphWidget, text="Min temp")
    mintemp.config(font=(value.font, 10), bg=value.widgetBackground, fg="white")
    mintemp.pack()
    mintemp.place(x=375, y=70)

    mintempval = Label(graphWidget, text="20°C")
    mintempval.config(font=(value.font, 10), bg=value.widgetBackground, fg="white")
    mintempval.pack()
    mintempval.place(x=375, y=90)


def replace(): ## Wanneer er terug word geschakeld van Settings naar View, word de widget opnieuw geplaatst
    g1.graphWidget.place(height=150, width=525, x=330, y=410)

def updatedingen(): ## Updates the values in this statistics
    global totalLight
    global totalTemp
    global maxLight
    global minLight
    global minTemp
    global maxTemp

    totalLight = light.totalLight()
    g1.averagelightvalue.config(text=totalLight)
    maxLight = light.maxLight()
    g1.maxlightval.config(text=maxLight)
    minLight = light.minLight()
    g1.minlightval.config(text=minLight)

    totalTemp = temp.totalTemp()
    g1.averagetempvalue.config(text=totalTemp)
    minTemp = temp.minTemp()
    g1.mintempval.config(text=minTemp)
    maxTemp = temp.maxTemp()
    g1.maxtempval.config(text=maxTemp)
    mainframe.root.after(500, updatedingen)
g1 = graphwidget
controller.update()
updatedingen()