import os
from tkinter import Label, Tk, Button, RAISED
from PIL import Image, ImageTk
from carte import Carte, PaquetDeCarte
coeur={1:"Carte\\ace_of_hearts.png",
       2:"Carte\\2_of_hearts.png",
       3:"Carte\\3_of_hearts.png",
       4:"Carte\\4_of_hearts.png",
       5:"Carte\\5_of_hearts.png",
       6:"Carte\\6_of_hearts.png",
       7:"Carte\\7_of_hearts.png",
       8:"Carte\\8_of_hearts.png",
       9:"Carte\\9_of_hearts.png",
       10:"Carte\\10_of_hearts.png",
       11:"Carte\\jack_of_hearts2.png",
       12:"Carte\\queen_of_hearts2.png",
       13:"Carte\\king_of_hearts2.png"}
trefle={1:"Carte\\ace_of_clubs.png",
       2:"Carte\\2_of_clubs.png",
       3:"Carte\\3_of_clubs.png",
       4:"Carte\\4_of_clubs.png",
       5:"Carte\\5_of_clubs.png",
       6:"Carte\\6_of_clubs.png",
       7:"Carte\\7_of_clubs.png",
       8:"Carte\\8_of_clubs.png",
       9:"Carte\\9_of_clubs.png",
       10:"Carte\\10_of_clubs.png",
       11:"Carte\\jack_of_clubs2.png",
       12:"Carte\\queen_of_clubs2.png",
       13:"Carte\\king_of_clubs2.png"}
carreau={1:"Carte\\ace_of_diamonds.png",
       2:"Carte\\2_of_diamonds.png",
       3:"Carte\\3_of_diamonds.png",
       4:"Carte\\4_of_diamonds.png",
       5:"Carte\\5_of_diamonds.png",
       6:"Carte\\6_of_diamonds.png",
       7:"Carte\\7_of_diamonds.png",
       8:"Carte\\8_of_diamonds.png",
       9:"Carte\\9_of_diamonds.png",
       10:"Carte\\10_of_diamonds.png",
       11:"Carte\\jack_of_diamonds2.png",
       12:"Carte\\queen_of_diamonds2.png",
       13:"Carte\\king_of_diamonds2.png"}
pique={1:"Carte\\ace_of_spades.png",
       2:"Carte\\2_of_spades.png",
       3:"Carte\\3_of_spades.png",
       4:"Carte\\4_of_spades.png",
       5:"Carte\\5_of_spades.png",
       6:"Carte\\6_of_spades.png",
       7:"Carte\\7_of_spades.png",
       8:"Carte\\8_of_spades.png",
       9:"Carte\\9_of_spades.png",
       10:"Carte\\10_of_spades.png",
       11:"Carte\\jack_of_spades2.png",
       12:"Carte\\queen_of_spades2.png",
       13:"Carte\\king_of_spades2.png"}
dico_carte={"coeur":coeur, "trefle":trefle, "carreau":carreau, "pique":pique}
card=Carte(1, 1)
n_card=0
def add_image_J():
    global card, n_card, dico_carte, coeur, trefle, carreau, pique
    image = Image.open(os.path.join(os.path.dirname(os.path.abspath(__file__)), dico_carte[card.get_couleur][card.valeur]))
    size=image.size
    resize_image = image.resize((size[0]//4, size[1]//4))
    img = ImageTk.PhotoImage(resize_image)
    img_lab=Label(image=img)
    img_lab.image = img # keep a reference!
    img_lab.place(x=544+(50*n_card),y=100)
    n_card+=1
    return img_lab

root = Tk()
root.title("BlackJack")
username="Bismaon"
root.attributes("-fullscreen", True)
ROWS = 0
while ROWS < 50:
    root.rowconfigure(ROWS, weight=1)
    root.columnconfigure(ROWS,weight=1)
    ROWS += 1
def disable():
    for widgets in root.winfo_children():
        if isinstance(widgets, Button):
            widgets['state']='disabled'
L_Dealer = Label(root,
                 text="Dealer",
                 font="Arial 17 bold").grid(row=2,
                                            column =24)
l_joueur= Label(root, text=username, font="Arial 17 bold")
l_joueur.grid(row=28, column=24)
l_total_d=Label(root, text="Total du Dealer: ",font="Arial 12 bold")
l_total_d.grid(row=2, column=26)
l_total_j=Label(root, text="Total du Joueur: ",font="Arial 12 bold")
l_total_j.grid(row=28, column=26)
l_mis_en_jeu=Label(root, text="Argent en jeu:", font="Arial 12 bold")
l_mis_en_jeu.grid(row=28, column=2)
l_argent_j=Label(root, text="Argent gagné/perdu par le Joueur: ", font="Arial 12 bold")
l_argent_j.grid(row=29, column=2)
l_argent_d=Label(root, text="Argent gagné/perdu par le dealer: ", font="Arial 12 bold")
l_argent_d.grid(row=2, column=2)
pioche = Button(root, text="Pioche", font="Arial 13 bold", relief=RAISED, command=add_image_J)
pioche.grid(row=48, column=24)
arret_p=Button(root, text="Terminé", font ="Arial 12 bold", relief =RAISED, command=disable)
arret_p.grid(row=48, column =23)
sortir=Button(root, text="Exit", font="Arial 12 bold", relief=RAISED, command=root.destroy)
sortir.grid(row=48, column=48)

root.mainloop()

# Read the Image
#image = Image.open( "Carte\\2_of_clubs.png")
#size=image.size
# Resize the image using resize() method
#resize_image = image.resize((size[0]//3, size[1]//3))

#img = ImageTk.PhotoImage(resize_image)

# create label and add resize image
#label1 = Label(image=img)
#label1.image = img
#label1.pack()
# Execute Tkinter
#root.mainloop()
