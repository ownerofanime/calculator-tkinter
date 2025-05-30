import tkinter
from tkinter import *

def button_pressed(name):
    output_label.config(text=f"You pressed: {name}")

window = Tk()
window.title('Button Press Example')
window.geometry('300x200')

button1 = Button(window, text='Button 1', command=lambda: button_pressed('Button 1'))
button1.pack(pady=10)

button2 = Button(window, text='Button 2', command=lambda: button_pressed('Button 2'))
button2.pack(pady=10)

output_label = Label(window, text="Press a button")
output_label.pack(pady=20)

window.mainloop()