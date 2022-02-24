from random import shuffle
from carte import *
###To do list:
#    - make it visual
#    - have interaction with the user
#    - be able to choose which game one wnats to play, black, or bataille
class Bataille:
    def __init__(self, paquet1:list, paquet2:list):
        self.jeu1=paquet1
        self.jeu2=paquet2

    def bataille(self):
        """Tapez ENTER pour tirer une carte et commencer la bataille.\n
        RAPPEL:\n
            - Les cartes sont tirer en meme temps
            - trefles < carreau < coeur < pique"""
        v_couleur={'trefle':1, 'carreau':2, 'coeur':3, 'pique':4}
        j1=0
        j2=0
        tour=0
        shuffle(self.jeu1)
        shuffle(self.jeu2)
        while len(self.jeu1.contenu)!=0 and len(self.jeu2.contenu)!=0:
            tour+=1
            if j1>=len(self.jeu1.contenu):
                j1=0
            if j2>=len(self.jeu2.contenu):
                j2=0
            carte1=self.jeu1.getCarteAt(j1)
            carte2=self.jeu2.getCarteAt(j2)
            input(f'{carte1.getNom()} de {carte1.getCouleur()} contre {carte2.getNom()} de {carte2.getCouleur()}')
            if carte1.Valeur>carte2.Valeur:
                input(f"J1: {carte1.getNom()} de {carte1.getCouleur()} l'emporte!")
                self.jeu2.contenu.append(carte1)
                self.jeu1.contenu.pop(j1)
                j2+=1
            elif carte1.Valeur == carte2.Valeur:
                if v_couleur[carte1.getCouleur()]>v_couleur[carte2.getCouleur()]:
                    input(f"J1: {carte1.getNom()} de {carte1.getCouleur()} l'emporte!")
                    self.jeu2.contenu.append(carte1)
                    self.jeu1.contenu.pop(j1)
                    j2+=1
                elif v_couleur[carte1.getCouleur()]==v_couleur[carte2.getCouleur()]:
                    input("Egalité!")
                    j1+=1
                    j2+=1
                else:
                    input(f"J2: {carte2.getNom()} de {carte2.getCouleur()} l'emporte!")
                    self.jeu1.contenu.append(carte2)
                    self.jeu2.contenu.pop(j2)
                    j1+=1
            else:
                input(f"J2: {carte2.getNom()} de {carte2.getCouleur()} l'emporte!")
                self.jeu1.contenu.append(carte2)
                self.jeu2.contenu.pop(j2)
                j1+=1
            if tour>100:
                if len(self.jeu2.contenu)>len(self.jeu1.contenu):
                    print("Joueur Numero 2 a gagné!", len(self.jeu2.contenu))
                    return
                elif len(self.jeu1.contenu)==len(self.jeu2.contenu):
                    print("Egalité!")
                    return
                else:
                    print("Joueur Numero 1 a gagné!", len(self.jeu1.contenu))
                    return
        if len(self.jeu2.contenu)==0:
            print("Joueur Numero 1 a gagné!", tour)
        else:
            print("Joueur Numero 2 a gagné!", tour)