from random import shuffle
from carte import *
from tkinter import *
from PIL import Image, ImageTk
import os

class BlackJack:
    def __init__(self, paquetA, paquetB, username:str):
        self.paquet1=paquetA
        self.paquet2=paquetB
        self.monnaie=0
        self.username=username
        self.Carte_J=[]
        self.Carte_D=[]
        self.indice_J=2
        self.indice_D=2
        self.total_J=0
        self.total_D=0
        self.bet=0
    
    
    def window(self):
        root = Tk()
        root.title("BlackJack")
        root.attributes("-fullscreen", True)
        rows = 0
        while rows < 50:
            root.rowconfigure(rows, weight=1)
            root.columnconfigure(rows,weight=1)
            rows += 1
        L_Dealer = Label(root, text="Dealer", font="Arial 17 bold")
        L_Dealer.grid(row=2, column =24)
        L_Joueur= Label(root, text=self.username, font="Arial 17 bold")
        L_Joueur.grid(row=24, column=24)
        L_total_D=Label(root, text="Total du Dealer: ",font="Arial 12 bold")
        L_total_D.grid(row=2, column=26)
        L_total_J=Label(root, text="Total du Joueur: ",font="Arial 12 bold")
        L_total_J.grid(row=24, column=26)
        L_Mis_en_jeu=Label(root, text=f"Argent en jeu: ${self.bet}", font="Arial 12 bold")
        L_Mis_en_jeu.grid(row=24, column=2)
        L_Argent_J=Label(root, text=f"Argent gagné/perdu par le Joueur: {self.monnaie}", font="Arial 12 bold")
        L_Argent_J.grid(row=25, column=2)
        Pioche = Button(root, text="Pioche", font="Arial 13 bold", relief=RAISED, command=self.piocher)
        Pioche.grid(row=48, column=24)
        Arret_P=Button(root, text="Terminé", font ="Arial 12 bold", relief =RAISED, command=self.dealer_stuff)
        Arret_P.grid(row=48, column =23)
        Sortir=Button(root, text="Exit", font="Arial 12 bold", relief=RAISED, command=root.destroy)
        Sortir.grid(row=48, column=48)
        reset=Button(root, text="Reset", font="Arial 12 bold", relief=RAISED, command=self.reinit)
        reset.grid(row=48, column=45)
        root.mainloop()
    
    
    @staticmethod
    def valeur_de_carte_J(card_value):
        global root
        if card_value>10 and card_value <14:
            return 10
        elif card_value==1:
            nb=Entry(root)
            nb.place(x=100, y=100)
            nb.focus_set()
            valeur=IntVar()
            answer_nb=Label(root, text='')
            answer_nb.place(x=0,y=0)
            def get_value():
                if not (int(nb.get())==10 or int(nb.get())==1 or int(nb.get())==11):
                    answer_nb.config(text="la valeur doit etre 1, 10, ou 11!")
                else:
                    valeur.set(nb.get())
            B_nb=Button(root, text="Valeur de l'As (1, 10, 11): ", command=get_value, font="Arial 12 bold", relief=RAISED)
            B_nb.place(x=50, y=50)
            root.wait_variable(valeur)
            return valeur.get()
        else:
            return card_value
    
    @staticmethod
    def valeur_de_carte_D(valeur, total):
        if valeur>10 and valeur <14:
            return 10
        elif valeur ==1:
            if total>11:
                return 1
            elif total ==11:
                return 10
            else:
                return 11
        else:
            return valeur
    
    def add_image_D(self):
        image = Image.open(os.path.join(os.path.dirname(os.path.abspath(__file__)), dico_carte[
            self.Carte_D[-1].getCouleur()][self.Carte_D[-1].Valeur]))
        size=image.size
        resize_image = image.resize((size[0]//4, size[1]//4))
        img = ImageTk.PhotoImage(resize_image)
        img_lab=Label(image=img)
        img_lab.image = img # keep a reference!
        img_lab.place(x=544+(50*(len(self.Carte_D)-1)),y=100)
        return img_lab
    
    def add_image_J(self):
        image = Image.open(os.path.join(os.path.dirname(os.path.abspath(__file__)), dico_carte[
            self.Carte_J[-1].getCouleur()][self.Carte_J[-1].Valeur]))
        size=image.size
        resize_image = image.resize((size[0]//4, size[1]//4))
        img = ImageTk.PhotoImage(resize_image)
        img_lab=Label(image=img)
        img_lab.image = img # keep a reference!
        img_lab.place(x=544+(50*(len(self.Carte_J)-1)),y=450)
        return img_lab
    
    def reinit(self):
        pass
    
    def piocher(self):
        self.Carte_J.append(self.paquet1.getCarteAt(self.indice_J))
        self.total_J=self.total_J+int(self.valeur_de_carte_J(self.Carte_J[-1].Valeur))
        self.indice_J=self.indice_J+1
        self.add_image_J()
                
    def dealer_stuff(self):
        pass
    
    def blackjack(self):
        """Le but du blackjack est de battre le dealer.
        Pour le battre il faut arriver à etre le plus proche de 21 sans avoir plus.
        Si le dealer a moins que vous ou depasse 21 vous self.monnaiez.\n
        RAPPEL:\n
            - Si vous obtenez 21 en recevant les cartes, vous self.monnaiez.
            - Un As peut valoir 1, 10, ou 11"""
        vouloir="True"
        perdu=False
        while vouloir=="True":
            self.total_D,self.total_J= 0, 0
            shuffle(self.paquet1.contenu)
            shuffle(self.paquet2.contenu)
            self.Carte_J, self.Carte_D =[self.paquet1.getCarteAt(0),self.paquet1.getCarteAt(1)],[self.paquet2.getCarteAt(0),self.paquet2.getCarteAt(1)]
            
            self.bet=int(input("Combien voulez vous mettre sur la table? [$] ")) #mettre un entry
            
            self.total_J=self.valeur_de_carte_J(self.Carte_J[0].Valeur)+self.valeur_de_carte_J(self.Carte_J[1].Valeur)#changer le total sur la fenete tkinter
            self.total_D=self.total_D+self.valeur_de_carte_D(self.Carte_D[0].Valeur, 0)
            self.total_D=self.total_D+self.valeur_de_carte_D(self.Carte_D[1].Valeur, self.total_D)#changer le total sur la fenete tkinter
            if self.total_J>21:
                self.monnaie=self.monnaie-self.bet
                print("Vous avez perdu ${}, le Dealer l'emporte.".format(self.bet))#Changer l'argent gagne, mettre le bet a 0 et pop up pour recommencer ou non
            pioche=input("Vous avez {}, voulez vous piocher une nouvelle carte? [True/False] ".format(self.total_J))#changer le total sur la fenete tkinter
            while pioche=="True" and self.total_J<22:
                self.Carte_J.append(self.paquet1.getCarteAt(self.indice_J))
                print("Vous avez pioché {} de {}.".format(self.Carte_J[-1].getNom(), self.Carte_J[-1].getCouleur()))
                self.total_J=self.total_J+self.valeur_de_self.Carte_J(self.Carte_J[-1].Valeur)
                print("Votre total est {}".format(self.total_J))
                if self.total_J>21:
                    pioche="False"
                    perdu=True
                else:
                    pioche=input("Vous avez {}, voulez vous piocher encore? [True/False] ".format(self.total_J))
                    Ij=Ij+1
                    
            Id=2
            while self.total_D<self.total_J and self.total_D<22 and not perdu:
                print("Le dealer a {} de {}, et {} de {}, son total {}".format(self.Carte_D[0].getNom(), self.Carte_D[0].getCouleur(),
                                                           self.Carte_D[1].getNom(), self.Carte_D[1].getCouleur(), self.total_D))
                self.Carte_D.append(self.paquet2.getCarteAt(Id))
                print("Le dealer a pioché {} de {}.".format(self.Carte_D[-1].getNom(), self.Carte_D[-1].getCouleur()))
                self.total_D=self.total_D+self.valeur_de_carte_D(self.Carte_D[-1].Valeur,self.total_D)
                Id=Id+1
                
            if self.total_D >21:
                print(f"Vous avez gagné ${self.bet}")
                self.monnaie=self.monnaie+self.bet
            elif self.total_D<self.total_J and self.total_J<=21:
                print(f"Vous avez gagné ${self.bet}")
                self.monnaie=self.monnaie+self.bet
            elif self.total_D ==self.total_J:
                print("C'est une égalité.")
            else:
                print(f"Le Dealer a gagné, vous avez perdu ${self.bet}")
                self.monnaie=self.monnaie-self.bet
            print(f"Votre total s'élève à ${self.monnaie}")
            vouloir=input("Voulez vous continuer à jouer? [True/False] ")
            
        print(f"Vous repartez avec ${self.monnaie}")
    
    def window(self):
        global root
        root.title("BlackJack")
        root.attributes("-fullscreen", True)
        rows = 0
        while rows < 50:
            root.rowconfigure(rows, weight=1)
            root.columnconfigure(rows,weight=1)
            rows += 1
        L_Dealer = Label(root, text="Dealer", font="Arial 17 bold")
        L_Dealer.grid(row=2, column =24)
        L_Joueur= Label(root, text=self.username, font="Arial 17 bold")
        L_Joueur.grid(row=24, column=24)
        L_total_D=Label(root, text="Total du Dealer: ",font="Arial 12 bold")
        L_total_D.grid(row=2, column=26)
        L_total_J=Label(root, text="Total du Joueur: ",font="Arial 12 bold")
        L_total_J.grid(row=24, column=26)
        L_Mis_en_jeu=Label(root, text=f"Argent en jeu: ${self.bet}", font="Arial 12 bold")
        L_Mis_en_jeu.grid(row=24, column=2)
        L_Argent_J=Label(root, text=f"Argent gagné/perdu par le Joueur: {self.monnaie}", font="Arial 12 bold")
        L_Argent_J.grid(row=25, column=2)
        Pioche = Button(root, text="Pioche", font="Arial 13 bold", relief=RAISED, command=self.piocher)
        Pioche.grid(row=48, column=24)
        Arret_P=Button(root, text="Terminé", font ="Arial 12 bold", relief =RAISED, command=self.dealer_stuff)
        Arret_P.grid(row=48, column =23)
        Sortir=Button(root, text="Exit", font="Arial 12 bold", relief=RAISED, command=root.destroy)
        Sortir.grid(row=48, column=48)
        reset=Button(root, text="Reset", font="Arial 12 bold", relief=RAISED, command=self.reinit)
        reset.grid(row=48, column=45)
        root.mainloop()


################################################################################################
#Storage des cartes
root = Tk()
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