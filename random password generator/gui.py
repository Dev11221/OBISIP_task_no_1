from tkinter import StringVar, Tk, Label, Button, IntVar
from tkinter.ttk import Combobox    
from tkinter import messagebox
from Randompass_generator import generate_random_password
box = Tk()
box.geometry('500x500')
box.title("Random password generator")
box.config(bg = 'light blue')
box.resizable(False, False) 

#values
char_no = IntVar()
int_no = IntVar()
special_no = IntVar()
#box title
char_box = Combobox(box,textvariable=char_no, state='readonly')
char_box['values'] = [str(i) for i in range(1, 16)]
char_box.current(3)

int_box = Combobox(box,textvariable=int_no, state='readonly')
int_box['values'] = [str(i) for i in range(1, 16)]
int_box.current(2)

special_box = Combobox(box,textvariable=special_no, state='readonly')
special_box['values'] = [str(i) for i in range(1, 16)]
special_box.current(3)

#place the boxes
char_box.place(x=250, y=50)
int_box.place(x=250, y=150)
special_box.place(x=250, y=250)

#lables for boxes
char_label = Label(box, text='Number of characters:', bg='#59788e', fg='white',font=('Arial', 10, 'bold')  )
char_label.place(x=50, y=50)        
int_label = Label(box, text='Number of integers:', bg='#59788e', fg='white')
int_label.place(x=50, y=150)
special_label = Label(box, text='Number of special characters:', bg='#59788e', fg='white', font=('Arial', 10, 'bold')  )
special_label.place(x=50, y=250)

def on_generate_password():
    pwd = generate_random_password(char_no.get(), int_no.get(), special_no.get())
    password.set(pwd)

Generate_button = Button(box, text = "generate password", cursor= 'hand2'
                        ,command = on_generate_password)
Generate_button.place(x=100, y=350)

password = StringVar()
password_label = Label(box, textvariable=password, bg='#59788e', fg='white', font=('Arial', 12, 'bold'))
password_label.place(x=250, y=350)

def copy_to_clipboard():
    box.clipboard_clear()
    box.clipboard_append(password.get())
    messagebox.showinfo("Copied", "Password copied to clipboard!")

copy_button = Button(box, text="Copy", command=copy_to_clipboard, cursor='hand2')
copy_button.place(x=400, y=350)

box.mainloop()

