from tkinter import Menu

class Edition (Menu):
    def __init__(self, fenetre, menu: Menu):
        super().__init__(menu)
        self.add_command(label="Bureau")
        self.add_command(label="Arrière")
        self.add_command(label="Avant")
        self.add_command(label="Recherche")