import Frame.mainframe as mainframe
from View import clock
from View import light
from View import control
from View import statswidget
from View import graph2
from View import lightgraph
from View import rollercontrol
from View import temperature
from View import toolbar
from View import widgetValues
from View.Settings import setting_clock
from View.Settings import setting_mintemp
from View.Settings import setting_closelight
from View.Settings import setting_openlight
from View.Settings import setting_theme
from View.Settings import settings_officehours
from View.Settings import setting_graphTemp
from View.Settings import setting_graphLight

closed = False
def kill(): ## What should happen when the window is closed?
    print("Dashboard is gesloten")
    global closed
    closed = True
    mainframe.root.destroy()
    mainframe.mainloop()

mainframe.root.protocol('WM_DELETE_WINDOW', kill)  # root is your root window

while not closed:
    mainframe.mainloop()

