#!/usr/bin/env python
# coding: utf-8

# In[3]:


# password
from tkinter import *
import random

win = Tk()
win.title("Password Generator")
win.geometry("350x220")

def make_password():
    try:
        size = int(length_box.get())
        if size < 4:
            output.config(text="Too short")
            return
        letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        digits = "0123456789"
        symbols = "!@#$%^&*()_+-=[]{}|;:,.<>?"

        all_chars = letters + digits + symbols
        password = ""
        for i in range(size):
            password += random.choice(all_chars)

        output.config(text=password)
    except:
        output.config(text="Enter a number")

Label(win, text="Password Length:", font=('Arial', 13)).pack(pady=10)

length_box = Entry(win, font=('Arial', 13), width=10)
length_box.pack()

Button(win, text="Generate", font=('Arial', 12), command=make_password).pack(pady=15)

output = Label(win, text="", font=('Arial', 14), fg="green")
output.pack()

win.mainloop()


# In[ ]:



