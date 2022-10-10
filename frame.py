from tkinter import *

zero=Tk()

zero.geometry("400x200")

f1= Frame(zero,bg="grey",borderwidth=1,relief=SUNKEN)

f1.pack(side=LEFT,fill=Y)

f2= Frame(zero,bg="Blue",borderwidth=2,relief=SUNKEN)

f2.pack(side=TOP,fill=X)

l1=Label(f1,text="Project Tkinter- Pycharm")
l1.pack(pady=42)

l2=Label(f2,text="Only title here",font="Helvetica",fg="red",bg="black")
l2.pack()




zero.mainloop()