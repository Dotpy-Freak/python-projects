from tkinter import *
import random

main_win = Tk()
main_win.title('Password Generator')
main_win.geometry('900x400')
main_win.configure(bg='white')


def gen():

    pass_entry.delete(0, END)
    val = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*(),.?"
    count = 16
    password = ''

    while len(password) < count:
        password += random.choice(val)

    pass_entry.insert(0, password)


Lbl = Label(main_win, text='Random Password Generator',
            font=('Verdana', 35),
            bd=1, pady=50,
            bg='white',
            padx=97
            )
Lbl.grid(row=0, column=1)

pass_entry = Entry(main_win, width=20, font=('Verdana', 26),
                   bd=5, relief='sunken', state='normal')
pass_entry.grid(row=1, column=1, pady=2)

btn = Button(main_win, text='Generate Password',
             font=('Verdana', 20),
             bg='Lime', fg='White', command=gen)

btn.grid(row=3, column=1, pady=10,)

main_win.mainloop()
