from Dice import *

class Configuration:

    configs = ["Category","Ones", "Twos","Threes","Fours","Fives","Sixes",
    "Upper Scores","Upper Bonus(35)","Three of a kind", "Four of a kind", "Full House(25)",
    "Small Straight(30)", "Large Straight(40)", "Yahtzee(50)","Chance","Lower Scores", "Total"]

    def getConfigs():
        return Configuration.configs
    def score(row, d):
        if(row>=0 and row<=5):
            return Configuration.scoreUpper(d,row+1)
        elif (row == 8):
            return Configuration.scoreThreeOfAKind(d)
        elif (row == 9):
            return Configuration.scoreFourOfAKind(d)
        elif (row == 10):
            return Configuration.scoreFullHouse(d)
        elif (row == 11):
            return Configuration.scoreSmallStraight(d)
        elif (row == 12):
            return Configuration.scoreLargeStraight(d)
        elif (row == 13):
            return Configuration.scoreYahtzee(d)
        elif (row == 14):
            return Configuration.scoreChance(d)
        elif (row == 6 or row == 7 or row == 15 or row == 16):
            return -1

    def scoreUpper(d, num):
        if(num == 1):
            pass
        elif#one , two, three .... 점수 반환.
        pass
    def scoreThreeOfAKind(d):
        pass
    def scoreFourOfAKind(d):
        pass
    def scoreFullHouse(d):
        pass
    def scoreSmallStraight(d):
        pass
    def scoreLargeStraight(d):
        pass
    def scoreYahtzee(d):
        pass
    def scoreChance(d):
        pass
    def sumDie(d):
        pass

