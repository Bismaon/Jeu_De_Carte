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

coeur={1:"Jeu_De_Carte\\Carte\\ace_of_hearts.png", 
       2:"Jeu_De_Carte\\Carte\\2_of_hearts.png", 
       3:"Jeu_De_Carte\\Carte\\3_of_hearts.png", 
       4:"Jeu_De_Carte\\Carte\\4_of_hearts.png", 
       5:"Jeu_De_Carte\\Carte\\5_of_hearts.png", 
       6:"Jeu_De_Carte\\Carte\\6_of_hearts.png", 
       7:"Jeu_De_Carte\\Carte\\7_of_hearts.png", 
       8:"Jeu_De_Carte\\Carte\\8_of_hearts.png", 
       9:"Jeu_De_Carte\\Carte\\9_of_hearts.png", 
       10:"Jeu_De_Carte\\Carte\\10_of_hearts.png", 
       11:"Jeu_De_Carte\\Carte\\jack_of_hearts2.png", 
       12:"Jeu_De_Carte\\Carte\\queen_of_hearts2.png", 
       13:"Jeu_De_Carte\\Carte\\king_of_hearts2.png"}
trefle={1:"Jeu_De_Carte\\Carte\\ace_of_clubs.png", 
       2:"Jeu_De_Carte\\Carte\\2_of_clubs.png", 
       3:"Jeu_De_Carte\\Carte\\3_of_clubs.png", 
       4:"Jeu_De_Carte\\Carte\\4_of_clubs.png", 
       5:"Jeu_De_Carte\\Carte\\5_of_clubs.png", 
       6:"Jeu_De_Carte\\Carte\\6_of_clubs.png", 
       7:"Jeu_De_Carte\\Carte\\7_of_clubs.png", 
       8:"Jeu_De_Carte\\Carte\\8_of_clubs.png", 
       9:"Jeu_De_Carte\\Carte\\9_of_clubs.png", 
       10:"Jeu_De_Carte\\Carte\\10_of_clubs.png", 
       11:"Jeu_De_Carte\\Carte\\jack_of_clubs2.png", 
       12:"Jeu_De_Carte\\Carte\\queen_of_clubs2.png", 
       13:"Jeu_De_Carte\\Carte\\king_of_clubs2.png"}
carreau={1:"Jeu_De_Carte\\Carte\\ace_of_diamonds.png", 
       2:"Jeu_De_Carte\\Carte\\2_of_diamonds.png", 
       3:"Jeu_De_Carte\\Carte\\3_of_diamonds.png", 
       4:"Jeu_De_Carte\\Carte\\4_of_diamonds.png", 
       5:"Jeu_De_Carte\\Carte\\5_of_diamonds.png", 
       6:"Jeu_De_Carte\\Carte\\6_of_diamonds.png", 
       7:"Jeu_De_Carte\\Carte\\7_of_diamonds.png", 
       8:"Jeu_De_Carte\\Carte\\8_of_diamonds.png", 
       9:"Jeu_De_Carte\\Carte\\9_of_diamonds.png", 
       10:"Jeu_De_Carte\\Carte\\10_of_diamonds.png", 
       11:"Jeu_De_Carte\\Carte\\jack_of_diamonds2.png", 
       12:"Jeu_De_Carte\\Carte\\queen_of_diamonds2.png", 
       13:"Jeu_De_Carte\\Carte\\king_of_diamonds2.png"}
pique={1:"Jeu_De_Carte\\Carte\\ace_of_spades.png", 
       2:"Jeu_De_Carte\\Carte\\2_of_spades.png", 
       3:"Jeu_De_Carte\\Carte\\3_of_spades.png", 
       4:"Jeu_De_Carte\\Carte\\4_of_spades.png", 
       5:"Jeu_De_Carte\\Carte\\5_of_spades.png", 
       6:"Jeu_De_Carte\\Carte\\6_of_spades.png", 
       7:"Jeu_De_Carte\\Carte\\7_of_spades.png", 
       8:"Jeu_De_Carte\\Carte\\8_of_spades.png", 
       9:"Jeu_De_Carte\\Carte\\9_of_spades.png", 
       10:"Jeu_De_Carte\\Carte\\10_of_spades.png", 
       11:"Jeu_De_Carte\\Carte\\jack_of_spades2.png", 
       12:"Jeu_De_Carte\\Carte\\queen_of_spades2.png", 
       13:"Jeu_De_Carte\\Carte\\king_of_spades2.png"}
dico_carte={"coeur":coeur, "trefle":trefle, "carreau":carreau, "pique":pique}

'''class GraphicInterfaceBlackJack:
    def __init__(self):
        BJ_window=Tk()
        BJ_window.geometry("1920x1080")  
        
    def add_image(self, card):'''
        
       