import hashlib
from tkinter import *
from tkinter.messagebox import showinfo, showerror
import uuid

first_hash_pass = hashlib.new('md5')
second_hash_pass = hashlib.new('md5')
third_hash_pass = hashlib.new('md5')


pass_dict = {}
salt_dict = {}


#   функция авторизации
def sing_up_func():
    if login_entry.get() in pass_dict.keys():
        showerror('Error', 'You\'ve already authorised')
    else:
        salt_dict.setdefault(login_entry.get(), uuid.uuid4().hex)
        pass_dict.setdefault(login_entry.get(), hashlib.md5(bytes((pass_entry.get() + salt_dict[login_entry.get()]).encode())))


#   функция входа


#  функция проверки пароля
def check_password():
    pass_check = hashlib.md5(bytes(pass_entry.get() + salt_dict[login_entry.get()]))
    if pass_check.digest() == pass_dict[login_entry.get()].digest():
        showinfo('Result', 'Password is correct!')
        login_entry.delete(0, END)
        pass_entry.delete(0, END)
        login_entry.focus()
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


#   поля ввода логина и пароля
login_entry = Entry(justify=LEFT, font='TimesNewRoman 11')
login_entry.place(height=40, width=150, x=30, y=40)
login_entry.focus()
pass_entry = Entry(justify=LEFT, font='TimesNewRoman 11')
pass_entry.place(height=40, width=150, x=30, y=120)


#   кнопки ввода пароля и проверки
enter_pass_butt = Button(text='Sign in', font='Sylfaen', background='PaleVioletRed')
enter_pass_butt.place(height=30, width=90, x=210, y=60)
check_pass_butt = Button(text='Sign up', font='Sylfaen 12', background='PaleVioletRed')
check_pass_butt.place(height=25, width=80, x=215, y=110)


root.mainloop()