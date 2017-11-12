from tkinter import *

import Controller.roller_controller as controller
import Frame.mainframe as mainframe
import View.widgetValues as value


class rollerwidget(object):
    widgetHeight = 150
    widgetWidth = 300
    widgetXPos=25

    widgetBackground = "gray35"

    closeImage = PhotoImage(file='images/closed.png')
    openImage = PhotoImage(file='images/open.png')
    motionImage = PhotoImage(file='images/motion.png')
    mainframe.widgetList.append("Roller Control Unit")
    rollerWidget = Frame(mainframe.root, relief=SUNKEN)

    rollerLabel = Label(rollerWidget, text="ROLLUCK CONTROL")
    rollerLabel.config(font=(value.titlefont), bg=widgetBackground, fg=value.titleColor)
    rollerLabel.pack()
    rollerLabel.place(x=5, y=1)

    rollerWidget.pack(side=LEFT)
    rollerWidget.place(height=widgetHeight, width=widgetWidth, x=25, y=410)
    rollerWidget.config(bg=widgetBackground,borderwidth= value.borderWidth, relief="raised")

    rollerLabel1 = Label(rollerWidget, text="Rolluck #1:")
    rollerLabel1.config(font=(value.font, 10), bg=widgetBackground, fg="white")
    rollerLabel1.pack()
    rollerLabel1.place(x=10, y=30)

    rollerLabel1Status = Label(rollerWidget, text="Status: Open")
    rollerLabel1Status.config(font=(value.font, 8), bg=widgetBackground, fg="white")
    rollerLabel1Status.pack()
    rollerLabel1Status.place(x=10, y=48)

    roller1Toggle = Button(rollerWidget, text="Toggle")
    roller1Toggle.config(font=(value.font, 8), bg="royalblue", fg="white")
    roller1Toggle.pack()
    roller1Toggle.place(x=150, y=38)
    roller1Toggle.bind("<Button-1>", lambda event: controller.rollToggle(1))

    rollerStatus1 = Label(rollerWidget, image=openImage, bg=widgetBackground)
    rollerStatus1.pack()
    rollerStatus1.place(x=widgetWidth-50, y=32)

    rollerLabel2 = Label(rollerWidget, text="Rolluck #2:")
    rollerLabel2.config(font=(value.font, 10), bg=widgetBackground, fg="white")
    rollerLabel2.pack()
    rollerLabel2.place(x=10, y=70)

    rollerLabel2Status = Label(rollerWidget, text="Status: Closed")
    rollerLabel2Status.config(font=(value.font, 8), bg=widgetBackground, fg="white")
    rollerLabel2Status.pack()
    rollerLabel2Status.place(x=10, y=88)

    roller2Toggle = Button(rollerWidget, text="Toggle")
    roller2Toggle.config(font=(value.font, 8), bg="royalblue", fg="white")
    roller2Toggle.pack()
    roller2Toggle.place(x=150, y=78)
    roller2Toggle.bind("<Button-1>",lambda event:  controller.rollToggle(2))

    rollerStatus2 = Label(rollerWidget, image=closeImage, bg=widgetBackground)
    rollerStatus2.pack()
    rollerStatus2.place(x=widgetWidth-50, y=72)

    rollerLabel3 = Label(rollerWidget, text="Rolluck #3:")
    rollerLabel3.config(font=(value.font, 10), bg=widgetBackground, fg="white")
    rollerLabel3.pack()
    rollerLabel3.place(x=10, y=110)

    rollerLabel3Status = Label(rollerWidget, text="Status: Open")
    rollerLabel3Status.config(font=(value.font, 8), bg=widgetBackground, fg="white")
    rollerLabel3Status.pack()
    rollerLabel3Status.place(x=10, y=128)

    rollerStatus3 = Label(rollerWidget, image=openImage, bg=widgetBackground)
    rollerStatus3.pack()
    rollerStatus3.place(x=widgetWidth-50, y=112)

    roller3Toggle = Button(rollerWidget, text="Toggle")
    roller3Toggle.config(font=(value.font, 8), bg="royalblue", fg="white")
    roller3Toggle.pack()
    roller3Toggle.place(x=150, y=118)
    roller3Toggle.bind("<Button-1>",lambda event:  controller.rollToggle(3))

def replace():
    r1.rollerWidget.place(height=150, width=300, x=25, y=410)

r1 = rollerwidget()