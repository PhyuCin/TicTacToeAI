# tic tac toe game
from tkinter import Button

from future.moves import tkinter

# create window

window = tkinter.Tk()

for i in range(3):
    for j in range(3):
        frame = tkinter.Frame(
            master=window
        )
        frame.grid(row=i, column=j)
        button = Button(text= "H", width=10, height=5)
        button.grid(row=i, column=j)

window.mainloop()

