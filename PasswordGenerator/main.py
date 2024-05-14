import os
from tkinter import *
from tkinter import ttk
import random
import string
import pyperclip


# Suppress deprecation warning
os.environ["TK_SILENCE_DEPRECATION"] = "1"

root = Tk()
root.geometry("400x400")
root.resizable(0, 0)
root.title("Password Generator")
root.configure(bg="#2c3e50")

# Define a custom style for the buttons
style = ttk.Style()

style.configure('TButton', foreground='#FFD700', background='#3498db', font=('Arial', 12, 'bold'),bordercolor='#FFD700')

Label(root, text='PASSWORD GENERATOR', font=('Arial', 20, 'bold'), bg="#2c3e50", fg="#fff").pack(pady=10)
Label(root, text='By Tech IS', font=('Arial', 12), bg="#2c3e50", fg="#fff").pack(side=BOTTOM)

pass_str = StringVar()
pass_len = IntVar()

def Generator():
    password = ''
    length = pass_len.get()
    for _ in range(length):
        password += random.choice(string.ascii_letters + string.digits + string.punctuation)
    pass_str.set(password)

Label(root, text='PASSWORD LENGTH', font=('Arial', 10), bg="#2c3e50", fg="#fff").pack(pady=5)
entry_pass_len = Entry(root, textvariable=pass_len, bg="#fff", fg="#000", font=('Arial', 14), bd=2, relief="solid")
entry_pass_len.pack(pady=5)

ttk.Button(root, text="GENERATE PASSWORD", command=Generator, style='TButton').pack(pady=10)

entry_pass_str = Entry(root, textvariable=pass_str, bg="#fff", fg="#000", font=('Arial', 14), bd=2, relief="solid")
entry_pass_str.pack(pady=5)

def Copy_password():
    pyperclip.copy(pass_str.get())

copy_button = ttk.Button(root, text='COPY TO CLIPBOARD', command=Copy_password, style='TButton')
copy_button.pack(pady=10)
style.configure('TButton', foreground='#000')
copy_button.configure(style='TButton')

root.mainloop()



