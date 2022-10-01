from tkinter import Menu
import sys
class Files (Menu):
    def __init__(self, fenetre, menu:Menu):
        super().__init__(menu)
        self.add_command(label="Nouveau")
        self.add_command(label="Ouvrir")
        self.add_command(label="Recents")
        self.add_command(label="Save")
        self.add_command(label="Save as")
        self.add_command(label="Exporter")
        self.add_command(label="Importer")
        self.add_command(label="Parametre")

        self.add_command(label="Quit", command=lambda : sys.exit())
