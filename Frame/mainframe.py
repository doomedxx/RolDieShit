from tkinter import *
from tkinter import Tk
import getpass
import builtins
builtins.timeGlobal = 1

from ctypes import windll, byref, create_unicode_buffer, create_string_buffer
FR_PRIVATE  = 0x10
FR_NOT_ENUM = 0x20
def loadfont(fontpath, private=True, enumerable=False):
    if isinstance(fontpath, bytes):
        pathbuf = create_string_buffer(fontpath)
        AddFontResourceEx = windll.gdi32.AddFontResourceExA
    elif isinstance(fontpath, str):
        pathbuf = create_unicode_buffer(fontpath)
        AddFontResourceEx = windll.gdi32.AddFontResourceExW
    else:
        raise TypeError('fontpath must be of type str or unicode')
    flags = (FR_PRIVATE if private else 0) | (FR_NOT_ENUM if not enumerable else 0)
    numFontsAdded = AddFontResourceEx(byref(pathbuf), flags, 0)
    return bool(numFontsAdded)


########### LAAD ALLE CUSTOM FONTS ZODAT DEZE KUNNEN WORDEN WEERGEGEVEN##################
loadfont("Fonts/CODE Bold.otf")
loadfont("Fonts/CODE Light.ttf")
loadfont("Fonts/DINBold.ttf")
loadfont("Fonts/DINLight.ttf")
loadfont("Fonts/DINMedium.ttf")
loadfont("Fonts/DINRegular.ttf")

##########################################################################################

windowHeight = 580
windowWidth = 880

root = Tk()
root.configure(background='gray15')
root.title("RolDieShizzle Dashboard")
root.resizable(width=False, height=False)
root.minsize(width=windowWidth, height=windowHeight)
root.iconbitmap('icon.ico')
widgetList = []


################# Geeft informatie weer onderaan de frame. #################
VersionNumber = Label(root)
VersionNumber.config(text="Version 0.2", font=("DIN-bold", 8), bg="gray15",  fg="white")
VersionNumber.place(x=windowWidth - 90, y=windowHeight-25)

Username = Label(root)
Username.config(text=getpass.getuser().upper(), font=("DIN-bold", 8), bg="gray15",  fg="white")
Username.place(x=25, y=windowHeight-25)