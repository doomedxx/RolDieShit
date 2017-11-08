import matplotlib
matplotlib.use("TkAgg")

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure

from tkinter import *
import Frame.mainframe as mainframe
import View.widgetValues as value


class graphtestwidget2(object):
    def __init__(self):
        self.graphtestWidget2 = Frame(mainframe.root, relief=SUNKEN)

        self.graphtestWidget2.pack(side=LEFT)
        self.graphtestWidget2.place(height=220, width=400, x=25, y=570)
        self.graphtestWidget2.config(bg=value.widgetBackground,borderwidth= value.borderWidth, relief=value.relief)

        f = Figure(figsize=(5,5), dpi=80, facecolor='grey')
        a = f.add_subplot(111)
        a.plot([1,2,3,4,5,6,7,8],[5,6,1,3,4,6,7,3])

        canvas = FigureCanvasTkAgg(f, self.graphtestWidget2)
        canvas.show()
        canvas.get_tk_widget().pack(side=mainframe.TOP, expand=True)

def replace():
    g2.graphtestWidget2.place(height=220, width=300, x=25, y=180)

g2 = graphtestwidget2()