from tkinter import *


class ScrolledFrame_Rank(Frame):
    def __init__(self, root, CardDB, img, *args, **kwargs):
        self.img = img
        self.CardDB = CardDB

        Frame.__init__(self, root, *args, **kwargs)
        self.canvas = Canvas(root, bg = 'black')
        self.frame = Frame(self.canvas, bg = 'black')
        self.vsb = Scrollbar(root, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.vsb.set)

        self.vsb.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)
        self.canvas.create_window((4,4), window=self.frame, anchor="nw", 
                                  tags="self.frame")

        self.frame.bind("<Configure>", self.onFrameConfigure)
        self.populate()
        
    def populate(self):
        
        for i in range(len(self.CardDB)):
            color = ''
            if(self.CardDB[i][0]):
                color = 'dark blue'
            else:
                color = 'dark red'
            CardFrame = Frame(self.frame, bg = color, relief="solid")
            CardFrame.grid(row = i // 5, column = i % 5)
            Label(CardFrame, image = self.img[self.CardDB[i][1]], bg = color, fg = 'white').pack(side = 'top')

            Label(CardFrame, text= str(self.CardDB[i][2]) +
                  '/' + str(self.CardDB[i][4]) +
                  '/' + str(self.CardDB[i][3]), bg = color, fg = 'white',
                  font = ('HY견고딕', 12)).pack(side = 'top')

    def onFrameConfigure(self, event):
        '''Reset the scroll region to encompass the inner frame'''
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
