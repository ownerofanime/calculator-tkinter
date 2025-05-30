import tkinter
from tkinter import *

def output(number):
    output_label.config(text=f'{number}')

window = Tk()
window.title('Calculator Program')
window.geometry('600x600')

output_label = Label(window, text="",height=2, font=('arial', 30), bg='grey')
output_label.grid(row=0, columnspan=2, sticky='we',)

button = Button(window, text='1',height=4, width=9,font=('arial', 15), bg='grey', command=lambda: output(1))
button.grid(row=1, column=0, stick='w')


window.mainloop()