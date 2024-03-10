"""
radio button = similar to checkbox, but you can only select one from a group
"""

from tkinter import *

food = ["pizza", "hamburger", "hotdog"]

window = Tk()

pizza_image = PhotoImage(file="Python-Fundamentals-2024\\69-RadioButtons\\pizza.png")
hamburger_image = PhotoImage(
    file="Python-Fundamentals-2024\\69-RadioButtons\\hamburger.png"
)
hotdog_image = PhotoImage(file="Python-Fundamentals-2024\\69-RadioButtons\\hotdog.png")

foodImage = [pizza_image, hamburger_image, hotdog_image]


def order():
    if x.get() == 0:
        print(f"You order pizza")
    elif x.get() == 1:
        print(f"You order a hamburger")
    elif x.get() == 2:
        print(f"You order a hotdog")
    else:
        print("Huh?")


x = IntVar()

for index in range(len(food)):
    radio_button = Radiobutton(
        window,
        text=food[index],  # adds text to radio buttons
        variable=x,  # groups radiobutton together if they share the same variable
        value=index,  # assigns each radiobutton a different value
        padx=25,  # adds padding on  x-axis
        font=("Impact", 25),
        image=foodImage[index],  # adds image to radiobutton
        compound="left",  # adds image & text left-side
        width=375,  # sets width of radiobutton
        command=order,  # set command of radiobutton to function
    )
    radio_button.pack(anchor=W)

window.mainloop()
