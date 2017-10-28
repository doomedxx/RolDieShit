import Frame.mainframe as mainframe
import View_Widgets.temperature as temperature
import View_Widgets.light as light
import View_Widgets.control as control
import View_Widgets.rollercontrol as roller
import View_Widgets.graph1 as graph1
import View_Widgets.graph2 as graph2
import View_Widgets.graph3 as graph3
import View_Widgets.clock as clock
import View_Settings.theme as theme
import View_Settings.maxtemp as max
import View_Settings.mintemp as min
import Model.maxtemp_model as tempModel
import Controller.clock_controller as clockcontrol
import View_Widgets.topframe as Holder

if __name__ == '__main__':
    clockcontrol.timeString
    mainframe.mainloop()