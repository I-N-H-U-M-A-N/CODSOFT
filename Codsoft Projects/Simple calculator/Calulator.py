from tkinter import *

root =Tk()

root.geometry("450x605")
root.wm_iconbitmap("calculator1.ico")
root.title("Calculator")
root.resizable(False,False)
root.configure(bg="#222222")

x=""
def show(value):
    global x
    x+=value
    result.config(text=x)

def clear():
    global x
    x=""
    result.config(text=x)

def calculate():
    global x
    r=""
    if x!="":
        try:
            r=eval(x)
        except:
            r="ERROR"
            x=""
    result.config(text=r)

result = Label(root, text="0", width=20, height=2, font="ariel 30 bold", bg="#222222", fg="#ffffff", relief=SUNKEN, bd="5")
result.pack(padx=5, pady=8)

Button(root, text="C", width=4, height=1, font="ariel 30", bd=1, fg="#ffffff", bg="#3697f5", command=lambda: clear()).place(x=8,y=120)
Button(root, text="(", width=4, height=1, font="ariel 30", bd=1, fg="#ffffff", bg="#333333", command=lambda: show("(")).place(x=120,y=120)
Button(root, text=")", width=4, height=1, font="ariel 30", bd=1, fg="#ffffff", bg="#333333", command=lambda: show(")")).place(x=232,y=120)
Button(root, text="/", width=4, height=1, font="ariel 30", bd=1, fg="#ffffff", bg="#333333", command=lambda: show("/")).place(x=343,y=120)

Button(root, text="7", width=4, height=1, font="ariel 30", bd=1, fg="#ffffff", bg="#444444", command=lambda: show("7")).place(x=8,y=220)
Button(root, text="8", width=4, height=1, font="ariel 30", bd=1, fg="#ffffff", bg="#444444", command=lambda: show("8")).place(x=120,y=220)
Button(root, text="9", width=4, height=1, font="ariel 30", bd=1, fg="#ffffff", bg="#444444", command=lambda: show("9")).place(x=232,y=220)
Button(root, text="*", width=4, height=1, font="ariel 30", bd=1, fg="#ffffff", bg="#333333", command=lambda: show("*")).place(x=343,y=220)

Button(root, text="4", width=4, height=1, font="ariel 30", bd=1, fg="#ffffff", bg="#444444", command=lambda: show("4")).place(x=8,y=320)
Button(root, text="5", width=4, height=1, font="ariel 30", bd=1, fg="#ffffff", bg="#444444", command=lambda: show("5")).place(x=120,y=320)
Button(root, text="6", width=4, height=1, font="ariel 30", bd=1, fg="#ffffff", bg="#444444", command=lambda: show("6")).place(x=232,y=320)
Button(root, text="-", width=4, height=1, font="ariel 30", bd=1, fg="#ffffff", bg="#333333", command=lambda: show("-")).place(x=343,y=320)

Button(root, text="1", width=4, height=1, font="ariel 30", bd=1, fg="#ffffff", bg="#444444", command=lambda: show("1")).place(x=8,y=420)
Button(root, text="2", width=4, height=1, font="ariel 30", bd=1, fg="#ffffff", bg="#444444", command=lambda: show("2")).place(x=120,y=420)
Button(root, text="3", width=4, height=1, font="ariel 30", bd=1, fg="#ffffff", bg="#444444", command=lambda: show("3")).place(x=232,y=420)
Button(root, text="+", width=4, height=1, font="ariel 30", bd=1, fg="#ffffff", bg="#333333", command=lambda: show("+")).place(x=343,y=420)

Button(root, text=".", width=4, height=1, font="ariel 30", bd=1, fg="#ffffff", bg="#333333", command=lambda: show(".")).place(x=8,y=520)
Button(root, text="0", width=4, height=1, font="ariel 30", bd=1, fg="#ffffff", bg="#444444", command=lambda: show("0")).place(x=120,y=520)
Button(root, text="=", width=9, height=1, font="ariel 30", bd=1, fg="#ffffff", bg="#fe9037", command=lambda: calculate()).place(x=232,y=520)

root.mainloop()