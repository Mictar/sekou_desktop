from tkinter import BooleanVar, Checkbutton

class Checkbutton(Checkbutton):
    def __init__(self, root, text=""):
        self._values = BooleanVar()
        super().__init__(root, text=text, variable=self._values)
    def get(self):
        return self._values.get()