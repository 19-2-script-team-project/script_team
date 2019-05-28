        
        #5GHaky xhpMDatlPQddXaIoAqs3tqgHNuJY0Q2IwG_3ztonj0WSyeo
        #kmmjEmPIS8vz7KeNTCEJegBOZPIObRoxMoQh8vHoXGzm
        #uyLDF9li-2kVsPToVrhGDcwSUXkr007gQ5wK9_a0C_HzBCQ
import webbrowser
import urllib.request
import urllib.parse

import json
import os

from tkinter import *
from tkinter.ttk import *

from tkinter.font import *
import http.client

#JSON 파일을 딕셔너리로 파싱하기

class RiotApiParsing:
    # 초기화 : 서버, Key / PlayerID, AccountID는 함수에서 받아옴.
    def __init__(self):
        self.__Server = "kr.api.riotgames.com"
        self.__ApiKey = "RGAPI-3144c3aa-6726-42c0-a894-7adee400c429"
        self.__PlayerID = ""
        self.__AccountID = ""
        self.__championData = []

    def getPlayerIDByName(self,PlayerName):

        conn = http.client.HTTPSConnection(self.__Server)

        conn.request("GET","/lol/summoner/v4/summoners/by-name/" + PlayerName +  "?api_key=" + self.__ApiKey)

        req = conn.getresponse()
        result = req.read().decode('utf-8')
        jsonTempData = json.loads(result)

        self.__PlayerID = jsonTempData['id']
        self.__AccountID = jsonTempData['accountId']

    def getPlayerMasteryByPlayerID(self):
                
        conn = http.client.HTTPSConnection(self.__Server)

        conn.request("GET","/lol/champion-mastery/v4/champion-masteries/by-summoner/" + self.__PlayerID +  "?api_key=" + self.__ApiKey)

        req = conn.getresponse()
        result = req.read().decode('utf-8')
        return json.loads(result)

    def getPlayerLeagueByPlayerID(self):
        conn = http.client.HTTPSConnection(self.__Server)

        conn.request("GET","/lol/league/v4/entries/by-summoner/" + self.__PlayerID +  "?api_key=" + self.__ApiKey)

        req = conn.getresponse()
        result = req.read().decode('utf-8')
        return json.loads(result)

    def getPlayingGameByPlayerID(self):
        conn = http.client.HTTPSConnection(self.__Server)

        conn.request("GET","/lol/spectator/v4/active-games/by-summoner/" + self.__PlayerID +  "?api_key=" + self.__ApiKey)

        req = conn.getresponse()
        result = req.read().decode('utf-8')
        return json.loads(result)

    def getMatchsByAccountID(self):
        #champion, queue, season, endIndex, beginIndex
        conn = http.client.HTTPSConnection(self.__Server)
        filterOptions = "?"
        conn.request("GET","/lol/match/v4/matchlists/by-account/" + self.__AccountID + filterOptions + "api_key=" + self.__ApiKey)

        req = conn.getresponse()
        result = req.read().decode('utf-8')
        return json.loads(result)

    def getAllChampionsData(self):

        conn = http.client.HTTPSConnection("ddragon.leagueoflegends.com")
        conn.request("GET","/cdn/9.10.1/data/ko_KR/champion.json")
        req = conn.getresponse()
        result = req.read().decode('utf-8')
        return json.loads(result)
        

        
        print("완료")
         
	#이미지 파일 얻어오는코드
    def getImgByChampionsName(self, championName):
        url = "http://ddragon.leagueoflegends.com/cdn/9.10.1/img/champion/" + championName + ".png"
        #http://ddragon.leagueoflegends.com/cdn/img/champion/splash/Azir_0.jpg

        outPath = "images/"
        outFile = "image_" + championName + ".png"

        if not os.path.isdir(outPath):
            os.makedirs(outPath)

        urllib.request.urlretrieve(url, outPath + outFile)
    
    

class championData:
    
    def __init__(self, data):
        #self.__championData = []
        temp = []
        for i in data['data'].items():
            #self.__championData.append(i)
           temp.append(i)
        self.__championData = tuple(temp)

        #for i in range(len(self.__championData)):
            #self.getImgByChampionsName(championData[i][0]) #img 호출 코드
            #print(self.__championData[i][0])

    def printChampionData(self):
        for i in self.__championData:
            print(i)
        self.__championData[0]

abc = RiotApiParsing()
abc.getPlayerIDByName("5GHaky")
a = championData(abc.getAllChampionsData())
