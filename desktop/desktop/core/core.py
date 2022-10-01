from  pyexcel_ods3 import get_data, save_data
from desktop.core.config import NOTES_REP, ELEVES_REP, BULLETIN_REP, PAYEMENT_REP
from collections import OrderedDict

import json

class StoreFile(object):

    def __init__(self, file_name):
        """
        """
        self._liste = get_data(file_name)

        self._modifier = False

    def addListe(self, data: list):
        """
        Description:
        ------------
            cette fonction ajoute de nouvelle donnée a la liste
        
        Parametre:
        ----------
            data : une liste
                il represent l nouvelle a enregistrer
        """
        self._liste[list(self._liste.keys())[0]].append(data)
        #print((data))
        #print(self._liste)
        #print(self._classe_name)

    def getListe(self) -> OrderedDict:
        """
        """

        return (self._liste)
    
    def setListe(self, new_liste: OrderedDict):
        """
        Description:
        ------------
            cette fonction change la liste en cours par un nouveau
            liste
        
        Parametre:
        ----------
            new_liste : un OrderedDict
                il represente la nouvelle liste
        """
        self._liste = new_liste
    
    def updateListe(self, values: list, new_values: list):
        """
        Description:
        ------------
            cette fonction mmet a jour une donnée dans
            le self._liste
        """
    def save(self):
        """
        Description:
        ------------
            cette fonction enregistre le 
        """
        
        save_data("test.ods", self._liste)

class GNotes(StoreFile):
    """
    Description:
    ------------
        cette classe assure la gestion des notes des élèves

    """
    def __init__(self, classe: int) -> None:
        self.classe_name = (f"{NOTES_REP}/listes/liste {classe} année.ods")

        super().__init__(self.classe_name)
    
    

class GBulletin(StoreFile):
    """
    Description:
    ------------
        cette classe assure la gestion du bulletins
        des élèves
    """
    
    def __init__(self, classe: int):
        """
        """
        classe_name = (f"{BULLETIN_REP}/listes/liste {classe} année.ods")
        super().__init__(classe_name)

class GPayement(StoreFile):
    """
    Description:
    ------------
        cette classe assure la gestion de
        payement des elèves

    """
    def __init__(self, classe: int):
        classe_name = (f"{PAYEMENT_REP}/listes/liste {classe} année.ods")
        super().__init__(classe_name)

class GEleve(StoreFile):
    """
    Description:
    ------------
        cette classe assure la gestion des elèves
    """

    def __init__(self, classe: int):
        self._classe_name = (f"{ELEVES_REP}/listes/liste {classe} année.ods")
        super().__init__(self._classe_name)
    
    def addListe(self, data: dict):
        eleve = [
            len( self._liste[list(self._liste.keys())[0]]) + 1,
            data['matricule'],
            data["prenom"],
            data["nom"],
            data['sexe'],
            data["lieu de naissance"],
            data["date de naissance"],
            data["prenom du père"],
            data["nom"],
            data["prenom de la mère"],
            data["nom de la mère"],
            data["contact"],
            data["adresse"]
        
        ]
        super().addListe(eleve)

        #return super().addListe(data)

#test = GNotes(1)

#print(test.setListe(""))