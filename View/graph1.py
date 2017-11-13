import matplotlib
matplotlib.use("TkAgg")

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure

from tkinter import *
import Frame.mainframe as mainframe
import View.widgetValues as value
from Model import light_model as light
from Model import temp_model as temp


class graphwidget(object):
    graphWidget = Frame(mainframe.root, relief=SUNKEN)
    widgetHeight = 150
    widgetWidth = 300
    totalLight = light.totalLight()

    closeImage = PhotoImage(file='images/closed.png')
    openImage = PhotoImage(file='images/open.png')

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

    graphLabelLight = Label(graphWidget, text="Light")
    graphLabelLight.config(font=(value.font, 8), bg=value.widgetBackground, fg="white")
    graphLabelLight.pack()
    graphLabelLight.place(x=10, y=50)

    if light.getConnection() == True:
        graphLabelCon = Label(graphWidget, image=openImage, bg=value.widgetBackground)
        graphLabelCon.pack()
        graphLabelCon.place(x=100, y=50)
    elif light.getConnection() == False:
        graphLabelCon = Label(graphWidget, image=closeImage, bg=value.widgetBackground)
        graphLabelCon.pack()
        graphLabelCon.place(x=100, y=50)

    graphLabelTemp = Label(graphWidget, text="Temperature")
    graphLabelTemp.config(font=(value.font,8), bg=value.widgetBackground,fg="white")
    graphLabelTemp.pack()
    graphLabelTemp.place(x=10,y=70)

    if temp.getConnection() == True:
        graphLabelCon = Label(graphWidget, image=openImage, bg=value.widgetBackground)
        graphLabelCon.pack()
        graphLabelCon.place(x=100, y=70)
    elif temp.getConnection() == False:
        graphLabelCon = Label(graphWidget, image=closeImage, bg=value.widgetBackground)
        graphLabelCon.pack()
        graphLabelCon.place(x=100, y=70)

    averagetemp = Label(graphWidget, text="Average temperature")
    averagetemp.config(font=(value.font, 10), bg=value.widgetBackground, fg="white")
    averagetemp.pack()
    averagetemp.place(x=150, y=30)


    averagelight = Label(graphWidget, text="Average light percentage")
    averagelight.config(font=(value.font, 10), bg=value.widgetBackground, fg="white")
    averagelight.pack()
    averagelight.place(x=300, y=30)

    averagetempvalue = Label(graphWidget, text=totalLight)
    averagetempvalue.config(font=(value.font, 10), bg=value.widgetBackground, fg="white")
    averagetempvalue.pack()
    averagetempvalue.place(x=150, y=70)


def replace(): ## Wanneer er terug word geschakeld van Settings naar View, word de widget opnieuw geplaatst
    g1.graphWidget.place(height=150, width=525, x=330, y=410)

g1 = graphwidget
