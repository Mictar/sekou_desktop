from tkinter import Label

class Label(Label):

    def get(self):
        return self["text"]