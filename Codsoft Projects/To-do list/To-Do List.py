from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.wm_iconbitmap("icon.ico")
root.title("To-do list")
root.geometry("400x580")
root.resizable(False,False)
root.configure(bg="black")

task_list = []

def task_done():
    listbox.itemconfig(listbox.curselection(), fg="#ffffff")

def delete_task():
    global task_list
    t = str(listbox.get(ANCHOR))
    if t in task_list:
        task_list.remove(t)
        with open("task_list","w") as taskfile:
            for t in task_list:
                taskfile.write(t+"\n")
        listbox.delete(ANCHOR)
def add_task():
    t = task_entry.get()
    task_entry.delete(0, END)

    if t:
        with open("task_list","a") as taskfile:
            taskfile.write(f"\n{t}")
        task_list.append(t)
        listbox.insert(END,t)

def openTaskFile():
    try:
        global task_list
        with open("task_list.txt","r") as taskfile:
            tasks = taskfile.readlines()

        for t in tasks:
            if t !="\n":
                task_list.append(t)
                listbox.insert(END,t)

    except:
        file = open("task_list","w")
        file.close()


Label(root, text="What's the Plan for Today?", width=25, height=2, font="lexend 15 bold", bg="#222222", fg="#ffffff").place(x=30,y=20)


photo1 = Image.open("Top1.png")
resized = photo1.resize((50,50),Image.LANCZOS)
photo2 = ImageTk.PhotoImage(resized)
Label(root, image=photo2, bg="#222222").place(x=320,y=20)

frame1 = Frame(root, width=392, height=50, bg="#ffffff")
frame1.place(x=4,y=100)

task = StringVar()
task_entry = Entry(frame1, text="", width=19, font="ariel 20 bold", bg="#ffffff", bd=0)
task_entry.place(x=6,y=7)
task_entry.focus()

button = Button(frame1, text="ADD", font="couriernew 20 bold", width=6, bg="#5a95ff", fg="#ffffff", bd=0,command=add_task)
button.place(x=300,y=0)

frame2 = Frame(root, width=700, height=280, bg="#333333", bd=3)
frame2.pack(pady=(160,0))

listbox = Listbox(frame2, font="comicsanms 12 bold", width=40, height=16, bg="#32405b", fg="white", cursor="hand2")
listbox.pack(side=LEFT, fill=BOTH , padx=2)
scroolbar = Scrollbar(frame2)
scroolbar.pack(side=RIGHT, fill=BOTH)

listbox.config(yscrollcommand=scroolbar.set)
scroolbar.config(command=listbox.yview())

openTaskFile()

delete = Image.open("delete.jpg")
resized1 = delete.resize((50,50),Image.LANCZOS)
delete2 = ImageTk.PhotoImage(resized1)
Button(root,image=delete2,bg="#111111", bd=0, command=delete_task).place(x=170,y=510)

root.mainloop()