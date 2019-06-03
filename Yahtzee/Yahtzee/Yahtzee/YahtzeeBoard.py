from tkinter import *
from tkinter import font
import tkinter.messagebox
from Player import *
from Dice import *
from Configuration import *

class YahtzeeBoard:
    UPPERTOTAL = 6
    UPPERBONUS = 7
    LOWERTOTAL = 15
    TOTAL = 16
    dice = []
    diceButtons = []
    fields = []

    players = []
    numPlayers = 0
    player = 0
    round = 0
    roll = 0

    def __init__(self):
        self.InitPlayers()
        self.pwindow = Tk()
        self.TempFont = font.Font(size=16, weight = 'bold', family = 'Consolas')
        self.label = []
        self.entry = []
        self.label.append(Label(self.pwindow, text = "플레이어   명수", font = self.TempFont))
        self.label[0].grid(row=0, column =0)

        for i in range(1,11):
            self.label.append(Label(self.pwindow, text="플레이어"+str(i)+"이름", font = self.TempFont))
            self.label[i].grid(row=i,column=0)
        
        for i in range(11):
            self.entry.append(Entry(self.pwindow,font=self.TempFont))
            self.entry[i].grid(row = i, column = 1)
        Button(self.pwindow, text="Yahtzee 플레이어 설정 완료",
               font = self.TempFont, command = self.playerNames).grid(row=11,column = 0)
        self.pwindow.mainloop()


    