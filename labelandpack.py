from tkinter import *

root=Tk()

root.geometry("544x533")
root.title("My gui")

# important label option
# text = adds the text
# bd= background
# fg = foreground
# font = sets the sfont 1. font=("Helvetica" ,19,"bold") 2.
# padx = x padding
# pady = y padding
# relief = border styling = sunken(mota border) , raised groove, ridge

title_label = Label(text="""Bellis perennis, 
the daisy, is a European species 
of the family Asteraceae,
often considered the archetypal 
species of the name daisy. """,bg="red", fg="blue",pady=115,font="Helvetica 19 bold",borderwidth=15, relief=SUNKEN)

# important pack options
# anchor:
#title_label.pack(anchor=NE)
# title_label.pack(anchor="ne")
# title_label.pack(anchor="se")
# fill
#pad x
#Pad y

title_label.pack(anchor="sw",side=BOTTOM,fill=X,padx=12)

title_label.pack()





root.mainloop()