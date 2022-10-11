from tkinter import *
from PIL import Image, ImageTk
import datetime as dt

def every_100(text):
    final_text =""
    for i in range(0,len(text)):
        final_text +=text[i]
        if i%60 ==0 and i!=0:
            final_text +="\n"
    return final_text


root = Tk()
root.geometry("600x600")
root.title("Quotes")


texts=[]
photos=[]
for i in range(0,3):
    with open(f"{i+1}.txt", encoding = 'utf-8') as f:
        text = f.read()
        texts.append(every_100(text))

    image = Image.open(f"{i+1}.png")
    #TODO: Resize these images
    image=image.resize((100,100),Image.ANTIALIAS)

    photos.append(ImageTk.PhotoImage(image))

f0 = Frame(root,width=800,height=700)
Label(f0,text="ANIME QUOTES",font="lucida 33 bold").pack()
date = dt.datetime.now()
# %A – Day of the week, full name
# %B – Full month name
# %d – Day of the month
# %Y – Year with century as a decimal number
Label(f0,text=f"{date:%A, %B %d, %Y}",font="lucida 15 bold").pack()

f0.pack()


for i in range(0,3):
    f1= Frame(root, width=900, height=200, pady=28)
    Label(f1, text=texts[i], padx=22, pady=22).pack(side="left")
    Label(f1, image=photos[i], anchor="e").pack()
    f1.pack(anchor="w")

root.mainloop()