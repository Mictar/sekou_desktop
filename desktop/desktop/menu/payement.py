from datetime import date
from tkinter import Button, Canvas, Label, Menu, Scrollbar, Spinbox, Tk, Entry
from menu.classes import Classes

from desktop.composants import Checkbutton

from desktop.core.core import GPayement

from menu.forms import Form

from desktop.core.config import MOIS, MONTANT

class Payement(Menu):
    def __init__(self, fenetre, menu:Menu):
        super().__init__(menu)
        self.add_cascade(label="Payé", menu=Classes(fenetre, self, Paye))
        #self.add_cascade(label="Non payé", menu=Classes(fenetre, self, NonPaye))
        self.add_command(label="Gestion", command=Gestion().view)

class Paye(GPayement, Form):
    def __init__(self, fenetre, classe):
        """
        """
        self._fenetre = fenetre

        # definition global de la variable classe dans
        # l'object Paye
        self._classe = classe
        
        #top = Toplevel(fenetre)
        self._header = ["Prenom et Nom", "Montant Paye", "Validation"]

        GPayement.__init__(self, classe)

        liste = (self.getListe())

        self.label = list()

        for i in liste.values():
            for y in i: self.label.append(" ".join(y))
        
        del self.label[0]
        
        Form.__init__(self, self._fenetre, self.label)

        self._valide = None
        self._mois = None
        self._montant = None

        #self.colm = None
        
        self.values = [None, None]

        #self.colval = None

    def view(self):
        """
        """
        
        self.render(row=2, column=0)
        
        self.addColumn()

        self.header()
        self.changeEntry()

    def changeEntry(self):
        """
        Description:
        ------------
            cette fonction change les entry
        """

        getData = self.getJson(self._mois.get(), self._classe)

        if getData:
            value = [ self._montant.get() \
                if i["valide"] else i["montant"] \
                    for i in getData["data"]]

            self.modifierEntry(0, value)
        else:
            self.modifierEntry(0, all=True)
        
    def header(self):
        """
        Description:
        ------------
            cette fonction affiche les meta données de l'entête

        """
        self._valide = Button(self.frame, text="Valider",
                             command=self.valider)

        self._mois = Spinbox(self.frame, values=MOIS, 
                             command=self.changeEntry )

        self._montant = Entry(self.frame)
        

        self._montant.insert(0, MONTANT[self._classe])

        self._valide.grid(row=0, column=0)

        self._mois.grid(row=0, column=1)
        
        self._montant.grid(row=0, column=2)

        Label(self.frame, text="Montant").grid(row=0, column=3)

        for  index, i in enumerate(self._header):
            Label(self.frame, text=i).grid(row=1, column=index)
        
    
    def addColumn(self):
        """
        Description:
        ------------
            cette fonction affiche les colonnes accesoire dans le body

        """
        # index 0 contient des entry pour representé les montants

        self.values[0] = [ Entry(self.frame) \
            for i in range(len(self.label))]
        
        # index 1 contient les checkbutton pour selectionne directement 
        # les entre
        self.values[1] = [ Checkbutton(self.frame, text="Payé")\
             for i in range(len(self.label))]

        for index, i in enumerate(self.values[0]): \
            i.grid(row=index + 2 , column=1)

        for index, i in enumerate(self.values[1]): \
            i.grid(row=index + 2 , column=2)

    
    def modifierEntry(self, pos, data=[], all=False):
        """
        
        """
        if all:
            for i in self.values[pos]:
                i.delete(0, "end")
                i.insert(0, "")

        for i, value in zip(self.values[pos], data):
            i.delete(0, "end")
            i.insert(0, value)

    def getValue(self) -> list:
        
        label = [i["text"] for i in self._label ]

        data = [ [ y.get() for y in i ]for i in self.values]
        data.append(label)

        return (data)

    def valider(self):
        
        montant, validation, name = self.getValue()
        
       
        data = {
            "header": {
                "mois": self._mois.get(),
                "montant": self._montant.get(),
                "date": str(date.today()),
                "classe": str(self._classe)
            },
            "data": [ {"name" : i[0][0], "montant": i[2], "valide": i[1] }\
                for i in zip(enumerate(name), validation, montant)]
        }

        self.saveJson(data) 




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
        #for i in self._fenetre.children.values(): i.grid_remove()

        self.render()

class Gestion(object):
    def __init__(self,):
        """
        """
    
    def view(self):
        """
        
        """