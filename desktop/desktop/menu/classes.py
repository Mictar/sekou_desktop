from tkinter import*

class Classes(Menu):
    def __init__(self, fenetre, menu:Menu, objects):

        super().__init__(menu)
        
        for i in range(1, 10):

            self.add_command(label= ( str(i) + " année"),\
                 command=objects(fenetre, classe=i).view)