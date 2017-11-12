import Frame.mainframe as f
from View.Settings import setting_theme as theme
from View import widgetValues as value

color = 16

def lightTransition():
    global color
    if color <= 80:
        f.root.after(10, lightTransition)
        f.root.configure(background='gray{}'.format(color))
        f.VersionNumber.config(text="Version 0.2", font=("DIN-bold", 8), bg='gray{}'.format(color),  fg="gray5")
        f.Username.config(text="Version 0.2", font=("DIN-bold", 8), bg='gray{}'.format(color),  fg="gray5")
        color+=3

def darkTransition():
    global color
    if color >= 15:
        f.root.after(10, darkTransition)
        f.root.configure(background='gray{}'.format(color))
        f.VersionNumber.config(text="Version 0.2", font=("DIN-bold", 8), bg='gray{}'.format(color),  fg="white")
        f.Username.config(text="Version 0.2", font=("DIN-bold", 8), bg='gray{}'.format(color),  fg="white")
        color-=3