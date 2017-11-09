import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import numpy as np

from tkinter import *

import Frame.mainframe as mainframe
import View.widgetValues as value


class graphwidget3(object):
    graphWidget3 = Frame(mainframe.root, relief=SUNKEN)
    graphWidget3Tool = Frame(mainframe.root, relief=SUNKEN)

    f = Figure(figsize=(10,5), dpi=100, facecolor='#65686d')
    a = f.add_subplot(111)
    x = np.array(range(1,13))
    y = np.random.randint(80, size=x.shape)
    a.plot(x,y)

    canvas = FigureCanvasTkAgg(f, graphWidget3)
    canvas.get_tk_widget().pack(expand=True)
    canvas.get_tk_widget().configure(background='black')

    graphWidget3.place(height=220, width=525, x=330, y=180)
    graphWidget3.config(bg=value.widgetBackground,borderwidth= value.borderWidth, relief=value.relief)
    # graphWidget3Tool.place(height=30, width=525, x=330, y=400)
    # graphWidget3Tool.config(bg=value.widgetBackground,borderwidth= value.borderWidth, relief=value.relief)
    #
    # toolbar = NavigationToolbar2TkAgg(canvas, graphWidget3Tool)
    # toolbar.update()

    graphlabel31 = Label(graphWidget3, text="LIGHT LEVELS")

    graphlabel31.config(font=(value.titlefont), bg="#65686d", fg="white")
    graphlabel31.pack()
    graphlabel31.place(x=10, y=-2)


def replace():
    g3.graphWidget3.place(height=220, width=525, x=330, y=180)

g3 = graphwidget3()