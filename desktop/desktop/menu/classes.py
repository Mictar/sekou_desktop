from tkinter import*
from desktop.menu.forms import Form

class Classes(Menu):
    def __init__(self, fenetre, menu:Menu, objects):

        super().__init__(menu)
        
        for i in range(1, 10):

            self.add_command(label= ( str(i) + " année"),\
                 command=objects(fenetre, classe=i).view)
    
    

class Cadre(Form):
    def __init__(self, fenetre, row=0, col=0) -> None:

        # position de la ligne en cour
        self._current_row = row

        # position de la colonne en cour
        self._current_col = col

        taille = None

        # donnée interne de la fenetre
        self._data = None

        # la fenetre ou les composant seront ajouter
        self._fenetre = fenetre

        # le conteneur de composant
        self._body = {}

        # initialisation de form
        Form.__init__(self, fenetre, )

    def getBodyShape(self) -> tuple:
        """
        Description:
        ------------
            cette fonction fournie la taille de la fenetre
            principale
        """

    def addLabel(self, labels_names: list,
                orient="vertical",):
        """
        Description:
        ------------
            cette fonction ajoutes des colonne
            dans le frame
        """
        labels = [Label(self.frame, text=i) for i in labels_names]

        self._body.append(labels)
    
    def addEntry(self, taille: int):
        """
        
        """
        entry = [Entry(self.frame) for i in range(taille)]

        self._body.append(entry)

    def grid(self, composant, orient: str = "vertical"):
        
        if orient == "vertical":

            for i in enumerate(composant):
                self._current_col += 1
                i.grid(row=self._current_row,
                       col=self._current_col)
        else:
            for i in enumerate(composant):
                self._current_row += 1
                i.grid(row=self._current_row,
                       col=self._current_col)
            
    def view(self):
        """
        Description:
        ------------
            cette fonction serve de rendu des composant
            graphique
        """
        self.load_data()

        # initiliasation de la fenetre
        self.initilise()

        # initialisation d'entête de la fenetre
        self.head()

        # initialisation du pied de la fenetre
        self.foot()
        
    def head(self):
        """
        Description:
            entête de la fenetre
        """
    
    def foot(self):
        """
        Description:
        ------------
            pied de la fenetre
        """

    def load_data(self, loader):
        """
        Description:
        ------------
            cette fonction charge les donneé necessaire
            avant le rendu
        """

        self._data = loader()

    def setPos(self, row: int, col: int):
        """
        Description:
        ------------
            cette fonction reactialise a nouveau
            la position en cours de la colonne et
            de la ligne
        """
        self._current_col = col,
        self._current_row = row

    def addComposant(self, composant, pos=""):
        """
        Description:
        ------------
            cette fonction ajoute des nouveau composant
            a l'object

        Parametre:
        ----------
            composant: un object ajouter
            pos: ["d", "g", "b", "h", "c"]
        """

        self._composant.append(composant(self._fenetre))
        if "d":
            self._current_row += 1
            self._composant[-1].grid(row=self._current_row,
                                     col=self._current_col)

        elif "b":
            self._current_col += 1
            self._composant[-1].grid(row=self._current_col)
