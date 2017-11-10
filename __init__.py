import Frame.mainframe as mainframe
from View_Widgets import light
from View_Widgets import clock
from View_Widgets import control
from View_Widgets import graph1
from View_Widgets import graph2
from View_Widgets import graph3
from View_Widgets import rollercontrol
from View_Widgets import temperature
from View_Widgets import toolbar
from View_Widgets import widgetValues
from View_Widgets import setting_clock
from View_Widgets import setting_mintemp
from View_Widgets import setting_maxtemp
from View_Widgets import setting_theme
from View_Widgets import setting_values
from View_Widgets import settings_officehours

def kill():
    print("Dashboard is gesloten")
    mainframe.root.destroy()

mainframe.root.protocol('WM_DELETE_WINDOW', kill)  # root is your root window


def main():
    mainframe.mainloop()

main()