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

        result = 0
        for i in d:
            if (i.getRoll() == num):
                result += num
        return result

    def scoreThreeOfAKind(d):
        result = 0
        dieList = [i.getRoll() for i in d]
        for i in range(1,7):
            if(dieList.count(i) == 3):
                for i in dieList:
                    result += i
                return result
        return 0

    def scoreFourOfAKind(d):
        result = 0
        dieList = [i.getRoll() for i in d]
        for i in range(1,7):
            if(dieList.count(i) == 4):
                for i in dieList:
                    result += i
                return result
        return 0

    def scoreFullHouse(d):
        three = False
        two = False

        dieList = [i.getRoll() for i in d]

        for i in range(1,7):
            if(dieList.count(i) == 3):
                three = True
            if(dieList.count(i) == 2):
                two = True

        if(three and two):
            return 25
        return 0

    def scoreSmallStraight(d):
        
        dieList = [i.getRoll() for i in d]
        
        check = [1 if i in dieList else 0 for i in [1,2,3,4]]
        check2 = [1 if i in dieList else 0 for i in [2,3,4,5]]
        check3 = [1 if i in dieList else 0 for i in [3,4,5,6]]
        if(check.count(0) == 0 or check2.count(0) == 0 or check3.count(0) == 0):
            return 30

        return 0

    def scoreLargeStraight(d):

        dieList = [i.getRoll() for i in d]
        
        check = [1 if i in dieList else 0 for i in [1,2,3,4,5]]
        check2 = [1 if i in dieList else 0 for i in [2,3,4,5,6]]
        if(check.count(0) == 0 or check2.count(0) == 0):
            return 40

        return 0

    def scoreYahtzee(d):
        dieList = [i.getRoll() for i in d]

        for i in range(1,7):
            if(dieList.count(i) == 5):
                return 50
        return 0

    def scoreChance(d):
        result = 0
        for i in d:
            result += i.getRoll()
        return result

    def sumDie(d):
        pass

