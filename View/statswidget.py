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


class graphwidget(object):
    graphWidget = Frame(mainframe.root, relief=SUNKEN)
    widgetHeight = 150
    widgetWidth = 300
    totalLight = light.totalLight()
    totalTemp = temp.totalTemp()

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

    graphLabel2 = Label(graphWidget, text="Connected Arduinos")
    graphLabel2.config(font=(value.font,10), bg=value.widgetBackground, fg="white")
    graphLabel2.pack()
    graphLabel2.place(x=10, y=30)

    graphLabelLight = Label(graphWidget, text="Light Unit")
    graphLabelLight.config(font=(value.font, 8), bg=value.widgetBackground, fg="white")
    graphLabelLight.pack()
    graphLabelLight.place(x=10, y=50)

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

    Seperator = Separator(graphWidget,orient=HORIZONTAL)


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

    averagetempvalue = Label(graphWidget, text="{} %".format(totalLight))
    averagetempvalue.config(font=(value.font, 10), bg=value.widgetBackground, fg="white")
    averagetempvalue.pack()
    averagetempvalue.place(x=225, y=50)


def replace(): ## Wanneer er terug word geschakeld van Settings naar View, word de widget opnieuw geplaatst
    g1.graphWidget.place(height=150, width=525, x=330, y=410)

g1 = graphwidget
controller.update()