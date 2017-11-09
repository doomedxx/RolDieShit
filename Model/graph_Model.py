from View import lightgraph as view
from View import graph1 as graph1
import Frame.mainframe as mainframe

pos = 410

def getTools():
    view.g3.graphWidget3Tool.place(x=330, y=400, width=525)
    graph1.g1.graphWidget.place(height=150, width=525, x=330, y=440)

def releaseTools():
    mainframe.root.after(2000,releaseGo)

def releaseGo():
    graph1.g1.graphWidget.place(height=150, width=525, x=330, y=410)
    view.g3.graphWidget3Tool.place_forget()
