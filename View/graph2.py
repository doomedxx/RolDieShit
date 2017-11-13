from tkinter import *
import matplotlib
matplotlib.use("TkAgg")

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
import matplotlib.pyplot as plt
import Frame.mainframe as mainframe
import View.widgetValues as value
import numpy as np


yMax = 40
class graphwidget2(object):
    global yMax
    graphWidget2 = Frame(mainframe.root, relief=SUNKEN)

    graphWidget2.pack(side=LEFT)
    graphWidget2.place(height=220, width=300, x=25, y=180)
    graphWidget2.config(bg=value.widgetBackground,borderwidth= value.borderWidth, relief=value.relief)

    fig = plt.figure(figsize=(4,3), dpi=70, facecolor='#65686d', edgecolor="white")
    ax = fig.add_subplot(1,1,1)

    x = [0,0,0,0,0,0,0,0,0,0,0]
    y = [0,0,0,0,0,0,0,0,0,0,0]
    line, = ax.plot(x,y, 'green')
    line2, = ax.plot(x,y, 'gray')
    ylim = plt.ylim(0,yMax)
    xlim = plt.xlim(0,100)

    canvas = FigureCanvasTkAgg(fig, graphWidget2)
    canvas.get_tk_widget().pack(side=mainframe.TOP, expand=True)

    graphlabel2 = Label(graphWidget2, text="TEMPERATURES")
    graphlabel2.config(font=(value.titlefont), bg="#65686d", fg=value.titleColor)
    graphlabel2.pack()
    graphlabel2.place(x=5, y=-2)

def replace(): ## Wanneer er terug word geschakeld van Settings naar View, word de widget opnieuw geplaatst
    g2.graphWidget2.place(height=220, width=300, x=25, y=180)

def update():
    print("yo")
    plt.show

g2 = graphwidget2()
update()