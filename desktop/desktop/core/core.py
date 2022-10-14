from fileinput import filename
import glob
from  pyexcel_ods3 import get_data, save_data
from desktop.core.config import NOTES_REP, ELEVES_REP, BULLETIN_REP, PAYEMENT_REP
from collections import OrderedDict

import pandas as pd

from .config import PAYEMENT_REP_S
import json

import os


class StoreFile(object):

    def __init__(self, file_name: str):
        """

        """
        #self._liste = get_data(file_name)

        self._file_name = file_name

        #self._liste = pd.read_excel(file_name,engine="odf")

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
        
    
    def getListe(self) -> pd.DataFrame:
        """
        """

        return pd.read_excel(self._file_name, engine="odf")
    
    def getJson(self, file_name):
        with open(file_name) as fp:
            return json.load(fp)
            
    def saveJson(self, file_name: str, data):
        """
        Description:
        ------------
            cette fonction est savegarder les donnees
            au formant json
        
        Parametre:
        ----------
            file_name: le nom du fichier
            data: un object
        """
        
        with open(file_name, "w") as fp:
            json.dump(data, fp, indent=True)
        

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
    def save(self, data: pd.DataFrame, file_name="", ):
        """
        Description:
        ------------
            cette fonction enregistre le 
        """

        data.to_excel(file_name, index=False, engine="odf")
        
        

class GNotes(StoreFile):
    """
    Description:
    ------------
        cette classe assure la gestion des notes des élèves

    """
    def __init__(self, classe: int) -> None:
        self.classe_name = (f"{NOTES_REP}/listes/liste {classe} année.ods")

        super().__init__(self.classe_name)
    
    def saveJson(self, data):
        """
        Description:
        ------------
            cette fonction permet de sauvegarder les notes
            dans un fichier de formant json

        """
        matiere = data['header']['matiere']
        types = data["header"]["type"]
        classe = data["header"]["classe"]
        numero = data["header"]["numero"]

        file_name_add = f"{NOTES_REP}/{types}/{matiere}_{classe}_{numero}.json"
        
        super().saveJson(file_name_add, data)
    
    def getJson(self, types, classe, matiere, numero):

        notes_list = glob.glob(f"{NOTES_REP}/{types}/*.json")

        #print(notes_list)

        file_name = f"{NOTES_REP}/{types}/{matiere}_{classe}_{numero}.json"
        
        #print(file_name)

        if file_name  in notes_list:

            with open(file_name) as fp:
            
                return json.load(fp)


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
    def __init__(self, classe: int, montant: int = 0):
        classe_name = (f"{PAYEMENT_REP}/listes/liste {classe} année.ods")

        self.montant = montant

        super().__init__(classe_name)
    
    def getJson(self, mois, classe):
        """
        """

        mois_list = glob.glob(f"{PAYEMENT_REP_S}/*.json")
        #print(mois_list)

        if f"{PAYEMENT_REP_S}/{mois}_{classe}.json"  in mois_list:
            with open(f"{PAYEMENT_REP_S}/{mois}_{classe}.json") as fp:
                return json.load(fp)

    def saveJson(self, data):
        """
        Description:
        ------------
            
        """
        file_name_add = f"{PAYEMENT_REP_S}/{data['header']['mois']}_{data['header']['classe']}.json"

        """if os.path.isfile(file_name_add):
            return False"""
        super().saveJson(file_name_add, data)

        #return True
    
    
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
            #data["contact"],
            #data["adresse"]
        
        ]
    def save(self, data: pd.DataFrame):
        
        super().save(data, self._classe_name)
        
        #super().addListe(eleve)
    
        #return super().addListe(data)

#test = GNotes(1)

#print(test.setListe(""))