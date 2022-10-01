from tkinter import *

class Tableau(object):
    def __init__(self, fenetre, rows: int, columns: int):
        
        self._cellule = [ [ Entry(fenetre) for y in range(columns)] for i in range(rows)]

        for column in range(columns):
            for row in range(rows):
                self._cellule[row][column].grid(row=row, column=column)
    
    def getCellule(self, row: int, column: int):

        return self._cellule[row][column]
    
    def add_rows(self):
        """
        Description:
        ------------
            cette fonction ajoute une ligne de tableau
            dans le tableau actuel
        """
    
    def add_colums(self):
        """
        Description:
        ------------
            cette fonction ajoute une column au tableau 
            actuel
        """
    
    def sup_row(self):
        """
        Description:
        ------------
            cette fonction supprime une line au tableau
            actuel
        """
    
    def sup_columns(self):
        """
        Description:
        ------------
            cette fonction supprime une colonne au tableau actuel
        """
    
    def paste(self):
        """
        Description:
        ------------
            cette fonction colle les données dans le tableau
        """
    
    def copie(self):
        """
        Description:
        ------------
            cette fonction copie une colonne ou une ligne
            ou les deux ensemble
        """
                
