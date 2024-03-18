from tkinter import *


def submit():
    print(f"The temperature is: {str(scale.get())} degrees C")


window = Tk()

hot_image = PhotoImage(file="")
scale = Scale(
    window,
    from_=0,
    to=100,
    length=600,
    orient=VERTICAL,  # orientation of scale
    font=("Consolas", 20),
    tickinterval=10,  # adds numeric indicators for value
    showvalue=0,  # hide current value
    resolution=5,  # increment of slider
    troughcolor="#69EAFF",
    foreground="#FF1C00",
    background="#111111",
)
scale.set(((scale["from"] - scale["to"]) / 2) + scale["to"])
scale.pack()

button = Button(window, text="submit", command=submit)
button.pack()

window.mainloop()
