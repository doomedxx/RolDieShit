import matplotlib
matplotlib.use("TkAgg")

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure

from tkinter import *

import Frame.mainframe as mainframe
import View.widgetValues as value


class graphwidget3(object):
    graphWidget3 = Frame(mainframe.root, relief=SUNKEN)

    f = Figure(figsize=(7,5), dpi=80, facecolor='#707a75')
    a = f.add_subplot(111)
    a.plot([10,20,30,40,50,60,70,80],[2,3,4,1,4,6,4,2])

    canvas = FigureCanvasTkAgg(f, graphWidget3)
    canvas.show()
    canvas.get_tk_widget().pack(side=mainframe.TOP,expand=True)

    graphWidget3.pack(side=LEFT)
    graphWidget3.place(height=220, width=525, x=330, y=180)
    graphWidget3.config(bg=value.widgetBackground,borderwidth= value.borderWidth, relief=value.relief)
    graphlabel31 = Label(graphWidget3, text="|  LIGHT LEVELS")
    graphlabel31.config(font=(value.titlefont), bg="#707a75", fg="white")
    graphlabel31.pack()
    graphlabel31.place(x=10, y=-2)

    toolbar = NavigationToolbar2TkAgg(canvas, graphWidget3)
    toolbar.update()
    canvas._tkcanvas.pack(side=mainframe.RIGHT,expand=True)

def replace():
    g3.graphWidget3.place(height=220, width=525, x=330, y=180)
    g3.graphWidget3.place(height=220, width=525, x=330, y=180)

g3 = graphwidget3()