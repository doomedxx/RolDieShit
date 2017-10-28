from tkinter import *

import Controller.roller_controller as event
import Frame.mainframe as mainframe
import View_Widgets.widgetValues as value


class rollerwidget(object):
    mainframe.widgetList.append("Roller Control Unit")
    rollerWidget = Frame(mainframe.root, relief=SUNKEN)

    rollerLabel = Label(rollerWidget, text="ROLLUCK CONTROL")
    rollerLabel.config(font=(value.titlefont), bg=value.widgetBackground, fg=value.titleColor)
    rollerLabel.pack()
    rollerLabel.place(x=5, y=1)

    rollerWidget.pack(side=LEFT)
    rollerWidget.place(height=150, width=300, x=25, y=mainframe.windowHeight-160)
    rollerWidget.config(bg=value.widgetBackground,borderwidth= value.borderWidth, relief=value.relief)

    rollerLabel1 = Label(rollerWidget, text="Rolluck #1:")
    rollerLabel1.config(font=(value.font, 10), bg=value.widgetBackground, fg="white")
    rollerLabel1.pack()
    rollerLabel1.place(x=10, y=30)

    rollerLabel1Status = Label(rollerWidget, text="Status: UNKNOWN")
    rollerLabel1Status.config(font=(value.font, 8), bg=value.widgetBackground, fg="white")
    rollerLabel1Status.pack()
    rollerLabel1Status.place(x=10, y=48)

    roller1Toggle = Button(rollerWidget, text="Toggle")
    roller1Toggle.config(font=(value.font, 8), bg=value.widgetBackground, fg="white")
    roller1Toggle.pack()
    roller1Toggle.place(x=150, y=38)
    roller1Toggle.bind("<Button-1>", event.callback(1))

    rollerLabel2 = Label(rollerWidget, text="Rolluck #2:")
    rollerLabel2.config(font=(value.font, 10), bg=value.widgetBackground, fg="white")
    rollerLabel2.pack()
    rollerLabel2.place(x=10, y=70)

    rollerLabel2Status = Label(rollerWidget, text="Status: UNKNOWN")
    rollerLabel2Status.config(font=(value.font, 8), bg=value.widgetBackground, fg="white")
    rollerLabel2Status.pack()
    rollerLabel2Status.place(x=10, y=88)


    rollerLabel3 = Label(rollerWidget, text="Rolluck #3:")
    rollerLabel3.config(font=(value.font, 10), bg=value.widgetBackground, fg="white")
    rollerLabel3.pack()
    rollerLabel3.place(x=10, y=110)

    rollerLabel3Status = Label(rollerWidget, text="Status: UNKNOWN")
    rollerLabel3Status.config(font=(value.font, 8), bg=value.widgetBackground, fg="white")
    rollerLabel3Status.pack()
    rollerLabel3Status.place(x=10, y=128)

def replace():
    r1.rollerWidget.place(height=150, width=300, x=25, y=mainframe.windowHeight-160)

r1 = rollerwidget()