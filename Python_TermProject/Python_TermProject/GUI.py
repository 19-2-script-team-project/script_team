from tkinter import *

class imgButton(Label) : 
    def __init__(self, container, imgFile, func = None):
        self.Image = PhotoImage(file = imgFile)

        Label.__init__(self, container, image = self.Image, bg = 'black')
        self.bind("<Button-1>", func)
