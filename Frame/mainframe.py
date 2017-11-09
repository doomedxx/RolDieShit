from tkinter import *
from tkinter import Tk, font

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

loadfont("Fonts/DINBold.ttf")
loadfont("Fonts/DINLight.ttf")
loadfont("Fonts/DINMedium.ttf")
loadfont("Fonts/DINRegular.ttf")

windowHeight = 570
windowWidth = 880

root = Tk()
print(font.families())
root.configure(background='gray15')
root.title("RolDieShit Dashboard")
root.resizable(width=False, height=False)
root.minsize(width=windowWidth, height=windowHeight)
root.iconbitmap('icon.ico')
widgetList = []
