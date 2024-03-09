"""
button = you click it, then it does stuff
"""

from tkinter import *

count = 0


def click():
    global count
    count += 1
    print(count)


window = Tk()

photo = PhotoImage("Python-Fundamentals-2024\\66-Buttons\\thumbs-up.png")
button = Button(
    window,
    text="Click me",
    command=click,
    font=("Comic Sans", 30),
    fg="#00FF00",
    bg="black",
    activeforeground="#00FF00",
    activebackground="black",
    image=photo,
    compound="top",
)
button.pack()


window.mainloop()
