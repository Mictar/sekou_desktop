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

import pandas as pd
DEBUG = 0

class Eleve(Menu):
    def __init__(self, fenetre, menu:Menu):
        super().__init__(menu)

        # ajoute du menu profile
        self.add_cascade(label="Profile", menu=Classes(fenetre,
                                                         self, 
                                                         Profile))
        # ajoute du menu "ajouter eleve"
        self.add_cascade(label="ajoute", menu=Classes(fenetre,
                                                       self, 
                                                       AddStudiant))

        # ajoute du menu notes
        self.add_cascade(label="Notes", menu=Classes(fenetre, self, Notes))

        # ajoute du menu Bulletin
        self.add_cascade(label="Bulletin", menu=Classes(fenetre, self, Bulletin))


class Profile(GEleve, Form):
    """
    """
    def __init__(self, fenetre, classe: int):
        GEleve.__init__(self, classe)
        self._fenetre = fenetre
        
        self._classe = classe

        
        self._user_information = USER_INFORMATION


        self.liste = (self.getListe())

        self.label = [ f"{str(i[0])} {str(i[1])}" for i in zip(self.liste["Prenoms"], self.liste["Noms"])]
        #print(self.label)
        """for i in liste.values():
            for y in i: self.label.append(" ".join(y))
        
        del self.label[0]"""
        #print(self.label)
        
        Form.__init__(self, self._fenetre, self.label)
    
    def view(self):
        """
        """
        self.render()
        self.addColumn()

    def addColumn(self):
        data = self.liste.keys()
        values = []

        for i in range(len(self.liste["Noms"])):
            el = []
            for y in data:
                el.append(self.liste[y][i])
            values.append(el)

        self._profile = [Button(self.frame, text="voir",
                                command=self.eleve(i)) for i in values]

        for index, i in enumerate(self._profile):

            i.grid(row=index, column=1)
    
    def eleve(self, name: list):

        def el():
            #global key
            #for i in self.key: print(self.liste[i])
            
            """for _, i in self.liste.items():
                for y in i: print(y)"""
            
            add_studiant =Toplevel(self._fenetre)
            add_studiant.resizable(0, 0)

            user_len = len(self._user_information.keys())

            label_user = [ Label(add_studiant, 
                        text=key).grid(row=index, column=1, sticky=W)\
                for index, key in enumerate(self._user_information.keys())]

            self._entry_user = [ Entry(add_studiant) \
                for i in range(user_len)]


            for index, i in enumerate(self._entry_user):
                i.grid(row=index, column=2)
            
            self._entry_user[-1].insert(0, str(self._classe))

            index = {0: 2, 1 : 3, 2 : 6, 3: 5, 4 : 4,
                    5: 7, 6: 8, 8 : 1, 7 : 9}

            for key, value in index.items():
                try:
                    #print(key, name[value])
                    self._entry_user[key].insert(0, str(name[value]))
                except: pass
            
            valider=Button(add_studiant,text=' valider ',
                        command=self.valider )
            
            selection=Button(add_studiant,text='Selection',
                            command=self.selection)

            self._cadre = Canvas(add_studiant, 
                                width =160, height =160, bg ='white')
            
            
            #self._photo = PhotoImage()

            #self.item = self._cadre.create_image(160, 160, image =self._photo)
            valider.grid(row=12,column=2,padx=2,pady=8)

            self._cadre.grid(row =1, column =3, rowspan =8 ,padx =10, pady =5)

            selection.grid(row=9,column=3, sticky =N)
        
        return el

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
        """eleve = { key: value.get() for value, key \
            in zip(self._entry_user, self._user_information.keys())}
        
        self.addListe(eleve)
        self.save()"""
    

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

        valider=Button(add_studiant,text=' valider ',
                       command=self.valider )
        
        selection=Button(add_studiant,text='Selection',
                        command=self.selection)

        self._cadre = Canvas(add_studiant, 
                            width =160, height =160, bg ='white')
        
        
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
        
        
        data = self.getListe()
        #print(list(data.keys()))
        data_eleve =  {
            "N °ordre": len(data['N °ordre']),
            'N° Ml': "",
            "Noms": eleve['nom'],
            "Prenoms": eleve['prenom'],
            'Sexe' : eleve["sexe"],
            'Lieu de naissance' : eleve["lieu de naissance"],
            'Date de naissance': eleve["date de naissance"],
            'Prenom du père': eleve["prenom du père"], 
            'Nom du père' : eleve["nom"], 
            'Prenom de la mere': eleve["prenom de la mère"],
            'Nom de la mère' : eleve["nom de la mère"],
        }
        data = data.append(data_eleve, ignore_index=True)
        #save = pd.concat([data, data_eleve], ignore_index=True)
        
        self.save(data)
        data.to_excel("test1.ods", engine="odf")
        #print(save)

        # imcorrect code
        """keys = list(data.keys())
        for i, el in zip(keys, eleve):
            data[i].append(str(el))"""

        #self.addListe(eleve)
        
        #self.save(data, "~/Bureau/test.ods")

class Notes(GNotes, Form):
    def __init__(self, fenetre, classe):
        """
        Desciption:
        -----------
        """
        self._fenetre = fenetre
        self._frame = Frame(fenetre)
        self._classe = classe
        
        #top = Toplevel(fenetre)
        #self._matiere = MATIERE[classe]

        GNotes.__init__(self, classe)

        liste = (self.getListe())

        self.label = [ f"{str(i[0])} {str(i[1])}" for i in zip(liste["Prenoms"], liste["Noms"])]
        
        """for i in liste.values():
            for y in i: self.label.append(" ".join(y))
        
        del self.label[0]"""
        Form.__init__(self, self._fenetre, self.label)

        self._valide = None

        self._matiere = None
        
        self._coeficient = None
        
        self._numero = None

        self._type = None

        self.values = [None]



    def view(self):
        """
        
        """
        
        self.render(row=3, column=0)
        
        self.header()

        self.addColumn()

        
    def header(self):

        # les etiquêtes de l'entête
        self._valide = Button(self.frame, text="Valider", 
                             command=self.valide)

        self._matiere = Spinbox(self.frame, 
                                values=MATIERE[self._classe],
                                wrap=True, command=self.changeEntry)
        
        self._coeficient = Entry(self.frame, )
        
        self._numero = Spinbox(self.frame, )

        self._type = Spinbox(self.frame, wrap=True, 
                            values=[
                                "Interrogation", 
                                "Devoir", 
                                "Composition"
                                ],
                            command=self.changeEntry)

        label = ["matière", "coeficient", "numero", "type"]

        for index, i in enumerate(label):

            Label(self.frame, text=i).grid(row=0, column=index + 1)
        
        # positoin de l'entête
        row = 1
        
        # mise en position des entêtes de notes
        self._valide.grid(row=row, column=0)

        self._matiere.grid(row=row, column=1)
        self._coeficient.grid(row=row, column=2)
        self._numero.grid(row=row, column=3)
        self._type.grid(row=row, column=4)

        # les etiquêtes de body
        body_label = ["Prenom et Nom ", "Note"]

        for index, i in enumerate(body_label):
            Label(self.frame, text=i).grid(row=2, column=index)

    def valide(self):
        """
        Description:
        ------------
            cette fonction enregistrement les donnée de notes des élèves

        """

        note, name = self.getValue()

        data = {
            "header": {
                "matiere" : self._matiere.get(),
                "type" : self._type.get(),
                "coefficient": self._coeficient.get(),
                "numero": self._numero.get(),
                "classe": self._classe
            },
            "data": [
                {
                    "name": i[1][0],
                    "note": i[0]
                }
                for i in zip(note, enumerate(name))
            ]
        }

        self.saveJson(data)

    def changeEntry(self):
        """
        Description:
        ------------
            cette fonction change les entry
        """

        getData = self.getJson(self._type.get(), self._classe, self._matiere.get(), self._numero.get())
        
        if getData:
            value = [ i['note']
                    for i in getData["data"]]
            self.modifierEntry(0, value)
        else:
            self.modifierEntry(0, all=True)
    
    def addColumn(self):
        """
        Description:
        ------------
            cette fonction affiche les colonnes accesoire dans le body

        """
        # index 0 contient des entry pour representé les montants

        self.values[0] = [ Entry(self.frame) for i in range(len(self.label))]
        
        
        for index, i in enumerate(self.values[0]): i.grid(row=index + 3 , column=1)


    
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

class Bulletin(GBulletin, Form):
    """
    Cette classe est charger du rendu des bulletins
    des élèves
    """
    def __init__(self, fenetre, classe) -> None:
        self._fenetre = fenetre
        self._matiere = MATIERE[classe]
        
        GBulletin.__init__(self, classe)

        self._valide = None
        self._classe = None

        Form.__init__(self, fenetre)

    def view(self):
        """
        Description:
        ------------
            cette fonction permet d'afficher le bulletin
            des élèves 
        """
    
    def valide(self):
        """
        Description:
        ------------
            cette fonction enregistres les bulletins
            des élèves
        """
