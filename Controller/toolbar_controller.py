from Model.Settings import toolbar_model as model


def goSettings(event):
    model.executeSettings()

def goView(event):
    model.executeView()

def hover(button):
    model.executeHover(button)

def leave(button):
    model.executeLeave(button)