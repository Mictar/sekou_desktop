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

    def addListe(self, data):
        """
        Description:
        ------------
            cette fonction ajoute de nouvelle donnée a la liste
        
        Parametre:
        ----------
            data : une liste
                il represent l nouvelle a enregistrer
        """
        #self._liste.update

    def getListe(self) -> OrderedDict:
        """
        """

        return (self._liste)
    
    def setListe(self, new_liste: OrderedDict):
        """
        
        """
        self._liste = new_liste
    
    def save(self):
        """
        Description:
        ------------
            cette fonction enregistre le 
        """
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
        classe_name = (f"{ELEVES_REP}/listes/liste {classe} année.ods")
        super().__init__(classe_name)
    

#test = GNotes(1)

#print(test.setListe(""))