from tkinter import *

G=Tk()
G.geometry("200x200")

frame = Frame(G, borderwidth=4,bg="blue",relief=SUNKEN)
frame.pack(anchor="ne",fill=X,side=TOP)

def name():
    print("hello")

b1=Button(frame,fg="red",text="print name", command=name)
b1.pack(side=LEFT,padx=10)

b2=Button(frame,fg="red",text="name")
b2.pack(side=RIGHT,padx=10)

b3=Button(frame,fg="red",text="click here")
b3.pack()




G.mainloop()