import Frame.mainframe as mainframe
from View import light
from View import clock
from View import control
from View import graph1
from View import graph2
from View import graph3
from View import rollercontrol
from View import temperature
from View import toolbar
from View import widgetValues
from View import setting_clock
from View import setting_mintemp
from View import setting_maxtemp
from View import setting_theme
from View import setting_values
from View import settings_officehours

def kill():
    print("Dashboard is gesloten")
    mainframe.root.destroy()

mainframe.root.protocol('WM_DELETE_WINDOW', kill)  # root is your root window


def main():
    mainframe.mainloop()

main()