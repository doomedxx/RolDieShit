from tkinter import *
import matplotlib
matplotlib.use("TkAgg")

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import Frame.mainframe as mainframe
import View.widgetValues as value


class graphwidget2(object):
    graphWidget2 = Frame(mainframe.root, relief=SUNKEN)


    graphWidget2.pack(side=LEFT)
    graphWidget2.place(height=220, width=300, x=25, y=180)
    graphWidget2.config(bg=value.widgetBackground,borderwidth= value.borderWidth, relief=value.relief)

    f = Figure(figsize=(4,3), dpi=80, facecolor='#65686d')
    a = f.add_subplot(111)
    a.plot([5,10,15,20,25,30],[13,13,14,15,14,14])

    canvas = FigureCanvasTkAgg(f, graphWidget2)
    canvas.show()
    canvas.get_tk_widget().pack(side=mainframe.TOP, expand=True)

    graphlabel2 = Label(graphWidget2, text="TEMPERATURES")
    graphlabel2.config(font=(value.titlefont), bg="#65686d", fg=value.titleColor)
    graphlabel2.pack()
    graphlabel2.place(x=5, y=-2)

def replace():
    g2.graphWidget2.place(height=220, width=300, x=25, y=180)
g2 = graphwidget2()