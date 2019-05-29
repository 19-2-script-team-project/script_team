from tkinter import *
from tkinter.ttk import *
from tkinter.font import *

from API_Parsing import *
from DB import *
import random

#import GUI

class Interface:
    def __init__(self):
        self.__db = DB()
        self.__psEngine = RiotApiParsing()

        window = Tk()
        #window.geometry("500x1100+100+100")
        window.resizable(False, False)
        window.title("League Of Legends Search")
        #<<<<<<<<<<<<<<<<<<<<<<<<<<Frame1>>>>>>>>>>>>>>>>>>>>>>>>>>
        self.Frame1 = ttk.Frame(window, borderwidth = 2, width = 500, height = 100)
        self.Frame1.grid(row = 0, column = 0)
        LabelFrame
        #class 상속으로 구현
        F1_Font = Font(size = 15)
        
        playerButton = ttk.Button(self.Frame1, text = "플레이어", width = 20)
        playerButton.pack(side = "left", fill = "x", padx = 5)

        inGameButton = ttk.Button(self.Frame1, text = "인게임", width = 20)
        inGameButton.pack(side = "left", fill = "x", padx = 5)

        subFuncButton = ttk.Button(self.Frame1, text = "부가기능", width = 20)
        subFuncButton.pack(side = "left", fill = "x", padx = 5)

        #<<<<<<<<<<<<<<<<<<<<<<<<<<Frame2>>>>>>>>>>>>>>>>>>>>>>>>>>
        self.Frame2 = ttk.Frame(window, borderwidth = 2, width = 500, height = 1000)
        self.Frame2.grid(row = 1, column = 0)
        
        #<<<<<<<<<<<<<<<<<<<<<<<<<<Frame3>>>>>>>>>>>>>>>>>>>>>>>>>>
        self.Frame3 = ttk.Frame(self.Frame2, width = 500, height = 500)
        self.Frame3.grid(row = 0, column = 0)

        self.F2_SearchEntry = ttk.Entry(self.Frame3, text = "플레이어 이름", width = 50)
        self.F2_SearchEntry.grid(row = 0, column = 0)
        #self.F2_SearchEntry.bind("<Return>", func) 엔터 입력시 함수 실행.
        searchButton = ttk.Button(self.Frame3, text = "검색", width = 10, command = self.Btn_Search)
        searchButton.grid(row = 0, column = 1)  

        #<<<<<<<<<<<<<<<<<<<<<<<<<<FramePlayerInfo>>>>>>>>>>>>>>>>>>>>>>>>>>
        self.FramePlayerInfo = ttk.Frame(self.Frame3, width = 500, height = 300)
        self.FramePlayerInfo.grid(row = 1, column = 0, columnspan = 2)

        self.tierFrame = Frame(self.FramePlayerInfo, width = 250, height = 250)
        self.tierFrame.grid(row = 0, column = 0)
        
        self.mostFrame = Canvas(self.FramePlayerInfo, width = 250, height = 250)
        self.mostFrame.grid(row = 0, column = 1)

        #<<<<<<<<<<<<<<<<<<<<<<<<<<Frame4>>>>>>>>>>>>>>>>>>>>>>>>>>
        self.Frame4 = ttk.Frame(self.Frame2, width = 500, height = 500)#
        self.Frame4.grid(row = 1, column = 0)


        #<<<<<<<<<<<<<<<<<<<<<<<<<<FrameTab>>>>>>>>>>>>>>>>>>>>>>>>>>
        notebook = Notebook(self.Frame4, width = 500)
        FrameTab_entire = ttk.Frame(self.Frame4, width = 500, height = 300)
        FrameTab_soloRank = ttk.Frame(self.Frame4, width = 500, height = 300)
        FrameTab_normal = ttk.Frame(self.Frame4, width = 500, height = 300)
        FrameTab_ARAM = ttk.Frame(self.Frame4, width = 500, height = 300)
        FrameTab_freeRank = ttk.Frame(self.Frame4, width = 500, height = 300)
        
        notebook.add(FrameTab_entire, text="전체") 
        notebook.add(FrameTab_soloRank, text="솔랭") 
        notebook.add(FrameTab_normal, text="일반") 
        notebook.add(FrameTab_ARAM, text="칼바람") 
        notebook.add(FrameTab_freeRank, text="자유랭")
        #notebook.bind_all("<<NotebookTabChanged>>", self.tabChangedEvent) 
        notebook.pack()

        window.mainloop()

#<<<<<<<<<<<EVENT>>>>>>>>>>
    def Btn_Search(self):
        name = self.F2_SearchEntry.get()
        ID, AccountID = self.__psEngine.getPlayerIDByName(name)
        self.__db.setName(name)
        self.__db.setID((ID, AccountID))
        self.__db.setRank(self.__psEngine.getPlayerLeagueByPlayerID(ID))
        self.__db.setMasteryTop3(self.__psEngine.getChampionMasteryByPlayerID(ID))
        self.__db.setMatches(self.__psEngine.getMatchsByAccountID(AccountID, None, None))
        
        self.update_Search()
#<<<<<<<<<<<UPDATE>>>>>>>>>>
    def update_Search(self):
        #RANK DRAW
        rank = self.__db.getRank()
        canvas = Canvas(self.tierFrame, bg = "skyblue", width = 180, height = 180 )
        canvas.pack()
        #img = PhotoImage(file = "tierImg/" + rank[0][1] + ".gif") #rank
        #canvas.create_image(0,0,image = img)

        Label(self.tierFrame, text = rank[0][0]).pack()
        Label(self.tierFrame, text = rank[0][1]).pack()
        Label(self.tierFrame, text = rank[0][2]).pack()
        Label(self.tierFrame, text = str(rank[0][3]) + "LP").pack()


Interface()