from tkinter import *
from tkinter.ttk import *
from tkinter.font import *
from gmail import *
from GUI import *

from API_Parsing import *
from DB import *
import random

#import GUI

class Interface:
    def __init__(self):
        self.__db = DB()
        self.__psEngine = RiotApiParsing()
        self.__db.setChampionData(self.__psEngine.getAllChampionsData())
        
        self.window = Tk()
        self.window.geometry("500x800")
        self.window.resizable(False, False)

        #<<<<<<<<<imgList_Initialize>>>>>>>>>>>>
        self.imgChampionDict = {}
        self.imgTierDict = {}
        TierList = ['BRONZE','CHALLENGER','DIAMOND','GOLD','GRANDMASTER','IRON','MASTER','PLATINUM','SILVER']
        
        for i in self.__db.ChampionIDDict.items():
            self.imgChampionDict[i[0]] = PhotoImage(file = 'images/image_'+ i[1] +'.gif')

        for i in TierList:
            self.imgTierDict[i] = PhotoImage(file='tierImg/'+ i +'.gif')

        self.window.title("League Of Legends Search")
        #<<<<<<<<<<<<<<<<<<<<<<<<<<Background Image>>>>>>>>>>>>>>>>>>>>>
        img = PhotoImage(file='UI/Background.png')
        Label(self.window, image = img ).pack()

        #<<<<<<<<<<<<<<<<<<<<<<<<<<Menu_Btns>>>>>>>>>>>>>>>>>>>>>>>>>>
        
        imgButton(self.window, 'UI/PLAYER.png').place(x = 20, y = 20)
        imgButton(self.window, 'UI/INGAME.png').place(x = 20 + 80, y = 20)
        imgButton(self.window, 'UI/SUBFUNC.png', self.Btn_SubFunc).place(x = 20 + 80 + 80, y = 20)
        ttk.Button(self.window, text = "검색", width = 10, command = self.Btn_Search).place(x = 400, y = 20)
  
        #<<<<<<<<<<<<<<<<<<<<<<<<<<SearchEntry>>>>>>>>>>>>>>>>>>>>>>>>>> 과제 : 크기 맞추기.

        self.F2_SearchEntry = Entry(self.window, justify = 'center', bg = 'black', fg = 'white',  font = ('HY견고딕', 40), width = 15)
        self.F2_SearchEntry.bind("<Return>", self.Btn_Search) #엔터 입력시 함수 실행.
        self.F2_SearchEntry.place(x = 40, y = 45)

        #<<<<<<<<<<<<<<<<<<<<<<<<Tier Info>>>>>>>>>>>>>>>>>>>>>>>
        tierInfo = Frame(self.window)
        tierInfo.place(x = 100, y = 245)

        self.tierImgLabel = Label(self.window)#, image = self.imgTierDict['CHALLENGER']
        self.tierQueueLabel = Label(tierInfo, text = 'QueueType', bg = 'black', fg = 'white', font = ('gothic', 7))
        self.tierNameLabel = Label(tierInfo, text = 'Tier', bg = 'black', fg = 'white', font = ('gothic', 7))
        self.tierRankLabel = Label(tierInfo, text = 'Rank', bg = 'black', fg = 'white', font = ('gothic', 7))
        self.tierLPLabel = Label(tierInfo, text = "LP", bg = 'black', fg = 'white', font = ('gothic', 7))
        self.tierImgLabel.place(x = 40, y = 115)
        self.tierQueueLabel.pack(side = 'top')
        self.tierNameLabel.pack(side = 'top')
        self.tierRankLabel.pack(side = 'top')
        self.tierLPLabel.pack(side = 'top')

        #<<<<<<<<<<<<<<<<<<<<<<<<mostLabelLIst>>>>>>>>>>>>>>>>>>>>>>>
        
        self.mostLabelList = []
        for i in range(3):
            self.mostLabelList.append(Label(self.window, text = 'Point', image = self.imgChampionDict[1], compound = 'top'))
            self.mostLabelList[i].place( x = 230 + (90 * i), y = 115)
        #<<<<<<<<<<<<<<<<<<<<<<<<<<Frame4>>>>>>>>>>>>>>>>>>>>>>>>>>

        self.tabFrame = Frame(self.window, bg = 'black')#
        self.tabFrame.place(x = 20, y = 300)

        #<<<<<<<<<<<<<<<<<<<<<<<<<<FrameTab>>>>>>>>>>>>>>>>>>>>>>>>>> 과제 : style 사용.
        notebook = tkinter.ttk.Notebook(self.tabFrame)
        FrameTab_entire = Canvas(self.tabFrame, bg = 'black', width = 460, height = 460)
        FrameTab_soloRank = Canvas(self.tabFrame, bg = 'black', width = 460, height = 460)
        FrameTab_normal = Canvas(self.tabFrame, bg = 'black', width = 460, height = 460)
        FrameTab_ARAM = Canvas(self.tabFrame, bg = 'black', width = 460, height = 460)
        FrameTab_freeRank = Canvas(self.tabFrame, bg = 'black', width = 460, height = 460)
        
        notebook.add(FrameTab_entire, text="전체") 
        notebook.add(FrameTab_soloRank, text="솔랭") 
        notebook.add(FrameTab_normal, text="일반") 
        notebook.add(FrameTab_ARAM, text="칼바람") 
        notebook.add(FrameTab_freeRank, text="자유랭")
        #notebook.bind_all("<<NotebookTabChanged>>", self.tabChangedEvent) 

        notebook.pack()
        
        self.window.mainloop()

#<<<<<<<<<<<EVENT>>>>>>>>>>
    def Btn_EmailSend(self):
        recipientAddr = self.SF_Entry.get()
        mail_service = Mail_Service()
        mail_service.send_to_massage(recipientAddr, "전적 전송", str(self.__psEngine.getMatchsByAccountID(self.__db.getAccountID(),None,None)))
        print('완료')

    def Btn_DrawGraph(self):
        graphWindow = Toplevel(self.subFuncWindow)
        
        Matches = self.__db.getMatches()
        print(Matches)

        graphData = {}
        for i in Matches:
            if i[1] in graphData:
                graphData[i[1]] += 1
            else:
                graphData[i[1]] = 1
        print(graphData)
        value = graphData.values()
        maxCount = int(max(value))

        Width = 500
        Height = 300
        graphCanvas = Canvas(graphWindow, width = Width, height = Height, bg = 'white')
        graphCanvas.pack()
        graphCanvas.create_line(10, Height - 10, Width - 10, Height - 10)
        barW = (Width - 20) / len(graphData)
        graphData = list(graphData)
        value = list(value)
        for i in range(len(graphData)):
            graphCanvas.create_rectangle(i * barW + 10, Height - (Height - 20) * value[i] / maxCount,
                   (i + 1) * barW+10, Height - 10, fill = 'yellow', tags = "grim")
            graphCanvas.create_text(i*barW + 10 + 20, Height - 10+5, text = self.__db.chp_getIDtoName(graphData[i]), tags = "grim")
            graphCanvas.create_text(i*barW + 10 + 20, Height - (Height - 20) * value[i] / maxCount - 5,
                                   text = str(value[i]), tags = "grim")
        

    def Btn_SubFunc(self, event = None):
        
        self.subFuncWindow = Toplevel(self.window)
        self.subFuncWindow.geometry("200x100")
        Label(self.subFuncWindow, text = '전적 정보 이메일 전송',).pack(side = 'top')
        self.SF_Entry = Entry(self.subFuncWindow)
        self.SF_Entry.pack(side = 'top', fill = 'x')
        Button(self.subFuncWindow, text = "이메일 전송", command = self.Btn_EmailSend).pack(side = 'top', fill = "x")
        Button(self.subFuncWindow, text = "현재 전적 Champion Graph 출력", command = self.Btn_DrawGraph).pack(side = 'top', fill = "x")


    def Btn_Search(self, event = None):
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
        most = self.__db.getMastery()
        
        self.tierImgLabel.configure(image = self.imgTierDict[rank[0][1]])
        self.tierQueueLabel.configure(text = rank[0][0])
        self.tierNameLabel.configure(text = rank[0][1])
        self.tierRankLabel.configure(text = rank[0][2])
        self.tierLPLabel.configure(text = rank[0][3])

        for i in range(len(most)):
            self.mostLabelList[i].configure(image = self.imgChampionDict[most[i][0]], text = str(most[i][2]) + 'Pt')

            

Interface()