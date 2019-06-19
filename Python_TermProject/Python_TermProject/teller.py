#!/usr/bin/python
# coding=utf-8

import sys
import time
import sqlite3
import telepot
from API_Parsing import *

from tkinter import *
from pprint import pprint
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
from datetime import date, datetime, timedelta
import traceback

import noti

parseEngine = RiotApiParsing()
ChampionIDDict = {}
def replyMatchesData(user, name):
    
    print(user, name)
    ID = parseEngine.getPlayerIDByName(name)#[0] id, [1] accId
    Data = parseEngine.getMatchsByAccountID(ID[1],None,None, beginIndex= 0, endIndex = 3).get('matches')
    for i in Data:
        championID = i.get('champion')
        gameId = i.get('gameId')
        tempData = parseEngine.getMatchByGameID(gameId)
        participant = tempData.get("participantIdentities")
        participantId = 0
        for j in participant:
            p = j.get("player")
            if(p.get("accountId") == ID[1]):
                participantId = j.get("participantId")
                break;
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

        msg = ''
        if(win):
            msg += 'WIN\n'      
        else:
            msg += 'LOSE\n'      
        msg += 'champion : '        + ChampionIDDict[championID]    + '\n'
        msg += 'kills : '           + str(kills)                       + '\n'
        msg += 'assists : '         + str(assists)                       + '\n'
        msg += 'deaths : '          + str(deaths)                        + '\n'
        noti.sendMessage( user, msg )

def replyRankData(user, name):
    
    print(user, name)
    ID = parseEngine.getPlayerIDByName(name)#[0] id, [1] accId
    Data = parseEngine.getPlayerLeagueByPlayerID(ID[0])
    for i in Data:
        msg = ''
        msg += 'queueType : '      + i.get('queueType')    + '\n'
        msg +=  'tier : '          + i.get('tier')         + '\n'
        msg += 'rank : '           + i.get('rank')         + '\n'
        msg += 'leaguePoints : '   + str(i.get('leaguePoints')) + '\n'
        msg +=  'wins : '          + str(i.get('wins'))         + '\n'
        msg += 'losses : '         + str(i.get('losses'))
        noti.sendMessage( user, msg )
  
def replyMasteryData(user, name):
    
    print(user, name)
    ID = parseEngine.getPlayerIDByName(name)#[0] id, [1] accId
    Data = parseEngine.getChampionMasteryByPlayerID(ID[0])
    for i in range(3):
        msg = ''
        msg += 'Top' + str(i+1) + '\n'
        msg += 'champion : '         + ChampionIDDict[Data[i].get('championId')]   + '\n'
        msg += 'championLevel : '    + str(Data[i].get('championLevel'))                + '\n'
        msg += 'championPoints : '   + str(Data[i].get('championPoints'))
        noti.sendMessage( user, msg )
   

def check( user ):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS users( user TEXT, location TEXT, PRIMARY KEY(user, location) )')
    cursor.execute('SELECT * from users WHERE user="%s"' % user)
    for data in cursor.fetchall():
        row = 'id:' + str(data[0]) + ', location:' + data[1]
        noti.sendMessage( user, row )


def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    if content_type != 'text':
        noti.sendMessage(chat_id, '난 텍스트 이외의 메시지는 처리하지 못해요.')
        return

    text = msg['text']
    args = text.split(' ')
    if text.startswith('전적') and len(args)>1:
        print('try to 전적', args[1])
        replyMatchesData( chat_id, args[1] )
    elif text.startswith('랭크') and len(args)>1:
        print('try to 랭크', args[1])
        replyRankData( chat_id, args[1] )
    elif text.startswith('모스트')  and len(args)>1:
        print('try to 모스트', args[1])
        replyMasteryData( chat_id, args[1] )
    elif text.startswith('확인'):
        print('try to 확인')
        check( chat_id )
    else:
        noti.sendMessage(chat_id, """모르는 명령어입니다.\n전적 '유저이름'\n랭크 '유저이름'\n모스트 '유저이름'""")

def start():
    temp = (parseEngine.getAllChampionsData()).items()
    for i in temp:
        ChampionIDDict[int(i[1]['key'])] = i[0]

    window = Tk()
    window.title("League Of Legends Search")
    window.geometry("250x400")
    window.resizable(False, False)

    today = date.today()
    current_month = today.strftime('%Y%m')
    TEXT = ''
    TEXT += '[' + str(today) + ']received token :\n' +  noti.TOKEN + '\n'
    
    state = Label(window, text = TEXT)
    state.pack()

    bot = telepot.Bot(noti.TOKEN)

    printMessage(state, TEXT, str(bot.getMe()))

    bot.message_loop(handle)

    printMessage(state, TEXT, 'Listening...')
    
    window.mainloop()
    
    while 1:
      time.sleep(10)

def printMessage(label, Str, Message):
    Str += Message + '\n'
    label.configure(text = Str)