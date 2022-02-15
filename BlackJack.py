from random import shuffle
from carte import *
from tkinter import *
from PIL import Image, ImageTk
class BlackJack:
    def __init__(self, paquetA, paquetB):
        self.paquet1=paquetA
        self.paquet2=paquetB
    
    def blackjack(self):
        """Le but du blackjack est de battre le dealer.
        Pour le battre il faut arriver à etre le plus proche de 21 sans avoir plus.
        Si le dealer a moins que vous ou depasse 21 vous gagnez.\n
        RAPPEL:\n
            - Si vous obtenez 21 en recevant les cartes, vous gagnez.
            - Un As peut valoir 1, 10, ou 11"""
        vouloir="True"
        gagne=0
        perdu =False
        while vouloir=="True":
            shuffle(self.paquet1.contenu)
            shuffle(self.paquet2.contenu)
            total_D=0
            total_J=0
            bet=int(input("Combien voulez vous mettre sur la table? [$] "))
            carte_J=[self.paquet1.getCarteAt(0),self.paquet1.getCarteAt(1)]
            carte_D=[self.paquet2.getCarteAt(0),self.paquet2.getCarteAt(1)]
            
            print("Vous avez {} de {}, et {} de {}".format(carte_J[0].getNom(), carte_J[0].getCouleur(),
                                                           carte_J[1].getNom(), carte_J[1].getCouleur()))
            
            total_J=valeur_de_carte(carte_J[0].Valeur)+valeur_de_carte(carte_J[1].Valeur)
            total_D=total_D+valeur_de_carte_D(carte_D[0].Valeur, 0)
            total_D=total_D+valeur_de_carte_D(carte_D[1].Valeur, total_D)
            if total_J>21:
                gagne=gagne-bet
                print("Vous avez perdu ${}, le Dealer l'emporte.".format(bet))
            pioche=input("Vous avez {}, voulez vous piocher une nouvelle carte? [True/False] ".format(total_J))
            Ij=2
            while pioche=="True" and total_J<22:
                carte_J.append(self.paquet1.getCarteAt(Ij))
                print("Vous avez pioché {} de {}.".format(carte_J[-1].getNom(), carte_J[-1].getCouleur()))
                total_J=total_J+valeur_de_carte(carte_J[-1].Valeur)
                print("Votre total est {}".format(total_J))
                if total_J>21:
                    pioche="False"
                    perdu=True
                else:
                    pioche=input("Vous avez {}, voulez vous piocher encore? [True/False] ".format(total_J))
                    Ij=Ij+1
                
            
            Id=2
            while total_D<total_J and total_D<22 and not perdu:
                print("Le dealer a {} de {}, et {} de {}, son total {}".format(carte_D[0].getNom(), carte_D[0].getCouleur(),
                                                           carte_D[1].getNom(), carte_D[1].getCouleur(), total_D))
                carte_D.append(self.paquet2.getCarteAt(Id))
                print("Le dealer a pioché {} de {}.".format(carte_D[-1].getNom(), carte_D[-1].getCouleur()))
                total_D=total_D+valeur_de_carte_D(carte_D[-1].Valeur, total_D)
                Id=Id+1
                
            if total_D >21:
                print(f"Vous avez gagné ${bet}")
                gagne=gagne+bet
            elif total_D<total_J and total_J<=21:
                print(f"Vous avez gagné ${bet}")
                gagne=gagne+bet
            elif total_D ==total_J:
                print("C'est une égalité.")
            else:
                print(f"Le Dealer a gagné, vous avez perdu ${bet}")
                gagne=gagne-bet
            print(f"Votre total s'élève à ${gagne}")
            vouloir=input("Voulez vous continuer à jouer? [True/False] ")
            
        print(f"Vous repartez avec ${gagne}")

def valeur_de_carte(valeur):
    if valeur>10 and valeur <14:
        return 10
    elif valeur==1:
        nb=int(input("Voulez vous que l'As valle 1, 10, ou 11?"))
        return nb
    else:
        return valeur
    
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



'''class GraphicInterfaceBlackJack:
    def __init__(self):
        root = Tk()

        root.title("BlackJack")
        Username="Bismaon"
        root.attributes("-fullscreen", True)
        rows = 0
        while rows < 50:
            root.rowconfigure(rows, weight=1)
            root.columnconfigure(rows,weight=1)
            rows += 1
        L_Dealer = Label(root, text="Dealer", font="Arial 17 bold").grid(row=2, column =24)
        L_Joueur= Label(root, text=Username, font="Arial 17 bold").grid(row=24, column=24)
        L_Total_D=Label(root, text="Total du Dealer: ",font="Arial 12 bold").grid(row=2, column=26)
        L_Total_J=Label(root, text="Total du Joueur: ",font="Arial 12 bold").grid(row=24, column=26)
        L_Mis_en_jeu=Label(root, text="Argent en jeu:", font="Arial 12 bold").grid(row=24, column=2)
        L_Argent_J=Label(root, text="Argent gagné/perdu par le Joueur: ", font="Arial 12 bold").grid(row=25, column=2)
        L_Argent_D=Label(root, text="Argent gagné/perdu par le dealer: ",font="Arial 12 bold").grid(row=2, column=2)
        Pioche = Button(root, text="Pioche", font="Arial 13 bold", relief=RAISED).grid(row=48, column=24)
        Sortir=Button(root, text="Exit", font="Arial 12 bold", relief=RAISED, command=root.destroy).grid(row=48, column=48)
        root.mainloop()
        
    def add_image(self, card):'''
        
       