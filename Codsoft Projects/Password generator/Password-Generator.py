from tkinter import *
import tkinter.messagebox as tmsg
from random import randint

root = Tk()
root.wm_iconbitmap("p1.ico")
root.title("Password Generator")
root.geometry("500x330")
root.resizable(False,False)
root.config(bg="#242424")

def generate():
    password.delete(0, END)
    l =int(pass_lenght.get())
    my_password =""
    for i in range(l):
        my_password += chr(randint(33, 126))
    password.insert(0, my_password)

def copy():
    root.clipboard_clear()
    root.clipboard_append(password.get())
    tmsg.showinfo("Copy Passwords","Copied succesfully...")

length = LabelFrame(root, text="Lenght of Password", font="Helvetica 18 bold", bg="#242424", fg="#ffffff" , labelanchor="n", bd=5)
length.pack(pady=15)

pass_lenght = Entry(length, font="Helvetica 25 bold", bd=5, bg="#d0d0d0", relief=SUNKEN)
pass_lenght.pack(padx=20, pady=20)

password = Entry(root, text="", font="Helvetica 25 bold", bd=4, relief=SUNKEN, bg="#d0d0d0")
password.pack(padx=20, pady=20)

f = Frame(root, bg="#242424")
f.pack(pady=15)

b1 = Button(f, text="Generate Password", font="Helvetica 12 bold", bg="#d0d0d0", relief=RAISED, bd=5, command=generate)
b1.grid(row=0, column=0,padx=30)


b2 = Button(f, text="Copy Password", font="Helvetica 12 bold", bg="#d0d0d0", relief=RAISED, bd=5, command=copy)
b2.grid(row=0, column=1,padx=30)

root.mainloop()
