from tkinter import *
from tkinter import Tk


windowHeight = 570
windowWidth = 880

root = Tk()
root.configure(background='gray15')
root.title("RolDieShit Dashboard")
root.resizable(width=False, height=False)
root.minsize(width=windowWidth, height=windowHeight)
root.iconbitmap('icon.ico')
widgetList = []
