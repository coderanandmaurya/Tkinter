from tkinter import *

def getval():
    print(uservalue.get())
    print(passvalue.get())

root = Tk()

root.geometry("500x400")

u = Label(root, text="username")
p = Label(root, text="password")

u.grid(row=0)
p.grid(row=1)

# variable class : boolean var,double var, intvar,stringvar

uservalue= StringVar()
passvalue = StringVar()

userentry = Entry(root, textvariable=uservalue )
passentry = Entry(root, textvariable=passvalue)

userentry.grid(row=0, column=1)
passentry.grid(row=1, column=1)

Button(text="Submit", command=getval).grid(row=3,column=1)


root.mainloop()