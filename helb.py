import tkinter
from tkinter import *

def say_hello():
    print("Hello!")

window = Tk()
window.title('hello world button')
window.geometry('1000x1000')

button = Button(window, text='Click Me', command=say_hello)
button.pack()

window.mainloop()