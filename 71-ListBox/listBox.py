"""
listbox = a listing of selectable text item within it's container
"""


def submit():
    food = []
    for index in listbox.curselection():
        food.insert(index, listbox.get(index))

    print("You have ordered: ")
    for index in food:
        print(index)


def add():
    listbox.insert(listbox.size(), entry_box.get())
    listbox.config(height=listbox.size())


def delete():
    for index in reversed(listbox.curselection()):
        listbox.delete(index)
    listbox.config(height=listbox.size())


from tkinter import *

window = Tk()

listbox = Listbox(
    window,
    background="#f7ffde",
    font=("Constantia", 35),
    width=12,
    selectmode=MULTIPLE,
)
listbox.pack()

listbox.insert(1, "Pizza")
listbox.insert(2, "Pasta")
listbox.insert(3, "Garlic bread")
listbox.insert(3, "Soup")

listbox.config(height=listbox.size())

entry_box = Entry(window)
entry_box.pack()

submit_button = Button(window, text="submit", command=submit)
submit_button.pack()

add_button = Button(window, text="add", command=add)
add_button.pack()


delete_button = Button(window, text="delete", command=delete)
delete_button.pack()

window.mainloop()
