from tkinter import*
from desktop.menu.menu import KMenu
from desktop.utils.tableau import Tableau

import os
rep = "/home/moctar/Bureau/sekou_cisse/sekou_desktop/desktop/desktop/core/data/eleves/listes/"
os.system(f"cd {rep} && make")

def onFrameConfigure(canvas):
      '''Reset the scroll region to encompass the inner frame'''
      canvas.configure(scrollregion=canvas.bbox("all"))
    

root = Tk()
root.geometry("600x600")
root.title("Sekou School")

#frame = Frame(root, width=400, height=400)
#can = Canvas(frame)

#frame.bind("<Configure>", lambda event, can=can : onFrameConfigure(can))
#tab = Tableau(root, 5, 6)
#can.grid()
#frame.grid()
menu = KMenu(root)
root.config(menu=menu)

root.mainloop()
