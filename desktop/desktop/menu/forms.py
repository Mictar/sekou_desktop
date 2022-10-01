
from tkinter import Checkbutton, Entry, Label, W, Tk, Toplevel


class Form(object):

    def __init__(self,fenetre: Tk, champs: list) -> None:
        """
        
        """
        # creation des entrée
        #self._fenetre = Toplevel(self._fenetre)
        self._fenetre = fenetre

        #self._entre = [ Entry(self._fenetre) for i in range(len(champs))]
        
        self._values = list()

        self._label = [ Label(self._fenetre, text=text) for text in champs ]
        

    def render(self, row=0, column=1):
        """
        Description:
        ------------
            cette fonction assure le rendu du formulaire
        """
        
        # ajoute de la premiere valeur du champ
        self.grid(self._label, row=row, column=column)

        # ajoute des autre champ 
        
        for index, i in enumerate(self._values): self.grid(i, column=index + 2 + column, row= row)
    
    def grid(self, composant, row=0, column=1):
        for index, i in enumerate(composant):
            i.grid(row=index + row, column=column, sticky="W")

    def addColumn(self, types="E", text=None):
        """
        Description:
        ------------
            cette fonction ajoutter de nouveau colonne 
            au rendu de la formulaire
        """
        if types == "E":
            self._values.append([Entry(self._fenetre) for i in range(len(self._label))])
        
        if types == "C":
            
            self._values.append([Checkbutton(self._fenetre, text=text) for i in range(len(self._label))])
    
    def decalage(initial: int, fin: int):
        """
        Description:
        ------------
            cette fonction decale une colonne entiere
            dans une autre colonne
        """
    
    def getValue(self) -> dict:
        """
        Description:
        ------------
            cette fonction retourne les valeurs des champs

        """
        return { key["text"] : value.get() for  value, key in zip(self._entre, self._label)}