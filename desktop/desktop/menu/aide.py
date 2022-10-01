from tkinter import Menu

class Aide(Menu):
    def __init__(self, fenetre, menu:Menu):
        super().__init__(menu)
        self.add_command(label="Documentation")
        self.add_command(label="Exemple")
