from tkinter import *

cal = Tk()
cal.title('Simple Calculator')

first_num = 0
math = ''

e = Entry(cal, width=50, borderwidth=6, bd=20, insertwidth=2, font=('arial', 10, 'bold'))
e.grid(row=0, column=0, columnspan=3, padx=10, pady=2)
e.get()
e.insert(0, "")


def button_equal():
    total = int(e.get())
    e.delete(0, END)

    if math == 'addition':
        e.insert(0, first_num + total)

    if math == 'subtraction':
        e.insert(0, first_num - total)

    if math == 'multiplication':
        e.insert(0, first_num * total)

    if math == 'division':
        e.insert(0, first_num / total)


def button_clear():
    e.delete(0, END)


def button_insert(number):

    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))


def button_add():
    f_num = e.get()
    global first_num
    global math
    math = 'addition'
    first_num = int(f_num)
    e.delete(0, END)


def button_subtract():
    f_num = e.get()
    global first_num
    global math
    math = 'subtraction'
    first_num = int(f_num)
    e.delete(0, END)


def button_multiply():
    f_num = e.get()
    global first_num
    global math
    math = 'multiplication'
    first_num = int(f_num)
    e.delete(0, END)


def button_divide():
    f_num = e.get()
    global first_num
    global math
    math = 'division'
    first_num = int(f_num)
    e.delete(0, END)


# Defining the buttons
button_1 = Button(cal, text='1', padx=40, pady=20, bd=8, font=('arial', 20, 'bold'), command=lambda: button_insert(1))
button_2 = Button(cal, text='2', padx=40, pady=20, bd=8, font=('arial', 20, 'bold'), command=lambda: button_insert(2))
button_3 = Button(cal, text='3', padx=40, pady=20, bd=8, font=('arial', 20, 'bold'), command=lambda: button_insert(3))
button_4 = Button(cal, text='4', padx=40, pady=20, bd=8, font=('arial', 20, 'bold'), command=lambda: button_insert(4))
button_5 = Button(cal, text='5', padx=40, pady=20, bd=8, font=('arial', 20, 'bold'), command=lambda: button_insert(5))
button_6 = Button(cal, text='6', padx=40, pady=20, bd=8, font=('arial', 20, 'bold'), command=lambda: button_insert(6))
button_7 = Button(cal, text='7', padx=40, pady=20, bd=8, font=('arial', 20, 'bold'), command=lambda: button_insert(7))
button_8 = Button(cal, text='8', padx=40, pady=20, bd=8, font=('arial', 20, 'bold'), command=lambda: button_insert(8))
button_9 = Button(cal, text='9', padx=40, pady=20, bd=8, font=('arial', 20, 'bold'), command=lambda: button_insert(9))
button_0 = Button(cal, text='0', padx=40, pady=20, bd=8, font=('arial', 20, 'bold'), command=lambda: button_insert(0))

button_add = Button(cal, text='+', padx=40, pady=20, bd=8, font=('arial', 20, 'bold'), command=button_add)
button_equal = Button(cal, text='=', padx=106, pady=20, bd=8, font=('arial', 20, 'bold'), command=button_equal)
button_clear = Button(cal, text='AC', padx=95, pady=20, bd=8, font=('arial', 20, 'bold'), command=button_clear)

button_subtract = Button(cal, text='-', padx=41, pady=20, bd=8, font=('arial', 20, 'bold'), command=button_subtract)
button_multiply = Button(cal, text='x', padx=40, pady=20, bd=8, font=('arial', 20, 'bold'), command=button_multiply)
button_divide = Button(cal, text='/', padx=41, pady=20, bd=8, font=('arial', 20, 'bold'), command=button_divide)


# Put the buttons on the screen

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)
button_clear.grid(row=4, column=1, columnspan=2)

button_add.grid(row=5, column=0)
button_equal.grid(row=5, column=1, columnspan=2)

button_subtract.grid(row=6, column=0)
button_multiply.grid(row=6, column=1)
button_divide.grid(row=6, column=2)

cal.mainloop()
