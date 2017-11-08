from tkinter import *

import Frame.mainframe as mainframe
import View.widgetValues as value


class graphwidget3(object):
    graphWidget3 = Frame(mainframe.root, relief=SUNKEN)

    graphlabel3 = Label(graphWidget3, text="EEN GRAPH")
    graphlabel3.config(font=(value.titlefont), bg=value.widgetBackground, fg=value.titleColor)
    graphlabel3.pack()
    graphlabel3.place(x=5, y=1)

    graphWidget3.pack(side=LEFT)
    graphWidget3.place(height=150, width=525, x=330, y=mainframe.windowHeight-320)
    graphWidget3.config(bg=value.widgetBackground,borderwidth= value.borderWidth, relief=value.relief)

    graphlabel31 = Label(graphWidget3, text="GRAPH 3")
    graphlabel31.config(font=(value.titlefont), bg=value.widgetBackground, fg="white")
    graphlabel31.pack()
    graphlabel31.place(x=10, y=30)

    graphlabel3 = Label(graphWidget3, text="Placeholder")
    graphlabel3.config(font=(value.titlefont), bg=value.widgetBackground, fg="white")
    graphlabel3.pack()
    graphlabel3.place(x=10, y=30)

def replace():
    g3.graphWidget3.place(height=150, width=530, x=330, y=mainframe.windowHeight-320)

g3 = graphwidget3()