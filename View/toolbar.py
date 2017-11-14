from tkinter import *

import Controller.toolbar_controller as controller
import Frame.mainframe as mainframe
import View.widgetValues as value


class widgetholder:
    def __init__(self): ##Top bar
        self.selectedbutton = 495

        self.widgetHolder = mainframe.Frame(mainframe.root, relief=SUNKEN)
        self.widgetHolder.config(bg="gray25")
        self.widgetHolder.pack()
        self.widgetHolder.place(height=60,width=970,x=0, y=value.widgetHeight-105)

        self.tempImage = PhotoImage(file="images/dashboard-icon.png")
        self.titleIcon = Label(self.widgetHolder, image=self.tempImage, bg="gray25")
        self.titleIcon.pack()
        self.titleIcon.place(x=20, y=0)

        self.titleLabel = Label(self.widgetHolder, text="ROLDIESHIZZLE DASHBOARD")
        self.titleLabel.config(font=("code bold", 22), bg="gray25", fg=value.titleColor)
        self.titleLabel.pack()
        self.titleLabel.place(x=95, y=20)

        self.menuButton1 = Button(self.widgetHolder, text="VIEW")
        self.menuButton1.config(font=("code bold", 22), bg="gray25", fg=value.titleColor, borderwidth= 1, relief="flat")
        self.menuButton1.pack()
        self.menuButton1.place(x=540, y=13)

        self.menuButton2 = Button(self.widgetHolder, text="SETTINGS")
        self.menuButton2.config(font=("code bold", 22), bg="gray25", fg="gray60", borderwidth= 1, relief="flat")
        self.menuButton2.pack()
        self.menuButton2.place(x=650, y=13)

        self.Selected = Label(self.widgetHolder, text="..................................................................")
        self.Selected.config(font=("code bold", 7), bg="gray25", fg="deep sky blue", borderwidth= 1, relief="flat")
        self.Selected.pack()
        self.Selected.place(x=548, y=46)

        self.menuButton1.bind("<ButtonRelease-1>", controller.goView)
        self.menuButton1.bind("<Enter>", lambda event: controller.hover(1))
        self.menuButton1.bind("<Leave>", lambda event: controller.leave(1))

        self.menuButton2.bind("<ButtonRelease-1>", controller.goSettings)
        self.menuButton2.bind("<Enter>", lambda event: controller.hover(2))
        self.menuButton2.bind("<Leave>", lambda event: controller.leave(2))
w1 = widgetholder()
