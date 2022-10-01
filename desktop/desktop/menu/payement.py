from tkinter import Button, Canvas, Menu, Scrollbar, Tk
from menu.classes import Classes

from desktop.core.core import GPayement

from menu.forms import Form

from desktop.core.config import MOIS

class Payement(Menu):
    def __init__(self, fenetre, menu:Menu):
        super().__init__(menu)
        self.add_cascade(label="Payé", menu=Classes(fenetre, self, Paye))
        self.add_cascade(label="Non payé", menu=Classes(fenetre, self, NonPaye))
        self.add_command(label="Gestion", command=Gestion().view)

class Paye(GPayement, Form):
    def __init__(self, fenetre, classe):
        """
        """
        self._fenetre = fenetre
        
        #top = Toplevel(fenetre)

        GPayement.__init__(self, classe)

        liste = (self.getListe())

        label = list()

        for i in liste.values():
            for y in i: label.append(" ".join(y))
        
        del label[0]
        
        Form.__init__(self, self._fenetre, label)

        self.addColumn()

        self.addColumn(types="C", text="Payé")
    
    def view(self):
        """
        """
        for i in self._fenetre.children.values(): i.grid_remove()
        #scr = Scrollbar(self._fenetre, orient="vertical", command=self._fenetre.yview)

        #self._fenetre.configure(yscrollcommand=scr.set)
        #scr.place(x = 200, y = 10, height=250)
        self.render(row=1)

        Button(self._fenetre, text="Valider", command= self.getValue).grid(row=0, column=0)


class NonPaye(GPayement, Form):
    def __init__(self, fenetre, classe):
        """
        """
        self._fenetre = fenetre
        
        #top = Toplevel(fenetre)

        GPayement.__init__(self, classe)

        liste = (self.getListe())

        label = list()

        for i in liste.values():
            for y in i: label.append(" ".join(y))
        
        del label[0]
        
        Form.__init__(self, self._fenetre, label)

        self.addColumn()

        self.addColumn(types="C", text="Non Payé")
    
    def view(self):
        """
        """
        for i in self._fenetre.children.values(): i.grid_remove()

        self.render()

class Gestion(object):
    def __init__(self,):
        """
        """
    
    def view(self):
        """
        
        """