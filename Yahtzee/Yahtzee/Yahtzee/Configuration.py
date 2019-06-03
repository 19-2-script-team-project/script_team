from Dice import *

class Configuration:

    configs = ["Category","Ones", "Twos","Threes","Fours","Fives","Sixes",
    "Upper Scores","Upper Bonus(35)","Three of a kind", "Four of a kind", "Full House(25)",
    "Small Straight(30)", "Large Straight(40)", "Yahtzee(50)","Chance","Lower Scores", "Total"]
    def getConfigs():
        return Configuration.configs
    def score(row, d):
        #row에 따라 주사위 점수를 계산 반환.
        #구현 위치
        pass
    def scoreUpper(d, num):
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
    def sumDie(d):
        pass

