from tkinter import *
import tkinter

window = Tk()
entry = tkinter.Entry(window, width = 100, font =('arial', 20))
entry.pack()
button = tkinter.Button(window, font=('arial, 20'), text= 'click me!')
button.pack()
window.mainloop()