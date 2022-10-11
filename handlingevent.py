from tkinter import *

root = Tk()
root.title("event in Tkinter")
root.geometry("200x300")
def print1(event):
    print(f"hello {event.x},{event.y}")



widget = Button(root,text="click me")
widget.pack()

widget.bind('<Button-1>',print1)
widget.bind('<Double-1>',quit)

root.mainloop()