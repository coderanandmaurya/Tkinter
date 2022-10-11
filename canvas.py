from tkinter import *

root=Tk()

canvas_width = 400
canvas_height= 400

root.geometry(f"{canvas_height}x{canvas_width}")
can_width=Canvas(root,width=canvas_width,height=canvas_height)
can_width.pack()

# the line goes from x1 y1 to x2 y2
can_width.create_line(0,000,400,400,fill="red")
can_width.create_line(000,400,400,00,fill="red")

#to create rectangle  specify parameter in this order = coors of the top left
can_width.create_rectangle(300,200 ,50,100,fill="blue")

#
can_width.create_text(200,300,text="python")

# create oval
can_width.create_oval(200,200,50,100,fill="green")

root.mainloop()