from tkinter import *

class Cell(Label) : 
    def __init__(self, container, imgFile):
        self.Image = PhotoImage(file = imgFile)

        Label.__init__(self, container, image = self.Image)
        self.data = ' '
        self.bind("<Button-1>", self.click)

    def click(self, event):
       pass
