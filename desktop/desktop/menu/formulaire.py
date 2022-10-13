from optparse import Values
from tkinter import Button, Entry, Label, Menu, Toplevel
from menu.classes import Classes
from desktop.core.core import GEleve
from desktop.menu.forms import Form

class Formulaire(Menu):
    def __init__(self, fenetre, menu:Menu):
        
        super().__init__(menu)
        self.add_cascade(label="Rélevé", menu=Classes(fenetre, self, Releve))
        self.add_command(label="Relevé annuelle")
        self.add_command(label="Certificat de transfert")


class Releve(GEleve, Form):
    """
    """
    def __init__(self, fenetre, classe: int):
        GEleve.__init__(self, classe)
        self._fenetre = fenetre
        
        # definition de la classe
        self._classe = classe

        self.liste = (self.getListe())

        self._exporter = None
         
        self._heade  = list(self.liste.keys())


        #self.values = [None for i in range(len(self.label[0]))]
        
        self.values = []

        Form.__init__(self, self._fenetre, )
    
    def view(self):
        """
        """
        self.render(row=2)

        self.head()

        self.addColumn()

    def exporter(self):
        """
        Description:
        ------------
            cette fonction permet exporter les contenut des
            cellules en autres forme de document
        """

        top = Toplevel(self._fenetre)
        
        top.geometry("400x400")
        
    def head(self):
        """
        Description:
        ------------
            cette fonction ajoute entête dans le frame
        """
        self._exporter = Button(self.frame, text="Exporte", command=self.exporter)
        
        self._exporter.grid(row=0, column=0)

        for index, i in enumerate(self._heade):
            Label(self.frame, text=i).grid(row=1, column=index)
    
    def addColumn(self):
        """
        Description:
        ------------
            cette fonction ajoute des colunne suplementaire
            dans sur l'ecran

        """
        data = self.liste.keys()

        for i in range(len(self.liste["Noms"])):
            el = []
            for y in data:
                el.append(self.liste[y][i])

            entre = [ Entry(self.frame) for i in range(len(el))]

            for (col, y) , value in zip(enumerate(entre), el):
                #print(value)
                y.insert(0, value)

                y.grid(row=i + 3, column=col)

            self.values.append(entre)



        """for index, value in enumerate(self.label):
            

            for col, i in enumerate(entre):

                #i.insert(0, value[col])

                i.grid(row=index + 3, column=col)

            self.values.append(entre)"""
    