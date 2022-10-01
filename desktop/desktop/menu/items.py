
from menu.forms import Form

class ItemEleve(Form):
    """
    Desciption:
    -----------
        cette classe est charger du rendu
        d'une formulaire d'un élève avec un en tête,
        un corps et un pieds de page
    """
    def __init__(self, fenetre, classe, body=[], header=[], footer=[]):
        """
        """
        self._fenetre = fenetre
        super().__init__(self._fenetre, body)
    
    def view(self):
        """
        Description:
        ------------
            cette fonction assure le rendu de l'item
        
        """
    
    def cmd(self):
        """
        Description:
        ------------
            cette fonction assure
        """
        self._save()

    def getValues(self):
        """
        """