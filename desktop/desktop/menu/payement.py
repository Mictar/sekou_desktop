from datetime import date
from tkinter import Button, Canvas, Label, Menu, Scrollbar, Spinbox, Tk, Entry, Toplevel

from menu.classes import Classes

from desktop.composants import Checkbutton

from desktop.core.core import GPayement

from tkinter.filedialog import askopenfilename, asksaveasfile

from menu.forms import Form

import pandas as pd
import numpy as np

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

        self.label = [ f"{str(i[0])} {str(i[1])}" for i in zip(liste["Prenoms"], liste["Noms"])]
        
        """for i in liste.values():
            for y in i: self.label.append(" ".join(y))
        
        del self.label[0]"""
        
        Form.__init__(self, self._fenetre, self.label)

        self._valide = None
        self._mois = None
        self._montant = None

        self._exporter = None

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

        self._exporter = Button(self.frame, text="Exporter", command=self.exporter)
        

        self._montant.insert(0, MONTANT[self._classe])

        self._valide.grid(row=0, column=0)

        self._mois.grid(row=0, column=1)
        
        self._montant.grid(row=0, column=2)

        Label(self.frame, text="Montant").grid(row=0, column=3)

        self._exporter.grid(row=0, column=4)

        for  index, i in enumerate(self._header):
            Label(self.frame, text=i).grid(row=1, column=index)
        
    
    def exporter(self):
        """
        Description:
        ------------
            cette fonction permet exporter les contenut des
            cellules en autres forme de document
        """
        top = Toplevel(self._fenetre)

        data = pd.DataFrame()

        check = [ Checkbutton(top, text="Tout"),
                    Checkbutton(top, text="Non Paye"),
                    Checkbutton(top, text="Paye")
        ]

        for index, i in enumerate(check):
            i.grid(row=0, column=index)

        def valide():
            file_name = asksaveasfile(mode="w", initialdir="~/Bureau", initialfile="nouveau.ods")
            #file_name.close()
            montant, validation, name = self.getValue()
            write = pd.DataFrame()
            write["N° Elèves"] = [ i for i in range(len(name))]
            write["Prenoms"] = None
            write["Noms"] = None
            write["Classe"] = [ self._classe for i in range(len(name))]


            # tout

            if check[0].get():
                
                write["Prenoms"] = [" ".join(i.split(" ")[:-1]) for i in name]
                
                write["Noms"] = [ " ".join(i.split(" ")[1:]) for i in name]
                

            # non paye
            elif check[1].get():
                
                prenoms = [ " ".join(i.split(" ")[:-1]) for i, mon in zip(name, montant) if mon !=self._montant.get() ]

                noms = [ " ".join(i.split(" ")[1:]) for i, mon in zip(name, montant) if mon !=self._montant.get() ]

                montan = [ mon for i, mon in zip(name, montant) if mon !=self._montant.get() ]
                data = {
                        "N° Elèves": [ i for i in range(len(prenoms))],
                        "Prenoms": prenoms,
                        "Noms": noms,
                        "Montant": montan,
                        "Classe" : [ self._classe for i in range(len(prenoms))]


                    }

                write = pd.DataFrame(data)

                #write = write.transpose()
                
                
            # payé
            elif check[2].get():
                prenoms = []
                noms = []
                mont = []
                for nae, mon, val in zip(name, montant, validation):
                    if mon == self._montant.get() or val:
                        #print(nae, mon )
                        prenoms.append(" ".join(nae.split(" ")[:-1]))

                        noms.append(" ".join(nae.split(" ")[1:]))

                        mont.append(mon)

                data = {
                        "N° Elèves": [ i for i in range(len(prenoms))],
                        "Prenoms": prenoms,
                        "Noms": noms,
                        "Montant": mont,
                        "Classe" : [ self._classe for i in range(len(prenoms))]


                    }
                write = pd.DataFrame(data)

            self.save(write, file_name.name if file_name else "nouveau.ods")



        Button(top, text="valider", command=valide).grid(row=1, column=1)
                
                
        




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
        
        label = self.label

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