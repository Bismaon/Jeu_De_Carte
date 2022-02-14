
from tkinter import *
from PIL import Image, ImageTk
import os



root = Tk()

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
root.mainloop()