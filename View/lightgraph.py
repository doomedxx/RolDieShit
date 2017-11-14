import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
import matplotlib.pyplot as plt
from Controller import graphlight_controller as controller

from tkinter import *

import Frame.mainframe as mainframe
import View.widgetValues as value


class graphwidget3(object): ## Creates the graph for the light values
    graphWidget3 = Frame(mainframe.root, relief=SUNKEN)
    graphWidget3Tool = Frame(mainframe.root, relief=SUNKEN)
    f = plt.figure(figsize=(10,4), dpi=85, facecolor='#65686d', edgecolor="white")
    ax = f.add_subplot(1,1,1)
    x = [0]
    y = [0]
    line, = ax.plot(x,y, 'green')
    line2, = ax.plot(x,y, 'gray')

    plt.ylim(0,100)
    plt.xlim(0,100)
    plt.draw()

    canvas = FigureCanvasTkAgg(f, graphWidget3)
    canvas.get_tk_widget().pack(expand=True)
    canvas.get_tk_widget().configure(background='black')

    graphWidget3.place(height=220, width=525, x=330, y=180)
    graphWidget3.config(bg=value.widgetBackground,borderwidth= value.borderWidth, relief=value.relief)


    graphWidget3Tool.config(bg=value.widgetBackground,borderwidth= value.borderWidth, relief=value.relief)
    graphWidget3Tool.bind("<Enter>", controller.getTools)

    graphWidget3.bind("<Enter>", controller.getTools)
    graphWidget3.bind("<Leave>", controller.releaseTools)

    toolbar = NavigationToolbar2TkAgg(canvas, graphWidget3Tool)
    toolbar.update()

    graphlabel31 = Label(graphWidget3, text="LIGHT LEVELS")
    graphlabel31.config(font=(value.titlefont), bg="#65686d", fg="white")
    graphlabel31.place(x=60, y=-2)

    graphAverage = Label(graphWidget3, text="Grey = Light Average   |   Green = Light Value")
    graphAverage.config(font=(value.informationInfoFont), bg="#65686d", fg="grey85")
    graphAverage.place(x=250, y=2)

def replace(): ## Wanneer er terug word geschakeld van Settings naar View, word de widget opnieuw geplaatst
    g3.graphWidget3.place(height=220, width=525, x=330, y=180)

def update(xSet):
    plt.xlim(0,xSet)

g3 = graphwidget3()
update