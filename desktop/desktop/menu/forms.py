
from tkinter import Label, W, Tk


from desktop.composants.cadre import App, ScrollbarFrame

class Form():
    frame = None
    def __init__(self, fenetre: Tk, champs: list) -> None:
        """
        
        """
        
        self._fenetre = fenetre

        self.champs = champs
        
    def render(self, row=0, column=0, ):
        """
        Description:
        ------------
            cette fonction assure le rendu du formulaire
        """
        
        sbf = ScrollbarFrame(self._fenetre)
        self._fenetre.grid_rowconfigure(0, weight=1)
        self._fenetre.grid_columnconfigure(0, weight=1)
        sbf.grid(row=0, column=0, sticky='nsew')

        
        self.frame = sbf.scrolled_frame

        
        for index, i in enumerate(self.champs):
            Label(self.frame, text=i).grid(row= row + index, column=column)
        

        
    