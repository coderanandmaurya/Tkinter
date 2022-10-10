from tkinter import *
from PIL import Image, ImageTk

first_root=Tk()

#first_root.geometry("width x height")
first_root.geometry("644x344")

# for jpg images use PIL

image= Image.open("download.jpg")
photo=ImageTk.PhotoImage(image)
photo_label= Label(image=photo)
photo_label.pack()



first_root.mainloop()





