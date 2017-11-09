import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
from Controller import graphcontroller as controller
import matplotlib.pyplot as plt
import numpy as np

from tkinter import *

import Frame.mainframe as mainframe
import View.widgetValues as value


class graphwidget3(object):
    graphWidget3 = Frame(mainframe.root, relief=SUNKEN)
    graphWidget3Tool = Frame(mainframe.root, relief=SUNKEN)

    f = Figure(figsize=(10,90), dpi=100, facecolor='#65686d', edgecolor="white")
    a = f.add_subplot(111)
    x = [0,1,2,3,4,5,6,7,8,9,10]
    y = [0,10,20,30,40,50,60,70,80,90,100]
    line, = a.plot(x,y, 'green')
    line2, = a.plot(x,y, 'gray')

    canvas = FigureCanvasTkAgg(f, graphWidget3)
    canvas.get_tk_widget().pack(expand=True)
    canvas.get_tk_widget().configure(background='black')

    graphWidget3.place(height=220, width=525, x=330, y=180)
    graphWidget3.config(bg=value.widgetBackground,borderwidth= value.borderWidth, relief=value.relief)
    graphWidget3.bind("<Enter>", controller.getTools)
    graphWidget3.bind("<Leave>", controller.releaseTools)

    graphWidget3Tool.config(bg=value.widgetBackground,borderwidth= value.borderWidth, relief=value.relief)
    graphWidget3Tool.bind("<Enter>", controller.getTools)

    toolbar = NavigationToolbar2TkAgg(canvas, graphWidget3Tool)
    toolbar.update()

    graphlabel31 = Label(graphWidget3, text="| LIGHT LEVELS")
    graphlabel31.config(font=(value.titlefont), bg="#65686d", fg="white")
    graphlabel31.place(x=60, y=-2)


    graphAverage = Label(graphWidget3, text="Grey = Light Average   |   Green = Light Value")
    graphAverage.config(font=(value.informationInfoFont), bg="#65686d", fg="grey85")
    graphAverage.place(x=250, y=2)


def replace():
    g3.graphWidget3.place(height=220, width=525, x=330, y=180)

g3 = graphwidget3()