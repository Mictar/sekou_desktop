from tkinter import *
from menu.aide import Aide
from menu.eleve import Eleve
from menu.formulaire import Formulaire

from menu.payement import Payement
from menu.files import Files
from menu.edition import Edition

class KMenu(Menu):
    def __init__(self, fenetre):
        Menu.__init__(self, fenetre)

        self.add_cascade(label="Files", menu=Files(fenetre, self))
        self.add_cascade(label="Edition", menu=Edition(fenetre, self))
        
        
        self.add_cascade(label="Payement", menu=Payement(fenetre, self))

        
        self.add_cascade(label="Eleve", menu=Eleve(fenetre, self))
        
        
        self.add_cascade(label="Formulaire", menu=Formulaire(fenetre, self))

        
        self.add_cascade(label="Aide", menu=Aide(fenetre, self))


