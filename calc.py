import tkinter
from tkinter import *

current_input = ""
first_number = None
operation = None
reset_next = False

def calculate():
    global current_input, first_number, operation, reset_next
    if current_input != "" and first_number is not None and operation is not None: 
        second_number = int(current_input)
        result = 0
        if operation == "+":
            result = first_number + second_number
        elif operation == "-":
            result = first_number - second_number
        elif operation == "*":
            result = first_number * second_number
        elif operation == "/":
            result = first_number / second_number if second_number != 0 else "Error"
        output_label.config(text=str(result))
        current_input = str(result)
        first_number = None
        operation = None
        reset_next = True  # Set flag to reset on next number press

def clear():
    global current_input, first_number, operation
    current_input = ""
    first_number = ""
    operation = ""
    output_label.config(text="")

def output(number):
    global current_input, reset_next
    if reset_next:
        current_input = str(number)
        reset_next = False
    else:
        current_input += str(number)
    output_label.config(text=current_input)

def set_operation(op):
    global first_number, current_input ,operation
    if current_input != "":
        first_number = int(current_input)
        operation = op
        current_input = ("")
        output_label.config(text="")

def number_clear():
    global first_number, current_input, operation
    if output_label != "":
        current_input = None
        first_number = None
        operation = None
        output_label.config(text="")

window = Tk()
window.title('Calculator Program')
window.geometry('600x600')

#NUMBER OUTPUT
output_label = Label(window, text="",width = 18, height=2, font=('arial', 30), bg='grey')
output_label.grid(row=0, columnspan=4, sticky='we',)

#BUTTON FUNCTIONS
button = Button(window, text='+', height = 4, width=9,font=('arial', 15),bg='grey',
                command=lambda:  set_operation('+'))
button.grid(row=1, column=3, sticky='we')

button = Button(window, text='-', height = 4, width=9,font=('arial', 15),bg='grey',
                command=lambda:  set_operation('-'))
button.grid(row=2, column=3, sticky='we')

button = Button(window, text='*', height = 4, width=9,font=('arial', 15),bg='grey',
                command=lambda: set_operation('*'))
button.grid(row=3, column=3, sticky='we')

button = Button(window, text='/', height = 4, width=9,font=('arial', 15),bg='grey',
                command=lambda: set_operation('/'))
button.grid(row=4, column=1, sticky='we')

#NUMBER LINES
button = Button(window, text='1',height=4, width=9,font=('arial', 15), bg='grey',
                command=lambda: output(1))
button.grid(row=1, column=0, stick='we')
button = Button(window, text='2', height = 4, width=9,font=('reset_next = Falsereset_next = Falsearial', 15),bg='grey',
                command=lambda: output(2))
button.grid(row=1, column=1, sticky='we')
button = Button(window, text='3', height = 4, width=9,font=('arial', 15),bg='grey',
                command=lambda: output(3))
button.grid(row=1, column=2, sticky='we')
button = Button(window, text='4', height = 4, width=9,font=('arial', 15),bg='grey',
                command=lambda: output(4))
button.grid(row=2, column=0, sticky='we')
button = Button(window, text='5', height = 4, width=9,font=('arial', 15),bg='grey',
                command=lambda: output(5))
button.grid(row=2, column=1, sticky='we')
button = Button(window, text='6', height = 4, width=9,font=('arial', 15),bg='grey',
                command=lambda: output(6))
button.grid(row=2, column=2, sticky='we')
button = Button(window, text='7', height = 4, width=9,font=('arial', 15),bg='grey',
                command=lambda: output(7))
button.grid(row=3, column=0, sticky='we')
button = Button(window, text='8', height = 4, width=9,font=('arial', 15),bg='grey',
                command=lambda: output(8))
button.grid(row=3, column=1, sticky='we')
button = Button(window, text='9', height = 4, width=9,font=('arial', 15),bg='grey',
                command=lambda: output(9),)
button.grid(row=3, column=2, sticky='we')
button = Button(window, text='0', height = 4, width=9,font=('arial', 15),bg='grey',
                command=lambda: output(0))
button.grid(row=4, column=0, sticky='we')

#clear button
button = Button(window, text='<', height = 4, width=9,font=('arial', 15),bg='grey',command=clear)
button.grid(row=4, column=2, sticky='we')

#Equals button
button = Button(bg='grey', height = 4, width = 9, font=('arial', 15),text='=', command=calculate)
button.grid(row=4, column=3, sticky='we')
window.mainloop()