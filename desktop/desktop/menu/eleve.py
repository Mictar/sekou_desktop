"""
Desciption:
-----------
    cet module englobe tout les ojects et fonction
    s'appliquant sur les élèves
"""
from tkinter import *
from tkinter import filedialog

from menu.classes import Classes
from menu.items import  ItemEleve

from desktop.core.core import GBulletin, GEleve, GNotes
from desktop.core.config import MATIERE, USER_INFORMATION

from menu.forms import Form

DEBUG = 1
class Eleve(Menu):
    def __init__(self, fenetre, menu:Menu):
        super().__init__(menu)

        #add = AddStudiant(fenetre)
        self.add_cascade(label="Profile", menu=Classes(fenetre, self, Profile))
        self.add_cascade(label="ajoute", menu=Classes(fenetre, self, AddStudiant))
        self.add_cascade(label="Notes", menu=Classes(fenetre, self, Notes))

        self.add_cascade(label="Bulletin", menu=Classes(fenetre, self, Bulletin))


    

class Profile(GEleve, Form):
    """
    """
    def __init__(self, fenetre, classe: int):
        GEleve.__init__(self, classe)
    
    def view(self):
        """
        """

class AddStudiant(ItemEleve, GEleve):
    """
    Description:
    ------------
        cette class est permet d'ajouter des élèves selon
        leurs class
    """
    def __init__(self, fenetre, classe: int) -> None:

        ItemEleve.__init__(self, fenetre, classe)
        
        GEleve.__init__(self, classe)
        self._fenetre = fenetre
        self._classe = classe
        #self._fenetre = Tk()
        self._user_information = USER_INFORMATION

    def view(self):
        """
        Description:
        ------------
            cette fonction affiche une interface graphique
            pour ajouter les élèves
        """
        add_studiant =Toplevel(self._fenetre)

        user_len = len(self._user_information.keys())

        label_user = [ Label(add_studiant, 
                       text=key).grid(row=index, column=1, sticky=W)\
             for index, key in enumerate(self._user_information.keys())]

        self._entry_user = [ Entry(add_studiant) \
            for i in range(user_len)]

        for index, i in enumerate(self._entry_user):
            i.grid(row=index, column=2)


        if DEBUG:
            for i in self._entry_user:
                i.insert(0, 'Moctar')

        self._entry_user[-1].insert(0, str(self._classe))

        valider=Button(add_studiant,text=' valider ', command=self.valider )
        
        selection=Button(add_studiant,text='Selection', command=self.selection)

        self._cadre = Canvas(add_studiant, width =160, height =160, bg ='white')
        
        
        #self._photo = PhotoImage()

        #self.item = self._cadre.create_image(160, 160, image =self._photo)
        valider.grid(row=12,column=2,padx=2,pady=8)

        self._cadre.grid(row =1, column =3, rowspan =8 ,padx =10, pady =5)

        selection.grid(row=9,column=3, sticky =N)
        
    
    def selection(self):
        """
        Desciption:
            cette fonction selection une image

        """
        tof= filedialog.askopenfilename()
        photo = PhotoImage(file=tof)
        self._cadre.create_image(160, 160, image= photo)


    def valider(self, ):
        """
        Description:
        ------------
            cette fonction permet de valider l'ajoute d'un élève

        """
        eleve = { key: value.get() for value, key \
            in zip(self._entry_user, self._user_information.keys())}
        
        self.addListe(eleve)
        self.save()


    def cli(self):
        """
        Description:
        ------------
            cette fonction fournie une interface en lignes de commande
            pour ajouter les élèves
        """

class Notes(GNotes, Form):
    def __init__(self, fenetre, classe):
        """
        Desciption:
        -----------
        """
        self._fenetre = fenetre
        self._frame = Frame(fenetre)
        
        #top = Toplevel(fenetre)
        self._matiere = MATIERE[classe]

        GNotes.__init__(self, classe)

        liste = (self.getListe())

        label = list()

        for i in liste.values():
            for y in i: label.append(" ".join(y))
        
        del label[0]
        
        Form.__init__(self, self._fenetre, label)

        self.addColumn()

        #self.addColumn(types="C", text="Payé")


    def view(self):
        """
        
        """
        
        #print(self._fenetre.children)
        #self._frame.pack_forget()
        
        for i in self._fenetre.children.values(): i.grid_remove()

        Button(self._fenetre, text="valider", command= lambda : print(self.getValue())).grid(row=0, column=0)

        self.render(row=1)
        #self._frame.pack()
        

    def viewDevoir(self):
        """
        Description:
        ------------
            cette fonction affiche une interface graphique
            pour ajoutes les notes des élèves
        """


    def viewComposition(self):
        """
        Description:
        ------------
            cette fonction affiche une interface graphique
            pour ajouter les notes de compositions des élèves
        """
    
    def viewAnnuel(self):
        """
        Description:
        ------------
            cette fonction affiche une interfaces graphique
            pour ajouter les notes annuels des élèves
        """

class Bulletin(GBulletin):
    """
    Cette classe est charger du rendu des bulletins
    des élèves
    """
    def __init__(self, fenetre, classe) -> None:
        self._fenetre = fenetre
        self._matiere = MATIERE[classe]
        
        super().__init__(classe)

    def view(self):
        """
        Description:
        ------------
            cette fonction permet d'afficher le bulletin
            des élèves 
        """
    
    def buildPdf(self):
        """
        Description:
        ------------
            cette fonction est charger de produire le bulletin
            des élève en formant pdf
        """
    
    def buildXlsl(self):
        """
        Description:
        ------------
            cette fonction est charger de produire le bulletin
            des élèves en format excel

        """

