
from tkinter import *
from PIL import Image, ImageTk
import os

root = Tk()
width= root.winfo_screenwidth() 
height= root.winfo_screenheight()
#setting tkinter window size
root.geometry("%dx%d" % (width, height))
def func(): 
    label["text"] ="yo whats up g"

label = Label(root, text="yo man", font=20)
label.grid(row =3, column=5, columnspan=4)
button = Button(root, text="change text", command=func)
button.grid(row=3, column=3)
button1=Button(root, text="Exit", command=root.destroy )
button1.grid(row=5, column=2)
root.mainloop()
"""

# Read the Image
image = Image.open( "Jeu_De_Carte\\Carte\\2_of_clubs.png")
size=image.size
# Resize the image using resize() method
resize_image = image.resize((size[0]//3, size[1]//3))
 
img = ImageTk.PhotoImage(resize_image)
 
# create label and add resize image
label1 = Label(image=img)
label1.image = img
label1.pack()
# Execute Tkinter
root.mainloop()"""