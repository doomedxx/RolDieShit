from View_Settings import clockSettings as clock_setting
from View_Widgets import clock as clock_widget
import time

def onEnterScript():
    clock_setting.c1.setTooltip("Change clock format")

def onLeaveScript():
    clock_setting.c1.setTooltip("")
