from tkinter import *

import Frame.mainframe as mainframe
import View.widgetValues as value


class graphwidget(object):
    graphWidget = Frame(mainframe.root, relief=SUNKEN)

    graphLabel = Label(graphWidget, text="EEN GRAPH")
    graphLabel.config(font=(value.titlefont), bg=value.widgetBackground, fg=value.titleColor)
    graphLabel.pack()
    graphLabel.place(x=5, y=1)

    graphWidget.pack(side=LEFT)
    graphWidget.place(height=150, width=525, x=330, y=mainframe.windowHeight-160)
    graphWidget.config(bg=value.widgetBackground,borderwidth= value.borderWidth, relief=value.relief)

    graphLabel1 = Label(graphWidget, text="GRAPH 1")
    graphLabel1.config(font=(value.titlefont), bg=value.widgetBackground, fg="white")
    graphLabel1.pack()
    graphLabel1.place(x=10, y=30)

    graphLabel2 = Label(graphWidget, text="Placeholder")
    graphLabel2.config(font=(value.titlefont), bg=value.widgetBackground, fg="white")
    graphLabel2.pack()
    graphLabel2.place(x=10, y=30)

def replace():
    g1.graphWidget.place(height=150, width=530, x=330, y=mainframe.windowHeight-160)

g1 = graphwidget
