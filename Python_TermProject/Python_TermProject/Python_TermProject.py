from tkinter import *
from tkinter.ttk import *
from tkinter.font import *

import random
import GUI

class Interface:
    def __init__(self):
        global L1
        window = Tk()

        #<<<<<<<<<<<<<<<<<<<<<<<<<<Frame1>>>>>>>>>>>>>>>>>>>>>>>>>>
        self.Frame1 = ttk.Frame(window, borderwidth = 2, width = 500, height = 100)
        self.Frame1.grid(row = 0, column = 0)

        #class 상속으로 구현
        F1_Font = Font(size = 15)

        playerButton = ttk.Button(self.Frame1, text = "플레이어", width = 20)
        playerButton.grid(row = 0, column = 0)

        inGameButton = ttk.Button(self.Frame1, text = "인게임", width = 20)
        inGameButton.grid(row = 0, column = 1)

        subFuncButton = ttk.Button(self.Frame1, text = "부가기능", width = 20)
        subFuncButton.grid(row = 0, column = 2)

        #<<<<<<<<<<<<<<<<<<<<<<<<<<Frame2>>>>>>>>>>>>>>>>>>>>>>>>>>
        self.Frame2 = ttk.Frame(window, borderwidth = 2, width = 500, height = 1000)
        self.Frame2.grid(row = 1, column = 0)
        
        

        #<<<<<<<<<<<<<<<<<<<<<<<<<<Frame3>>>>>>>>>>>>>>>>>>>>>>>>>>
        self.Frame3 = ttk.Frame(self.Frame2, width = 500, height = 500)
        self.Frame3.grid(row = 0, column = 0)

        self.F2_SearchEntry = ttk.Entry(self.Frame3, text = "플레이어 이름", width = 50)
        self.F2_SearchEntry.grid(row = 0, column = 0)
        
        searchButton = ttk.Button(self.Frame3, text = "검색", width = 10)
        searchButton.grid(row = 0, column = 1)  

        #<<<<<<<<<<<<<<<<<<<<<<<<<<FramePlayerInfo>>>>>>>>>>>>>>>>>>>>>>>>>>
        self.FramePlayerInfo = ttk.Frame(self.Frame3, width = 500, height = 300)
        self.FramePlayerInfo.grid(row = 1, column = 0, columnspan = 2)

        self.tierCanvas = Canvas(self.FramePlayerInfo, bg = 'red', width = 250, height = 250)
        self.tierCanvas.grid(row = 0, column = 0)
        self.mostChamp = Canvas(self.FramePlayerInfo, bg = 'blue', width = 250, height = 250)
        self.mostChamp.grid(row = 0, column = 1)

        #<<<<<<<<<<<<<<<<<<<<<<<<<<Frame4>>>>>>>>>>>>>>>>>>>>>>>>>>
        self.Frame4 = ttk.Frame(self.Frame2, width = 500, height = 500)#
        self.Frame4.grid(row = 1, column = 0)


        #<<<<<<<<<<<<<<<<<<<<<<<<<<FrameTab>>>>>>>>>>>>>>>>>>>>>>>>>>
        self.FrameTab = ttk.Frame(self.Frame4)#, width = 500, height = 100
        self.FrameTab.grid(row = 0, column = 0)

        Tab_entireButton = ttk.Button(self.FrameTab, text = "전체", width = 15)
        Tab_entireButton.grid(row = 0, column = 0)

        Tab_soloRankButton = ttk.Button(self.FrameTab, text = "솔랭", width = 15)
        Tab_soloRankButton.grid(row = 0, column = 1)

        Tab_normalButton = ttk.Button(self.FrameTab, text = "일반", width = 15)
        Tab_normalButton.grid(row = 0, column = 2)

        Tab_ARAMButton = ttk.Button(self.FrameTab, text = "칼바람", width = 15)
        Tab_ARAMButton.grid(row = 0, column = 3)

        #<<<<<<<<<<<<<<<<<<<<<<<<<<Frame5>>>>>>>>>>>>>>>>>>>>>>>>>>
        self.Frame5 = ttk.Frame(self.Frame4)#, width = 500, height = 400
        self.Frame5.grid(row = 1, column = 0, columnspan = 4)
        self.scoreCanvas = Canvas(self.Frame5, bg = 'skyblue', width = 500, height = 250)
        self.scoreCanvas.pack()
       



        
        #L1 = Label(frame2, text = "게임중...")
        #L1.pack()
        
        window.mainloop()


Interface()