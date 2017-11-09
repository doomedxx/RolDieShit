import View as view
from View import toolbar as toolview
import Frame.mainframe as frame
import threading

selected = "view"
color = 60
def executeSettings():
    global selected
    global color
    view.clock.c.clockWidget.place_forget()
    view.control.c1.controlWidget.place_forget()
    view.light.l1.lightWidget.place_forget()
    view.temperature.t1.tempWidget.place_forget()
    view.lightgraph.g3.graphWidget3.place_forget()
    view.graph2.g2.graphWidget2.place_forget()
    view.graph1.g1.graphWidget.place_forget()
    view.rollercontrol.r1.rollerWidget.place_forget()

    view.settings_officehours.office1.addBlock()
    view.setting_theme.t1.addBlock()
    view.setting_maxtemp.max1.addBlock()
    view.setting_mintemp.min1.addBlock()
    view.setting_clock.c1.addBlock()

    toolview.w1.menuButton2.config(fg="white")
    toolview.w1.Selected.place(x=660, y=46)
    toolview.w1.menuButton1.config(fg="gray60")
    toolview.w1.Selected.config(text="............................................................................................................................")
    selected = "settings"
    color = 60
def executeView():
    global selected
    global color
    view.setting_theme.t1.themeWidget.place_forget()
    view.setting_maxtemp.max1.closetempWidget.place_forget()
    view.setting_mintemp.min1.opentempsetting.place_forget()
    view.setting_clock.c1.clocksettingwidget.place_forget()
    view.settings_officehours.office1.officesetting.place_forget()

    view.control.replace()
    view.graph1.replace()
    view.graph2.replace()
    view.lightgraph.replace()
    view.clock.replace()
    view.rollercontrol.replace()
    view.temperature.replace()
    view.light.replace()

    toolview.w1.Selected.place(x=550, y=46)
    toolview.w1.menuButton1.config(fg="white")
    toolview.w1.menuButton2.config(fg="gray60")
    toolview.w1.Selected.config(text="..................................................................")
    selected = "view"
    color = 60

def executeHover(button):
    global color
    global selected
    if color <= 98 and button == 1 and selected !="view":
        frame.root.after(10, executeHover, button)
        toolview.w1.menuButton1.config(fg='gray{}'.format(color))
        color+=4
    elif color <= 98 and button == 2 and selected !="settings":
        frame.root.after(10, executeHover, button)
        toolview.w1.menuButton2.config(fg='gray{}'.format(color))
        color+=4
    elif color >= 101:
        color = 100
def executeLeave(button):
    global color
    global selected
    if color >= 40 and button == 1 and selected !="view":
        frame.root.after(10, executeLeave, button)
        toolview.w1.menuButton1.config(fg='gray{}'.format(color))
        color-= 4
    elif color >= 40 and button == 2 and selected !="settings":
        frame.root.after(10, executeLeave, button)
        toolview.w1.menuButton2.config(fg='gray{}'.format(color))
        color-= 4

