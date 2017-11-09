import Frame.mainframe as mainframe
from View import clock
from View import light
from View import control
from View import graph1
from View import graph2
from View import lightgraph
from View import rollercontrol
from View import temperature
from View import toolbar
from View import widgetValues
from View.Settings import setting_clock
from View.Settings import setting_mintemp
from View.Settings import setting_maxtemp
from View.Settings import setting_theme
from View.Settings import setting_values
from View.Settings import settings_officehours

def kill():
    print("Dashboard is gesloten")
    mainframe.root.destroy()

mainframe.root.protocol('WM_DELETE_WINDOW', kill)  # root is your root window


def main():
    mainframe.mainloop()
main()