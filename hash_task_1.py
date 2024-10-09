import hashlib
from tkinter import *
from tkinter.messagebox import showinfo, showerror
import uuid

my_hash_pass = hashlib.new('md5')
salt = uuid.uuid4().hex


#   функция ввода и хеширования пароля
def hash_password():
    my_hash_pass.update(bytes((enter_pass_entry.get() + salt).encode()))
    check_pass_entry.focus()


#   функция проверки пароля
def check_password():
    my_hash_check = hashlib.md5(bytes((check_pass_entry.get() + salt).encode()))
    if my_hash_check.digest() == my_hash_pass.digest():
        showinfo('Result', 'Password is correct!')
        enter_pass_entry.delete(0, END)
        check_pass_entry.delete(0, END)
        enter_pass_entry.focus()
    else:
        showerror('Result', 'Password is wrong(')


#   создаём окно для ввода пароля
root = Tk()
root.title('Authorization')
root.geometry('330x200')
root['bg'] = 'LightPink'
root.resizable(False, False)
Label(text='Login:', font='Sylfaen', background='PaleVioletRed').place(x=30, y=5)
Label(text='Password:', font='Sylfaen', background='PaleVioletRed').place(x=30, y=85)


#   поля ввода пароля
enter_pass_entry = Entry(justify=LEFT, font='TimesNewRoman 11')
enter_pass_entry.place(height=40, width=150, x=30, y=40)
enter_pass_entry.focus()
check_pass_entry = Entry(justify=LEFT, font='TimesNewRoman 11')
check_pass_entry.place(height=40, width=150, x=30, y=120)


#   кнопки ввода пароля и проверки
enter_pass_butt = Button(text='Enter', font='Sylfaen', background='PaleVioletRed', command=hash_password)
enter_pass_butt.place(height=30, width=90, x=210, y=45)
check_pass_butt = Button(text='Check', font='Sylfaen', background='PaleVioletRed', command=check_password)
check_pass_butt.place(height=30, width=90, x=210, y=125)


root.mainloop()