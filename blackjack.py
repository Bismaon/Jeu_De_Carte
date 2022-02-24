from tkinter import Tk, Button, Label, RAISED, Frame, Toplevel, Entry, IntVar
import os
from random import shuffle
from PIL import Image, ImageTk
from carte import Carte, PaquetDeCarte
class BlackJack:
    """Cette class, BlackJack, permet de jouer au blackjack à l'aide d'un visuel, Tkinter.
        Elle permet de piocher des cartes, de jouer contre "l'ordinateur", de miser de l'argent,
        de l'argent fictif. Elle permet aussi d'avoir un username, un nom pour le joueur entrer par
        le joueur. Cette classe garde la trace de l'argent gagné à travers le jeu. On peut cliquer
    sur "Regle" pour avoir un pop up montrant les règles, un bouton pour reinitialiser le jeu."""

    def __init__(self, paquet_j, paquet_d):
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
        self.paquet1:PaquetDeCarte= paquet_j
        self.paquet2:PaquetDeCarte= paquet_d
        shuffle(self.paquet1.contenu)
        shuffle(self.paquet2.contenu)
        self.monnaie:str = '0'
        self.rows:int = 0
        self.keep:bool=False
        self.carte_j:list[Carte] = []
        self.carte_d:list[Carte] = []
        self.indice_j:int = 0
        self.indice_d:int = 0
        self.total_j:int = 0
        self.total_d:int = 0
        self.bet:int = 0
        self.username:str = ''
        self.root:Tk = Tk()
        self.root.title("BlackJack")
        self.root.attributes("-fullscreen", True)
        self.root.configure(bg='#f0f0c8')
        self.b_regle:Button=Button(self.root,
                                   font=self.min_font,
                                   text='Regle',
                                   command=self.reglement)
        self.l_dealer:Label = Label(self.root,
                              text="Dealer",
                              font=self.max_font,
                                bg="#f0f0c8")
        self.l_joueur = Label(self.root,
                              text=self.username,
                              font=self.max_font,
                                bg="#f0f0c8")
        self.l_total_d = Label(self.root,
                               text=f"Total du Dealer: {self.total_d}",
                               font=self.min_font,
                               bg="#f0f0c8")
        self.l_total_j = Label(self.root,
                               text=f"Total: {self.total_j}",
                               font=self.min_font,
                               bg="#f0f0c8")
        self.l_mis_en_jeu = Label(self.root,
                                  text=f"Argent en jeu: ${self.bet}",
                                  font=self.min_font,
                                  bg="#f0f0c8")
        self.l_argent_j = Label(self.root,
                                text=f"Argent gagné/perdu par le Joueur: ${self.monnaie}",
                                font=self.min_font,
                                bg="#f0f0c8")
        self.pioche = Button(self.root,
                             text="Pioche",
                             font=self.min_font,
                             relief=RAISED,
                             command=self.piocher)
        self.arret_p = Button(self.root,
                              text="Terminé",
                              font =self.min_font,
                              relief =RAISED,
                              command=self.dealer_stuff)
        self.sortir = Button(self.root,
                             text="Exit",
                             font=self.min_font,
                             relief=RAISED,
                             command=self.root.destroy)
        self.reset = Button(self.root,
                            text="Reset",
                            font=self.min_font,
                            relief=RAISED,
                            command=self.reinit)
        self.frame_j =Frame(self.root,
                            width=700,
                            height=250,
                            bg="#35654d")
        self.frame_d =Frame(self.root,
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

        self.frame_j.grid(row=25,
                          column=14,
                          columnspan=20,
                          rowspan=19)
        self.frame_d.grid(row=3,
                          column=14,
                          columnspan=20,
                          rowspan=19)
        self.l_dealer.grid(row=2,
                           column =24)
        self.l_total_d.grid(row=2,
                            column=26)
        self.l_joueur.grid(row=24,
                           column=24)
        self.l_total_j.grid(row=24,
                            column=26)
        self.l_mis_en_jeu.grid(row=24,
                               column=2)
        self.l_argent_j.grid(row=25,
                             column=2)
        self.pioche.grid(row=48,
                         column=25)

        self.arret_p.grid(row=48,
                          column =24)
        self.sortir.grid(row=48,
                         column=48)
        self.reset.grid(row=48,
                        column=46)
        self.b_regle.grid(row=48,
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
        self.deactivate_button()
        pop_up=Toplevel(self.root)
        regle=Label(pop_up,
                    font='Arial 12',
                    justify='left',
                    text="Le but du blackjack est de battre le dealer. Pour le battre il faut arriver à etre le plus proche de 21 sans avoir plus.\nSi le dealer a moins que vous ou dépasse 21 vous gagnez. Si le dealer a plus que vous et moins de 21, il gagne.")
        regle.pack()
        regle2=Label(pop_up,
                     font=self.min_font,
                     justify='left',
                     text="""RAPPEL:\n-   Un As peut valoir 1, 10, ou 11\n-   Le roi, la reine, et le valet vallent 10""")
        regle2.pack()
        b_exit=Button(pop_up,
                      font=self.min_font,
                      text="Exit",
                      command=lambda:[(pop_up.destroy(), self.activate_button())])
        b_exit.pack()
        pop_up.mainloop()

    def add_image_d(self):
        image = Image.open(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                        self.dico_carte[self.carte_d[-1].get_couleur()][self.carte_d[-1].valeur]))
        size=image.size
        resize_image = image.resize((size[0]//4, size[1]//4))
        img = ImageTk.PhotoImage(resize_image)
        img_lab=Label(self.frame_d,
                      image=img,
                      bg="#35654d")
        img_lab.image = img # keep a reference!
        img_lab.place(x=50+50*(len(self.carte_d)-1), y=50)

    def add_image_j(self):
        image = Image.open(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                        self.dico_carte[
            self.carte_j[-1].get_couleur()][self.carte_j[-1].valeur]))
        size=image.size
        resize_image = image.resize((size[0]//4, size[1]//4))
        img = ImageTk.PhotoImage(resize_image)
        img_lab=Label(self.frame_j,
                      image=img,
                      bg="#35654d")
        img_lab.image = img # keep a reference!
        img_lab.place(x=50+50*(len(self.carte_j)-1), y=50)

    def reinit(self, event=None):
        if not self.keep:
            self.monnaie='0'
            self.l_argent_j['text']=f"Argent gagné/perdu par le Joueur: ${self.monnaie}"
            self.username=""
            self.l_joueur['text']=self.username
        self.bet=0
        self.total_j=0
        self.total_d=0
        self.l_mis_en_jeu["text"]=f"Argent en jeu: ${self.bet}"
        self.l_total_d["text"]=f"Total du Dealer: {self.total_j}"
        self.l_total_j["text"]=f"Total: {self.total_j}"
        for widgets in self.frame_d.winfo_children():
            widgets.destroy()
        for widgets in self.frame_j.winfo_children():
            widgets.destroy()
        self.keep=False
        shuffle(self.paquet1.contenu)
        shuffle(self.paquet2.contenu)
        self.indice_j=0
        self.indice_d=0
        self.carte_j=[]
        self.carte_d=[]

    def piocher(self, event=None):
        if self.username=="":
            self.deactivate_button()
            self.set_username()
            return
        if self.bet == 0:
            self.deactivate_button()
            e_monnaie=Entry(self.root)
            e_monnaie.grid(row=26,
                           column=2)
            e_monnaie.focus_set()
            valeur=IntVar()
            answer_monnaie=Label(self.root,
                                 text='',
                                 bg="#f0f0c8")
            answer_monnaie.grid(row=30,
                                column=2)
            def get_value(event=None):
                if (int(e_monnaie.get())<=0):
                    answer_monnaie.config(text="Le bet doit etre superieur à 0")
                else:
                    valeur.set(int(e_monnaie.get()))
            b_valeur=Button(self.root,
                        text="Valeur du bet: ",
                        command=get_value,
                        font=self.min_font,
                        relief=RAISED)
            self.root.bind('<Return>',get_value)
            b_valeur.grid(row=28,
                      column=2)
            self.root.wait_variable(valeur)
            b_valeur.destroy()
            answer_monnaie.destroy()
            e_monnaie.destroy()
            self.bet=int(valeur.get())
            self.l_mis_en_jeu['text']=f"Argent en jeu: ${self.bet}"
            self.activate_button()
            return
        self.carte_j.append(self.paquet1.get_carte_at(self.indice_j))
        self.total_j=self.total_j+int(self.valeur_de_carte_j(self.carte_j[-1].valeur))
        self.indice_j=self.indice_j+1
        self.l_total_j["text"]=f"Total: {self.total_j}"
        self.add_image_j()
        if self.total_j>21:
            self.deactivate_button()
            self.perdre()

    def dealer_stuff(self, event=None):
        while self.total_d<self.total_j and self.total_d<22:
            self.carte_d.append(self.paquet2.get_carte_at(self.indice_d))
            self.total_d=self.total_d+int(self.valeur_de_carte_d(self.carte_d[-1].valeur,
                                                                 self.total_d))
            self.indice_d=self.indice_d+1
            self.l_total_d["text"]=f"Total du Dealer: {self.total_d}"
            self.add_image_d()
        if self.total_d<22 and self.total_d>self.total_j:
            self.deactivate_button()
            self.perdre()
        elif self.total_d>21 or self.total_d<self.total_j:
            self.deactivate_button()
            self.gagner()
        else:
            self.deactivate_button()
            self.egaliter()

    def valeur_de_carte_j(self, card_value):
        if 10 < card_value <14:
            return 10
        elif card_value==1:
            self.deactivate_button()
            warning_valeur=Entry(self.root)
            warning_valeur.grid(row=26,
                    column=2)
            warning_valeur.focus_set()
            valeur=IntVar()
            answer_nb=Label(self.root,
                            text='',
                            bg="#f0f0c8")
            answer_nb.grid(row=30,
                           column=2)
            def get_value(event=None):
                if (not (int(warning_valeur.get())==10 or
                          int(warning_valeur.get())==1 or
                          int(warning_valeur.get())==11)):
                    answer_nb.config(text="la valeur doit etre 1, 10, ou 11!")
                else:
                    valeur.set(int(warning_valeur.get()))
            b_valeur=Button(self.root,
                        text="Valeur de l'As (1, 10, 11): ",
                        command=get_value,
                        font=self.min_font,
                        relief=RAISED)
            b_valeur.grid(row=28,
                       column=2)
            self.root.bind('<Return>',get_value)
            self.root.wait_variable(valeur)
            b_valeur.destroy()
            answer_nb.destroy()
            warning_valeur.destroy()
            self.activate_button()
            return valeur.get()
        else:
            return card_value

    def valeur_de_carte_d(self, valeur, total):
        if 10 < valeur <14:
            return 10
        if valeur ==1:
            if total>11:
                return 1
            if total ==11:
                return 10
            return 11
        return valeur

    def perdre(self):
        self.monnaie=str(int(self.monnaie)-self.bet)
        self.l_argent_j['text']=f"Argent gagné/perdu par le Joueur: ${self.monnaie}"
        self.keep=True
        pop_up=Toplevel(self.root)
        pop_up.geometry('250x100')
        l_perdu=Label(pop_up,
                     font=self.min_font,
                     text=f"Vous avez perdu ${self.bet}!")
        l_perdu.pack()
        b_exit=Button(pop_up,
                             text="Exit",
                             font=self.min_font,
                             relief=RAISED,
                             command=lambda: [pop_up.destroy(),
                                              self.reinit(),
                                              self.activate_button()])
        b_exit.pack()
        pop_up.mainloop()

    def gagner(self):
        self.monnaie=str(int(self.monnaie)+self.bet)
        self.l_argent_j['text']=f"Argent gagné/perdu par le Joueur: ${self.monnaie}"
        self.keep=True
        pop_up=Toplevel(self.root)
        pop_up.geometry('250x100')
        l_gagne=Label(pop_up,
                     font=self.min_font,
                     text=f"Vous avez gagné ${self.bet}!")
        l_gagne.pack()
        b_exit=Button(pop_up,
                             text="Exit",
                             font=self.min_font,
                             relief=RAISED,
                             command=lambda: [pop_up.destroy(),
                                              self.reinit(),
                                              self.activate_button()])
        b_exit.pack()
        pop_up.mainloop()

    def egaliter(self):
        self.keep=True
        pop_up=Toplevel(self.root)
        pop_up.geometry('250x100')
        l_egalite=Label(pop_up,
                     font=self.min_font,
                     text="Vous etes à ex-aequo!")
        l_egalite.pack()
        b_exit=Button(pop_up,
                             text="Exit",
                             font=self.min_font,
                             relief=RAISED,
                             command=lambda: [pop_up.destroy(),
                                              self.reinit(),
                                              self.activate_button()])
        b_exit.pack()
        pop_up.mainloop()

    def set_username(self):
        t_username= Toplevel(self.root)
        t_username.geometry('250x100')
        l_username=Label(t_username,
                         font=self.min_font,
                         text="Entrer votre username:")
        l_username.pack()
        e_username=Entry(t_username,
                         font=self.min_font)
        e_username.pack()

        def init_username(event=None):
            self.username=str(e_username.get())
            self.l_joueur["text"]=self.username
        b_exit=Button(t_username,
                      text="Accepter",
                      font=self.min_font,
                      relief=RAISED,
                      command=lambda:[(init_username(),
                                       t_username.destroy(),
                                       self.activate_button())])
        b_exit.pack()
        t_username.mainloop()

    def activate_button(self, event=None):
        for widgets in self.root.winfo_children():
            if isinstance(widgets, Button):
                widgets['state']='normal'
        self.root.bind("<p>",
                       self.piocher)
        self.root.bind("<t>",
                       self.dealer_stuff)
        self.root.bind("<r>",
                       self.reinit)
        self.root.bind("<R>",
                       self.reglement)

    def deactivate_button(self, event=None):
        for widgets in self.root.winfo_children():
            if isinstance(widgets, Button):
                if widgets["text"]!="Exit":
                    widgets['state']='disabled'
        self.root.unbind("<p>")
        self.root.unbind("<t>")
        self.root.unbind("<r>")
        self.root.unbind("<R>")
