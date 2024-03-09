"""
GUI = Graphical User Interface

Tkinter = which is a module in python. That helps with GUI 

widgets = GUI elements: button, textbox, labels, images
windows = serves as a container to hold or contain these widgets
"""

from tkinter import *

window = Tk()  # instantiate an instance of a window
window.geometry("420x420")
window.title("Yashar's First GUI")

icon = PhotoImage(file="Python-Fundamentals-2024\\64-GUIWindows\\Instagram-Icon.png")
window.iconphoto(True, icon)

window.config(background="#5cfcff")  # hex color
window.mainloop()  # place window on computer screen, listen for events
