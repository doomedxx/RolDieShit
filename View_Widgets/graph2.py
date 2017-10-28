from tkinter import *

import Frame.mainframe as mainframe
import View_Widgets.widgetValues as value


class graphwidget2(object):
    mainframe.widgetList.append("graph2")
    graphWidget2 = Frame(mainframe.root, relief=SUNKEN)

    graphlabel2 = Label(graphWidget2, text="EEN GRAPH")
    graphlabel2.config(font=(value.titlefont), bg=value.widgetBackground, fg=value.titleColor)
    graphlabel2.pack()
    graphlabel2.place(x=5, y=1)

    graphWidget2.pack(side=LEFT)
    graphWidget2.place(height=150, width=300, x=25, y=180)
    graphWidget2.config(bg=value.widgetBackground,borderwidth= value.borderWidth, relief=value.relief)

    graphlabel21 = Label(graphWidget2, text="GRAPH 1")
    graphlabel21.config(font=(value.titlefont), bg=value.widgetBackground, fg="white")
    graphlabel21.pack()
    graphlabel21.place(x=10, y=30)

    graphlabel22 = Label(graphWidget2, text="Placeholder")
    graphlabel22.config(font=(value.titlefont), bg=value.widgetBackground, fg="white")
    graphlabel22.pack()
    graphlabel22.place(x=10, y=30)

def replace():
    g2.graphWidget2.place(height=150, width=300, x=25, y=180)

g2 = graphwidget2()