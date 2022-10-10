from tkinter import *

root =Tk()

def getval():
    print("it works")


root.geometry("290x250")

Label(root, text= "Welcome to travels",font="comicsansms 13 bold").grid(row=0,columns=4)
name=Label(root, text="name")
phone=Label(root,text="phone")
gender=Label(root,text="gender")
Emergency=Label(root,text="Emergency Contact")
paymentMode= Label(root, text="Payment Mode")

name.grid(row=1,column=0)
phone.grid(row=2,column=0)
gender.grid(row=3,column=0)
Emergency.grid(row=4,column=0)
paymentMode.grid(row=5,column=0)

namevalue= StringVar()
phonevalue= StringVar()
gendervalue= StringVar()
emergencyvalue= StringVar()
paymentvalue= StringVar()
foodservicevalue = StringVar()

nameentry=Entry(root,textvariable=namevalue)
phoneentry=Entry(root,textvariable=phonevalue)
genderentry=Entry(root,textvariable=emergencyvalue)
emergencyentry=Entry(root,textvariable=emergencyvalue)
paymententry=Entry(root,textvariable=paymentvalue)

nameentry.grid(row=1,column=1)
phoneentry.grid(row=2,column=1)
genderentry.grid(row=3,column=1)
emergencyentry.grid(row=4,column=1)
paymententry.grid(row=5,column=1)

# checkbox
foodservice = Checkbutton(text= "want to prebook your meal",variable=foodservicevalue)
foodservice.grid(row=7,column=1)

#button &packing it and assigning it a commmand
Button(text="submit to travel",command=getval).grid(row=8,column=1)


root.mainloop()
