from tkinter import Menu
from menu.classes import Classes

class Formulaire(Menu):
    def __init__(self, fenetre, menu:Menu):
        
        super().__init__(menu)
        self.add_cascade(label="Rélevé", menu=Classes(fenetre, self, Releve))
        self.add_command(label="Relevé annuelle")
        self.add_command(label="Certificat de transfert")


class Releve(object):
    def __init__(self, fenetre, classe):
        """
        
        """
        self._fenetre = fenetre
        self._classe = classe
        
    
    def view(self):
        """
        
        """