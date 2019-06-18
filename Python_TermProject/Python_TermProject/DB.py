from API_Parsing import *
parseEngine = RiotApiParsing()

class DB:
    def __init__(self):
        self.__playerName = ''
        self.__PlayerID = ''
        self.__AccountID = ''

        self.rawChampion = {}
        self.ChampionIDDict = {}
        self.__Rank = []
        self.__Mastery = []
        self.__Matches = []

#<<<<<<<<<<<<<<<Set>>>>>>>>>>>>>>>
    def setChampionData(self, data):
        self.rawChampion = data
        data = data.items()
        for i in data:
            self.ChampionIDDict[int(i[1]['key'])] = i[0]

    def setName(self, name):
        self.__playerName = name

    def setID(self, IDs):
        self.__PlayerID = IDs[0]
        self.__AccountID = IDs[1]

    def setRank(self, data):
        self.__Rank = []
        for i in range(len(data)):#queueType, tier, rank, point, wins, losses
            tempData = (data[i].get('queueType'),
                        data[i].get('tier'),
                        data[i].get('rank'),
                        data[i].get('leaguePoints'),
                        data[i].get('wins'),
                        data[i].get('losses'))
            self.__Rank.append(tempData)

    def setMasteryTop3(self, data):
        self.__Mastery = []
        for i in range(3):
            tempData = (data[i].get('championId'),
                        data[i].get('championLevel'),
                        data[i].get('championPoints'))
            self.__Mastery.append(tempData)
        
    def setMatches(self, data):
        data = data.get('matches')
        self.__Matches = []
        for i in range(len(data)):
            tempData = (data[i].get('gameId'),
                        data[i].get('champion'),
                        data[i].get('queue'))
            self.__Matches.append(tempData)

    def LoadMatches(self, data, type):
        tempMatches = data.get('matches')
        matches = []
        for i in range(len(tempMatches)):
            tempData = (tempMatches[i].get('gameId'),
                        tempMatches[i].get('champion'))
            matches.append(tempData)

        TempCardDB = []
        for i in matches:
            #AccountID와 일치하는 participantId 찾기.
            tempData = parseEngine.getMatchByGameID(i[0])
            participant = tempData.get("participantIdentities")
            participantId = 0
            for j in participant:
                p = j.get("player")
                if(p.get("accountId") == self.__AccountID):
                    participantId = j.get("participantId")
                    break;
            
            #찾은 participantId로 나의 정보 찾기.
            participant = tempData.get("participants")
            stats = {}
            for j in participant:
                if(j.get("participantId") == participantId):
                    stats = j.get("stats")
                    break;
            kills = stats.get("kills")
            assists = stats.get("assists")
            win = stats.get("win")
            deaths = stats.get("deaths")
            TempCardDB.append((win, i[1], kills, assists, deaths))

        if(type == 'Entire'):
            self.__CardDB_Entire = TempCardDB
        elif(type == 'SoloRank'):
            self.__CardDB_SolRank = TempCardDB
        elif(type == 'Normal'):
            self.__CardDB_Normal = TempCardDB
        elif(type == 'ARAM'):
            self.__CardDB_ARAM = TempCardDB
        elif(type == 'FreeRank'):
            self.__CardDB_FreeRank = TempCardDB
#<<<<<<<<<<<<<<<Get>>>>>>>>>>>>>>>

    def getName(self):
        return self.__playerName
    
    def getPlayerID(self):
        return self.__PlayerID
    
    def getAccountID(self):
        return self.__AccountID

    def getRank(self):
        return self.__Rank

    def getMastery(self):
        return self.__Mastery

    def getMatches(self):
        return self.__Matches

    def chp_getIDtoName(self, id):
        return self.ChampionIDDict[int(id)]

    def getCardDB(self,type):
        if(type == 'Entire'):
            return self.__CardDB_Entire
        elif(type == 'SoloRank'):
            return self.__CardDB_SolRank
        elif(type == 'Normal'):
            return self.__CardDB_Normal
        elif(type == 'ARAM'):
            return self.__CardDB_ARAM
        elif(type == 'FreeRank'):
            return  self.__CardDB_FreeRank