from tkinter import *
import sqlite3
from tkinter import messagebox

main = Tk()
main.title('Birth Dates')
main.geometry('400x450')

# Connecting to the Database
main_d = sqlite3.connect('birthdates_record.db')

# Creating a cursor
c = main_d.cursor()


# Save function
def save():
    main_d = sqlite3.connect('birthdates_record.db')
    c = main_d.cursor()

    c.execute('''INSERT INTO birthdates
    VALUES (:f_name, :l_name, :month, :day)''',
        {
            'f_name': f_name_entry.get(),
            'l_name': l_name_entry.get(),
            'month': month_entry.get(),
            'day': day_entry.get()

        })

    main_d.commit()  # Commit change
    main_d.close()  # Close connection

    # Clear the Entry Boxes
    f_name_entry.delete(0, END)
    l_name_entry.delete(0, END)
    month_entry.delete(0, END)
    day_entry.delete(0, END)


class show:

    def __init__(self):
        sh = Tk()
        sh.title('Records')
        sh.geometry('450x450')

        main_d = sqlite3.connect('birthdates_record.db')
        c = main_d.cursor()

        c.execute('SELECT *, oid FROM birthdates')
        records = c.fetchall()

        id = ''
        fname = ''
        lname = ''
        smonth = ''
        sday = ''

        # closing function
        def ok():
            sh.destroy()

        # Labels
        sh_id = Label(sh, text='ID').grid(row=1, column=0, padx=10, pady=6)
        sh_fname = Label(sh, text='FIRST NAME').grid(row=1, column=1, padx=10, pady=6)
        sh_lname = Label(sh, text='LAST NAME').grid(row=1, column=2, padx=10, pady=6)
        sh_month = Label(sh, text='MONTH').grid(row=1, column=3, padx=10, pady=6)
        sh_day = Label(sh, text='DAY').grid(row=1, column=4, padx=10, pady=6)

        for record in records:
            id += str(record[4]) + '\n'
            fname += str(record[0]) + '\n'
            lname += str(record[1]) + '\n'
            smonth += str(record[2]) + '\n'
            sday += str(record[3]) + '\n'

        # Inputting the values of the records in respective label
        id_l = Label(sh, text=id).grid(row=2, column=0, padx=5)
        fname_l = Label(sh, text=fname).grid(row=2, column=1, padx=5)
        lname_l = Label(sh, text=lname).grid(row=2, column=2, padx=5)
        month_l = Label(sh, text=smonth).grid(row=2, column=3, padx=5)
        day_l = Label(sh, text=sday).grid(row=2, column=4, padx=5)

        ok_btn = Button(sh, text='OK', command=ok).grid(row=3, column=2, padx=6, ipadx=50)

        main_d.commit()  # Commit change
        main_d.close()  # Close connection


def update():
    main_d = sqlite3.connect('birthdates_record.db')  # Create a database or connect to one
    c = main_d.cursor()  # Create cursor

    record_id = edit_entry.get()

    c.execute('''UPDATE birthdates SET
     first_name = :f_name,
     last_name = :l_name,
     month = :month,
     day = :day 
     
     WHERE oid = :oid''', {
        'f_name': f_name_entry_editor.get(),
        'l_name': l_name_entry_editor.get(),
        'month': month_entry_editor.get(),
        'day': day_entry_editor.get(),
        'oid': record_id
    })

    main_d.commit()  # Commit change
    main_d.close()  # Close connection

    messagebox.showinfo('Info', 'Record Updated!')  # Show a message
    editor.destroy()  # Close the window


def edit():
    global editor

    editor = Tk()
    editor.title('Update Records')
    editor.geometry('350x350')

    # Making the variable global
    global f_name_entry_editor
    global l_name_entry_editor
    global month_entry_editor
    global day_entry_editor

    main_d = sqlite3.connect('birthdates_record.db')  # Create a database or connect to one
    c = main_d.cursor()  # Create cursor

    # Labels
    f_name_editor = Label(editor, text='FIRST NAME').grid(row=2, column=0, padx=10, pady=4)
    l_name_editor = Label(editor, text='LAST NAME').grid(row=3, column=0, padx=10, pady=4)
    month_editor = Label(editor, text='MONTH').grid(row=4, column=0, padx=10, pady=4)
    day_editor = Label(editor, text='DAY').grid(row=5, column=0, padx=10, pady=4)

    # Entry boxes
    f_name_entry_editor = Entry(editor, width=30, bg='yellow', fg='blue')
    f_name_entry_editor.grid(row=2, column=1, padx=20, pady=4)
    l_name_entry_editor = Entry(editor, width=30, bg='yellow', fg='blue')
    l_name_entry_editor.grid(row=3, column=1, padx=20, pady=4)
    month_entry_editor = Entry(editor, width=30, bg='yellow', fg='blue')
    month_entry_editor.grid(row=4, column=1, padx=20, pady=4)
    day_entry_editor = Entry(editor, width=30, bg='yellow', fg='blue')
    day_entry_editor.grid(row=5, column=1, padx=20, pady=4)

    edit_id = edit_entry.get()
    c.execute('SELECT * FROM birthdates WHERE oid= ' + edit_id)
    records = c.fetchall()

    # Loop thru the record
    for record in records:
        f_name_entry_editor.insert(0, record[0])
        l_name_entry_editor.insert(0, record[1])
        month_entry_editor.insert(0, record[2])
        day_entry_editor.insert(0, record[3])

    save_button_editor = Button(editor, text='Save', command=update, bg='black', fg='white').grid(row=6, column=1, pady=10, padx=5, ipadx=20, columnspan=2)  # Save button
    main_d.commit()  # Commit change
    main_d.close()  # Close connection


"""
# Creating a table
c.execute('''CREATE TABLE birthdates(
                first_name text,
                last_name text,
                month text, 
                day integer
                )''')
"""

Top = Label(main, text='Birth Date Records').grid(row=0, column=0, columnspan=3, padx=10, pady=10, ipadx=120)

# Labels
f_name = Label(main, text='FIRST NAME').grid(row=2, column=0, padx=10, pady=4)
l_name = Label(main, text='LAST NAME').grid(row=3, column=0, padx=10, pady=4)
month = Label(main, text='MONTH').grid(row=4, column=0, padx=10, pady=4)
day = Label(main, text='DAY').grid(row=5, column=0, padx=10, pady=4)
select_id = Label(main, text='Select ID').grid(row=7, column=0, pady=4)

# Entry boxes
f_name_entry = Entry(main, width=30, bg='yellow', fg='blue')
f_name_entry.grid(row=2, column=1, padx=10, pady=4)
l_name_entry = Entry(main, width=30, bg='yellow', fg='blue')
l_name_entry.grid(row=3, column=1, padx=10, pady=4)
month_entry = Entry(main, width=30, bg='yellow', fg='blue')
month_entry.grid(row=4, column=1, padx=10, pady=4)
day_entry = Entry(main, width=30, bg='yellow', fg='blue')
day_entry.grid(row=5, column=1, padx=10, pady=4)
edit_entry = Entry(main, width=30, bg='yellow', fg='blue')
edit_entry.grid(row=7, column=1, padx=3, pady=4)

save_button = Button(main, text='Save', command=save, bg='black', fg='white').grid(row=6, column=0, pady=10, padx=5, ipadx=20)  # Save button
show_btn = Button(main, text='Show Records', command=show, bg='black', fg='white').grid(row=6, column=1, pady=10, ipadx=10)  # Show button
edit_btn = Button(main, text='Edit', command=edit, bg='black', fg='white').grid(row=8, column=1, pady=10, padx=10, ipadx=50)  # Edit button

main_d.commit()  # Commit change
main_d.close()  # Close connection

main.mainloop()
