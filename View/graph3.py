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

    f = Figure(figsize=(10,5), dpi=100, facecolor='#9a9ca0')
    f.tight_layout()
    a = f.add_subplot(111)
    x = np.array(range(1,13))
    y = np.random.randint(80, size=x.shape)
    a.plot(x,y)

    canvas = FigureCanvasTkAgg(f, graphWidget3)
    canvas.get_tk_widget().grid(row=20,column=6,sticky=W)
    canvas.get_tk_widget().pack(expand=True)
    canvas.get_tk_widget().config(height=220)

    graphWidget3.pack(side=RIGHT)
    graphWidget3.place(height=220, width=525, x=330, y=180)
    graphWidget3.config(bg=value.widgetBackground,borderwidth= value.borderWidth, relief=value.relief)
    graphlabel31 = Label(graphWidget3, text="LIGHT LEVELS")
    graphlabel31.config(font=(value.titlefont), bg="#9a9ca0", fg="white")
    graphlabel31.pack()
    graphlabel31.place(x=10, y=-2)

    toolbar = NavigationToolbar2TkAgg(canvas, graphWidget3)
    toolbar.update()
    canvas._tkcanvas.pack(side=mainframe.TOP,expand=True)

def replace():
    g3.graphWidget3.place(height=220, width=525, x=330, y=180)

g3 = graphwidget3()