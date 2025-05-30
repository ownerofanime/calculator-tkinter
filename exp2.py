import tkinter
from tkinter import *

window = tkinter.Tk()
label = Label(window, text="Name:")
label.grid(row=0, column=0)

entry = Entry(window)
entry.grid(row=0, column=1)

button = Button(window, text='press me!', bg='red', width=40, height=2)
button.grid(row=2, column=0, columnspan=2, sticky="we")  # Span both columns and stretch

window.mainloop()