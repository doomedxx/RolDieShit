import Frame.mainframe as f
from tkinter import *
import View_Widgets
import View_Settings


def goSettings(event):
    View_Widgets.clock.c.clockWidget.place_forget()
    View_Widgets.control.c1.controlWidget.place_forget()
    View_Widgets.light.l1.lightWidget.place_forget()
    View_Widgets.temperature.t1.tempWidget.place_forget()
    View_Widgets.graph3.g3.graphWidget3.place_forget()
    View_Widgets.graph2.g2.graphWidget2.place_forget()
    View_Widgets.graph1.g1.graphWidget.place_forget()
    View_Widgets.rollercontrol.r1.rollerWidget.place_forget()

    View_Settings.officehours.office1.addBlock()
    View_Settings.theme.t1.addBlock()
    View_Settings.maxtemp.max1.addBlock()
    View_Settings.mintemp.min1.addBlock()
    View_Settings.clockSettings.c1.addBlock()


def goView(event):
    View_Settings.theme.t1.themeWidget.place_forget()
    View_Settings.maxtemp.max1.closetempWidget.place_forget()
    View_Settings.mintemp.min1.opentempsetting.place_forget()
    View_Settings.clockSettings.c1.clocksettingwidget.place_forget()
    View_Settings.officehours.office1.officesetting.place_forget()


    View_Widgets.control.replace()
    View_Widgets.graph1.replace()
    View_Widgets.graph2.replace()
    View_Widgets.graph3.replace()
    View_Widgets.clock.replace()
    View_Widgets.rollercontrol.replace()
    View_Widgets.temperature.replace()
    View_Widgets.light.replace()