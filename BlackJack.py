from random import shuffle
from carte import *
from tkinter import *
from PIL import Image, ImageTk
import os
class BlackJack:
    def __init__(self, paquetA, paquetB):
        self.dico_carte={"coeur":{1:"Carte\\ace_of_hearts.png", 
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
                    13:"Carte\\king_of_hearts2.png"}, 
            "trefle":{1:"Carte\\ace_of_clubs.png", 
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
                    13:"Carte\\king_of_clubs2.png"}, 
            "carreau":{1:"Carte\\ace_of_diamonds.png", 
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
                    13:"Carte\\king_of_diamonds2.png"},
            "pique":{1:"Carte\\ace_of_spades.png", 
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
                    13:"Carte\\king_of_spades2.png"}}
        self.min_font:str="Arial 12 bold"
        self.max_font:str="Arial 17 bold"
        self.paquet1:PaquetDeCarte = paquetA
        self.paquet2:PaquetDeCarte = paquetB
        shuffle(self.paquet1.contenu)
        shuffle(self.paquet2.contenu)
        self.monnaie:str = '0'
        self.rows:int = 0
        self.keep:bool=False
        self.Carte_J:list[Carte] = []
        self.Carte_D:list[Carte] = []
        self.indice_J:int = 0
        self.indice_D:int = 0
        self.total_J:int = 0
        self.total_D:int = 0
        self.bet:int = 0
        self.username:str = ''
        self.root:Tk = Tk()
        self.root.title("BlackJack")
        self.root.attributes("-fullscreen", True)
        self.root.configure(bg='#f0f0c8')
        self.B_regle:Button=Button(self.root, 
                                   font=self.min_font, 
                                   text='Regle', 
                                   command=self.reglement)
        self.L_Dealer:Label = Label(self.root, 
                              text="Dealer", 
                              font=self.max_font,
                                bg="#f0f0c8")
        self.L_Joueur = Label(self.root, 
                              text=self.username, 
                              font=self.max_font,
                                bg="#f0f0c8")
        self.L_total_D = Label(self.root, 
                               text=f"Total du Dealer: {self.total_D}",
                               font=self.min_font,
                               bg="#f0f0c8")
        self.L_total_J = Label(self.root,
                               text=f"Total: {self.total_J}",
                               font=self.min_font,
                               bg="#f0f0c8")
        self.L_Mis_en_jeu = Label(self.root, 
                                  text=f"Argent en jeu: ${self.bet}", 
                                  font=self.min_font,
                                  bg="#f0f0c8")
        self.L_Argent_J = Label(self.root, 
                                text=f"Argent gagné/perdu par le Joueur: ${self.monnaie}", 
                                font=self.min_font,
                                bg="#f0f0c8")
        self.Pioche = Button(self.root, 
                             text="Pioche", 
                             font=self.min_font, 
                             relief=RAISED, 
                             command=self.piocher)
        self.Arret_P = Button(self.root, 
                              text="Terminé", 
                              font =self.min_font, 
                              relief =RAISED, 
                              command=self.dealer_stuff)
        self.Sortir = Button(self.root, 
                             text="Exit", 
                             font=self.min_font,
                             relief=RAISED, 
                             command=self.root.destroy)
        self.reset = Button(self.root, 
                            text="Reset", 
                            font=self.min_font, 
                            relief=RAISED, 
                            command=self.reinit)
        self.frame_J =Frame(self.root, 
                            width=700, 
                            height=250,
                            bg="#35654d")
        self.frame_D =Frame(self.root, 
                            width=700, 
                            height=250,
                            bg="#35654d")
        
        self.mis_en_place_des_widgets()
        self.root.mainloop()
        
    def mis_en_place_des_widgets(self):
        while self.rows < 50:
            self.root.rowconfigure(self.rows, 
                                   weight=1)
            self.root.columnconfigure(self.rows,
                                      weight=1)
            self.rows += 1
        
        self.frame_J.grid(row=25, 
                          column=14, 
                          columnspan=20,
                          rowspan=19)
        self.frame_D.grid(row=3, 
                          column=14, 
                          columnspan=20,
                          rowspan=19)
        self.L_Dealer.grid(row=2, 
                           column =24)
        self.L_total_D.grid(row=2, 
                            column=26)
        self.L_Joueur.grid(row=24, 
                           column=24)
        self.L_total_J.grid(row=24, 
                            column=26)
        self.L_Mis_en_jeu.grid(row=24, 
                               column=2)
        self.L_Argent_J.grid(row=25, 
                             column=2)
        self.Pioche.grid(row=48, 
                         column=25)
        
        self.Arret_P.grid(row=48, 
                          column =24)
        self.Sortir.grid(row=48, 
                         column=48)
        self.reset.grid(row=48, 
                        column=46)
        self.B_regle.grid(row=48, 
                          column=44)
        self.root.bind("<p>", 
                       self.piocher)
        self.root.bind("<t>", 
                       self.dealer_stuff)
        self.root.bind("<r>", 
                       self.reinit)
        self.root.bind("<R>", 
                       self.reglement)

    def reglement(self, event=None):
        pop_up=Toplevel(self.root)
        regle=Label(pop_up,
                    font='Arial 12', 
                    justify='left',
                    text="Le but du blackjack est de battre le dealer. Pour le battre il faut arriver à etre le plus proche de 21 sans avoir plus.\nSi le dealer a moins que vous ou dépasse 21 vous gagnez. Si le dealer a plus que vous et moins de 21, il gagne.")
        regle.pack()
        regle2=Label(pop_up, 
                     font=self.min_font,
                     justify='left',
                     text="RAPPEL:\n-   Un As peut valoir 1, 10, ou 11\n-   Le roi, la reine, et le valet vallent 10")
        regle2.pack()
        B_exit=Button(pop_up,
                      font=self.min_font,
                      text="Exit",
                      command=pop_up.destroy)
        B_exit.pack()
        pop_up.mainloop()
    
    def add_image_D(self):
        image = Image.open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 
                                        self.dico_carte[self.Carte_D[-1].getCouleur()][self.Carte_D[-1].Valeur]))
        size=image.size
        resize_image = image.resize((size[0]//4, size[1]//4))
        img = ImageTk.PhotoImage(resize_image)
        img_lab=Label(self.frame_D,
                      image=img,
                      bg="#35654d")
        img_lab.image = img # keep a reference!
        img_lab.place(x=50+50*(len(self.Carte_D)-1), y=50)
    
    def add_image_J(self):
        image = Image.open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 
                                        self.dico_carte[
            self.Carte_J[-1].getCouleur()][self.Carte_J[-1].Valeur]))
        size=image.size
        resize_image = image.resize((size[0]//4, size[1]//4))
        img = ImageTk.PhotoImage(resize_image)
        img_lab=Label(self.frame_J,
                      image=img,
                      bg="#35654d")
        img_lab.image = img # keep a reference!
        img_lab.place(x=50+50*(len(self.Carte_J)-1), y=50)
        
    def reinit(self, event=None):
        if not self.keep:
            self.monnaie='0'
            self.L_Argent_J['text']=f"Argent gagné/perdu par le Joueur: ${self.monnaie}"
        self.bet=0
        self.total_J=0
        self.total_D=0
        self.L_Mis_en_jeu["text"]=f"Argent en jeu: ${self.bet}"
        self.L_total_D["text"]=f"Total du Dealer: {self.total_J}"
        self.L_total_J["text"]=f"Total: {self.total_J}"
        for widgets in self.frame_D.winfo_children():
            widgets.destroy()
        for widgets in self.frame_J.winfo_children():
            widgets.destroy()
        self.keep=False
        shuffle(self.paquet1.contenu)
        shuffle(self.paquet2.contenu)
        self.indice_J=0
        self.indice_D=0
        self.Carte_J=[]
        self.Carte_D=[]
        self.username=""
        self.L_Joueur['text']=self.username
    
    def piocher(self, event=None):
        if self.username=="":
            self.set_username()
        if self.bet == 0:
            E_monnaie=Entry(self.root)
            E_monnaie.grid(row=26,
                           column=2)
            E_monnaie.focus_set()
            valeur=IntVar()
            answer_monnaie=Label(self.root, 
                                 text='',
                                 bg="#f0f0c8")
            answer_monnaie.grid(row=30, 
                                column=2)
            def get_value(event=None):
                if not int(E_monnaie.get())>0:
                    answer_monnaie.config(text="Le bet doit etre superieur à 0")
                else:
                    valeur.set(int(E_monnaie.get()))
            B_nb=Button(self.root, 
                        text="Valeur du bet: ", 
                        command=get_value, 
                        font=self.min_font, 
                        relief=RAISED)
            self.root.bind('<Return>',get_value)
            B_nb.grid(row=28, 
                      column=2)
            self.root.wait_variable(valeur)
            B_nb.destroy()
            answer_monnaie.destroy()
            E_monnaie.destroy()
            self.bet=int(valeur.get())
            self.L_Mis_en_jeu['text']=f"Argent en jeu: ${self.bet}"
        self.Carte_J.append(self.paquet1.getCarteAt(self.indice_J))
        self.total_J=self.total_J+int(self.valeur_de_carte_J(self.Carte_J[-1].Valeur))
        self.indice_J=self.indice_J+1
        self.L_total_J["text"]=f"Total: {self.total_J}"
        self.add_image_J()
        if self.total_J>21:
            self.perdre()
                
    def dealer_stuff(self, event=None):
        while self.total_D<self.total_J and self.total_D<22:
            self.Carte_D.append(self.paquet2.getCarteAt(self.indice_D))
            self.total_D=self.total_D+int(self.valeur_de_carte_D(self.Carte_D[-1].Valeur, 
                                                                 self.total_D))
            self.indice_D=self.indice_D+1
            self.L_total_D["text"]=f"Total du Dealer: {self.total_D}"
            self.add_image_D()
        if self.total_D<22 and self.total_D>self.total_J:
            self.perdre()
        elif self.total_D>21 or self.total_D<self.total_J:
            self.gagner()
        else:
            self.egaliter()
    
    def valeur_de_carte_J(self,card_value):
        if card_value>10 and card_value <14:
            return 10
        elif card_value==1:
            nb=Entry(self.root)
            nb.grid(row=26, 
                    column=2)
            nb.focus_set()
            valeur=IntVar()
            answer_nb=Label(self.root, 
                            text='',
                            bg="#f0f0c8")
            answer_nb.grid(row=30, 
                           column=2)
            def get_value(event=None):
                if not (int(nb.get())==10 or int(nb.get())==1 or int(nb.get())==11):
                    answer_nb.config(text="la valeur doit etre 1, 10, ou 11!")
                else:
                    valeur.set(int(nb.get()))
            B_nb=Button(self.root, 
                        text="Valeur de l'As (1, 10, 11): ", 
                        command=get_value, 
                        font=self.min_font, 
                        relief=RAISED)
            B_nb.grid(row=28, 
                       column=2)
            self.root.bind('<Return>',get_value)
            self.root.wait_variable(valeur)
            B_nb.destroy()
            answer_nb.destroy()
            nb.destroy()
            return valeur.get()
        else:
            return card_value
    
    def valeur_de_carte_D(self, valeur, total):
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
         
    def perdre(self):
        self.monnaie=str(int(self.monnaie)-self.bet)
        self.L_Argent_J['text']=f"Argent gagné/perdu par le Joueur: ${self.monnaie}"
        self.keep=True
        pop_up=Toplevel(self.root)
        pop_up.geometry('250x100')
        L_perd=Label(pop_up,
                     font=self.min_font,
                     text="Vous avez perdu ${}!".format(self.bet))
        L_perd.pack()
        B_exit=Button(pop_up, 
                             text="Exit", 
                             font=self.min_font,
                             relief=RAISED, 
                             command=lambda: [pop_up.destroy(), self.reinit()])
        B_exit.pack()
        pop_up.mainloop()
        
    def gagner(self):
        self.monnaie=str(int(self.monnaie)+self.bet)
        self.L_Argent_J['text']=f"Argent gagné/perdu par le Joueur: ${self.monnaie}"
        self.keep=True
        pop_up=Toplevel(self.root)
        pop_up.geometry('250x100')
        L_gag=Label(pop_up,
                     font=self.min_font,
                     text="Vous avez gagné ${}!".format(self.bet))
        L_gag.pack()
        B_exit=Button(pop_up, 
                             text="Exit", 
                             font=self.min_font,
                             relief=RAISED, 
                             command=lambda: [pop_up.destroy(), 
                                              self.reinit()])
        B_exit.pack()
        pop_up.mainloop()

    def egaliter(self):
        self.keep=True
        pop_up=Toplevel(self.root)
        pop_up.geometry('250x100')   
        L_egal=Label(pop_up,
                     font=self.min_font,
                     text="Vous etes à ex-aequo!")
        L_egal.pack()
        B_exit=Button(pop_up, 
                             text="Exit", 
                             font=self.min_font,
                             relief=RAISED, 
                             command=lambda: [pop_up.destroy(), self.reinit()])
        B_exit.pack()
        pop_up.mainloop()
    
    def set_username(self):
        T_username= Toplevel(self.root) 
        T_username.geometry('250x100')
        L_username=Label(T_username,
                         font=self.min_font,
                         text="Entrer votre username:")
        L_username.pack()
        E_username=Entry(T_username,
                         font=self.min_font)
        E_username.pack()
        
        def init_username(event=None):
            self.username=str(E_username.get())
            self.L_Joueur["text"]=self.username
        B_exit=Button(T_username,
                      text="Accepter",
                      font=self.min_font,
                      relief=RAISED, 
                      command=lambda:[(init_username(), T_username.destroy())])
        B_exit.pack()
        T_username.mainloop()