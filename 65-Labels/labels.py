"""
label = an area widget that holds text and/or an image within a window
"""

from tkinter import *

window = Tk()
photo = PhotoImage(file="Python-Fundamentals-2024\\65-Labels\\Code_Icon.png")
label = Label(
    window,
    text="Hello World",
    font=("Arial", 40, "bold"),
    fg="green",
    relief=RAISED,
    bg="black",
    bd=10,
    padx=20,
    pady=20,
    image=photo,
    compound="bottom",
)
# label.place(x=0, y=0)
label.pack()

window.mainloop()
