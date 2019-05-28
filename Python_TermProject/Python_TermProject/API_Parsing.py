        
        #5GHaky xhpMDatlPQddXaIoAqs3tqgHNuJY0Q2IwG_3ztonj0WSyeo
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
    def __init__(self):
        self.__Server = "kr.api.riotgames.com"
        self.__ApiKey = "RGAPI-60be92e4-4d94-4073-a51e-5c4aaa0cd82d"
        self.__PlayerID = ""
        self.__AccountID = ""
    def getPlayerIDByName(self,PlayerName):

        if (PlayerName == ""):
            print("비어있는입력")
            return
        #PlayerName = "5GHaky"
        #ApiKey = "RGAPI-a6ad83f9-60dd-468e-b68d-b3dc9b24446e"
        #server = "kr.api.riotgames.com"  # 물음표까지 다써도됌
        #파싱 ..
        #UserName = urllib.parse.quote(UserName)

        conn = http.client.HTTPSConnection(self.__Server)

        conn.request("GET","/lol/summoner/v4/summoners/by-name/" + PlayerName +  "?api_key=" + self.__ApiKey)

        req = conn.getresponse()
        result = req.read().decode('utf-8')
        jsonTempData = json.loads(result)
        if len(jsonData.jsonData["rows"]) == 0:
            return null;

        self.__PlayerID = jsonTempData['id']
        self.__AccountID = jsonTempData['accountId']

    def getPlayerMasteryByPlayerID(self):
        if (PlayerID == ""):
            print("비어있는입력")
            return
                
        conn = http.client.HTTPSConnection(self.__Server)

        conn.request("GET","/lol/champion-mastery/v4/champion-masteries/by-summoner/" + self.__PlayerID +  "?api_key=" + self.__ApiKey)

        req = conn.getresponse()
        result = req.read().decode('utf-8')
        return json.loads(result)

    def getMatchsByPlayerID(self):
        if (PlayerID == ""):
            print("비어있는입력")
            return
                
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

    #http://ddragon.leagueoflegends.com/cdn/9.10.1/data/ko_KR/champion.json
  
	#이미지 파일 얻어오는코드
    def getImgByChampionsName(self):
        
        url = "http://ddragon.leagueoflegends.com/cdn/9.10.1/img/champion/" + "Azir" + ".png"
        #http://ddragon.leagueoflegends.com/cdn/img/champion/splash/Azir_0.jpg

        outpath = "images/"
        outfile = "image_" + "Azir" + ".png"

        if not os.path.isdir(outpath):
            os.makedirs(outpath)

        urllib.request.urlretrieve(url, outpath + outfile)
	#여기까지

        print(jsonData)
        webbrowser.open_new(url)

        pass




class ParsingDataOfItems:
    def __init__(self,JSON):
        self.jsonData = json.loads(JSON) #string 형태의 JSON 객체를 딕셔너리로 바꾼다


        if len(self.jsonData["rows"]) == 0:
            return

        self.itemID = self.jsonData["rows"][0]["itemId"]
        self.itemName = self.jsonData["rows"][0]["itemName"]
        self.itemRarity = self.jsonData["rows"][0]["itemRarity"]
        self.itemType = self.jsonData["rows"][0]["itemType"]
        self.itemDetail = str(self.jsonData["rows"][0]["itemTypeDetail"])
        self.itemAvailableLevel = str(self.jsonData["rows"][0]["itemAvailableLevel"])

    def __str__(self):
        if len(self.jsonData["rows"]) == 0:
            return ""
        return " [아이템 고유코드 : " + self.itemID + "]\n [아이템이름 : " + self.itemName + "]\n [아이템 레어도 : " + self.itemRarity + "]\n [아이템 타입 : " + self.itemType + "]\n [아이템 타입상세 : " + self.itemDetail + "]\n [아이템 착용레벨 : " + self.itemAvailableLevel + "]\n"


RiotApiParsing().GetItemInfoFromMarket("흑천의 주인 - 대검")

