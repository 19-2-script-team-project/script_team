from tkinter import *
from tkinter.ttk import *
from tkinter.font import *
from gmail import *
from GUI import *
from ScrolledWindow import *
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
        self.window.title("League Of Legends Search")

        #<<<<<<<<<imgList_Initialize>>>>>>>>>>>>
        self.imgChampionDict = {}
        self.imgTierDict = {}
        TierList = ['BRONZE','CHALLENGER','DIAMOND','GOLD','GRANDMASTER','IRON','MASTER','PLATINUM','SILVER']
        
        for i in self.__db.ChampionIDDict.items():
            self.imgChampionDict[i[0]] = PhotoImage(file = 'images/image_'+ i[1] +'.gif')

        for i in TierList:
            self.imgTierDict[i] = PhotoImage(file='tierImg/AM_'+ i +'.png')

        #<<<<<<<<<<STYLING>>>>>>>>>>>>
        customStyle = ttk.Style()
       
        customStyle.theme_create( "CUSTOM", settings = {
        "TNotebook": {"configure": { "background" : 'black', "tabmargins" : [40,3], "bordercolor" : 'black'} },
        "TNotebook.Tab": {
            "configure": {"padding": [15, 2], "foreground" : 'white', "background": 'black' },
            "map":       {"background": [("selected", 'gray20'), ("active", 'gray30')]} } } )

        customStyle.theme_use("CUSTOM")

        #<<<<<<<<<<<<<<<<<<<<<<<<<<Background Image>>>>>>>>>>>>>>>>>>>>>
        img = PhotoImage(file='UI/Background.png')
        Label(self.window, image = img ).pack()
        
        #<<<<<<<<<<<<<<<<<<<<<<<<<<Menu_Btns>>>>>>>>>>>>>>>>>>>>>>>>>> 다시 imgBtn으로
        playerBtnImg = PhotoImage(file='UI/Player.png')
        Button(self.window, image = playerBtnImg, borderwidth=0, highlightthickness=0).place(x = 20, y = 20)
       
        ingameBtnImg = PhotoImage(file='UI/InGame.png')
        Button(self.window, image = ingameBtnImg, borderwidth=0, highlightthickness=0).place(x = 20 + 100, y = 20)

        subfuncBtnImg = PhotoImage(file='UI/SubFucn.png')
        Button(self.window, image = subfuncBtnImg, borderwidth=0, highlightthickness=0, command = self.Btn_SubFunc).place(x = 20 + 100 + 100, y = 20)
        
        searchBtnImg = PhotoImage(file='UI/Search.png')
        Button(self.window, image = searchBtnImg, borderwidth=0, highlightthickness=0, command = self.Btn_Search).place(x = 400, y = 20)
  
        #<<<<<<<<<<<<<<<<<<<<<<<<<<SearchEntry>>>>>>>>>>>>>>>>>>>>>>>>>>

        self.F2_SearchEntry = Entry(self.window, justify = 'center', bg = 'gray5', fg = 'white',  font = ('HY견고딕', 30), width = 18)
        self.F2_SearchEntry.bind("<Return>", self.Btn_Search) #엔터 입력시 함수 실행.
        self.F2_SearchEntry.place(x = 20, y = 48)

        #<<<<<<<<<<<<<<<<<<<<<<<<Tier Info>>>>>>>>>>>>>>>>>>>>>>>
        tierInfo = Frame(self.window, bg = 'black')
        tierInfo.place(x = 52, y = 245)

        self.tierImgLabel = Label(self.window, image = self.imgTierDict['CHALLENGER'], relief = 'flat')#, image = self.imgTierDict['CHALLENGER']
        self.tierImgLabel["borderwidth"] = 0

        self.tierQueueLabel = Label(tierInfo, text = 'RANKED_SOLO_5x5', bg = 'black', fg = 'white', font = ('gothic', 8))
        self.tierNameLabel = Label(tierInfo, text = 'Tier', bg = 'black', fg = 'white', font = ('gothic', 8))
        self.tierRankLabel = Label(tierInfo, text = 'Rank', bg = 'black', fg = 'white', font = ('gothic', 8))
        self.tierLPLabel = Label(tierInfo, text = "LP", bg = 'black', fg = 'white', font = ('gothic', 8))
        self.tierImgLabel.place(x = 40, y = 115)
        self.tierQueueLabel.pack(side = 'top')
        self.tierNameLabel.pack(side = 'top')
        self.tierRankLabel.pack(side = 'top')
        self.tierLPLabel.pack(side = 'top')

        #<<<<<<<<<<<<<<<<<<<<<<<<mostLabelLIst>>>>>>>>>>>>>>>>>>>>>>>
        
        self.mostLabelList = []
        for i in range(3):
            self.mostLabelList.append(Label(self.window, text = 'Top ' + str(i + 1) + '\nPoint', image = self.imgChampionDict[1], justify = 'center', compound = 'top', bg = 'gray10', fg = 'white'))
            self.mostLabelList[i].place( x = 230 + (90 * i), y = 115)

        #<<<<<<<<<<<<<<<<<<<<<<<<<<FrameTab>>>>>>>>>>>>>>>>>>>>>>>>>> scroll 적용.
        
        self.tabFrame = Frame(self.window, bg = 'black')
        self.tabFrame.place(x = 20, y = 350)

        self.scoreNotebook = ttk.Notebook(self.tabFrame)
        
        self.FrameTab_entire = Frame(self.tabFrame, bg = 'black', width = 460, height = 400)
        self.FrameTab_soloRank = Frame(self.tabFrame, bg = 'black', width = 460, height = 400)
        self.FrameTab_normal = Frame(self.tabFrame, bg = 'black', width = 460, height = 400)
        self.FrameTab_ARAM = Frame(self.tabFrame, bg = 'black', width = 460, height = 400)
        self.FrameTab_freeRank = Frame(self.tabFrame, bg = 'black', width = 460, height = 400)
        
        self.TabComplete = [False for i in range(5)]

        self.scoreNotebook.add(self.FrameTab_entire, text="  전체  ") 
        self.scoreNotebook.add(self.FrameTab_soloRank, text="  솔랭  ") 
        self.scoreNotebook.add(self.FrameTab_normal, text="  일반  ") 
        self.scoreNotebook.add(self.FrameTab_ARAM, text=" 칼바람 ") 
        self.scoreNotebook.add(self.FrameTab_freeRank, text=" 자유랭 ")
        self.scoreNotebook.bind_all("<<NotebookTabChanged>>", self.tabChangedEvent) 
        

        self.scoreNotebook.pack()
        
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
        self.__db.LoadMatches(self.__psEngine.getMatchsByAccountID(AccountID, None, None), 'Entire')
        print('Load Entire')

        self.update_Search()

    def tabChangedEvent(self, event):
        if(self.scoreNotebook.index('current') == 0 and not self.TabComplete[0]):
            self.__db.LoadMatches(self.__psEngine.getMatchsByAccountID(self.__db.getAccountID(), None, None), 'Entire')
            print('Load Entire')
            ScrolledFrame_Rank(self.FrameTab_entire,   self.__db.getCardDB('Entire'), self.imgChampionDict)
            print('Draw Entire')
            self.TabComplete[0] = True

        elif(self.scoreNotebook.index('current') == 1 and not self.TabComplete[1]):
            self.__db.LoadMatches(self.__psEngine.getMatchsByAccountID(self.__db.getAccountID(), None, 420), 'SoloRank')
            print('Load SoloRank')
            ScrolledFrame_Rank(self.FrameTab_soloRank, self.__db.getCardDB('SoloRank'), self.imgChampionDict)
            print('Draw SoloRank')
            self.TabComplete[1] = True

        elif(self.scoreNotebook.index('current') == 2 and not self.TabComplete[2]):
            self.__db.LoadMatches(self.__psEngine.getMatchsByAccountID(self.__db.getAccountID(), None, 430), 'Normal')
            print('Load Normal')
            ScrolledFrame_Rank(self.FrameTab_normal,   self.__db.getCardDB('Normal'), self.imgChampionDict)
            print('Draw Normal')
            self.TabComplete[2] = True

        elif(self.scoreNotebook.index('current') == 3 and not self.TabComplete[3]):
            self.__db.LoadMatches(self.__psEngine.getMatchsByAccountID(self.__db.getAccountID(), None, 450), 'ARAM')
            print('Load ARAM')
            ScrolledFrame_Rank(self.FrameTab_ARAM,     self.__db.getCardDB('ARAM'), self.imgChampionDict)
            print('Draw ARAM')
            self.TabComplete[3] = True

        elif(self.scoreNotebook.index('current') == 4 and not self.TabComplete[4]):
            self.__db.LoadMatches(self.__psEngine.getMatchsByAccountID(self.__db.getAccountID(), None, 440), 'FreeRank')
            print('Load FreeRank')
            ScrolledFrame_Rank(self.FrameTab_freeRank, self.__db.getCardDB('FreeRank'), self.imgChampionDict)
            print('Draw FreeRank')
            self.TabComplete[4] = True

#<<<<<<<<<<<UPDATE>>>>>>>>>>

    def update_Search(self):
        #RANK DRAW
        rank = self.__db.getRank()       
        most = self.__db.getMastery()
        #Tier Info
        self.tierImgLabel.configure(image = self.imgTierDict[rank[0][1]])
        self.tierQueueLabel.configure(text = rank[0][0])
        self.tierNameLabel.configure(text = rank[0][1])
        self.tierRankLabel.configure(text = rank[0][2])
        self.tierLPLabel.configure(text = rank[0][3])
        #Most List
        for i in range(len(most)):
            self.mostLabelList[i].configure(image = self.imgChampionDict[most[i][0]], text = 'Top ' + str(i + 1) + '\n' + str(most[i][2]) + 'Pt')
        AccountID =  self.__db.getAccountID()
        ScrolledFrame_Rank(self.FrameTab_entire,   self.__db.getCardDB('Entire'), self.imgChampionDict)
        print('Draw Entire')
        self.TabComplete[0] = True

Interface()