class Player:
    UPPER = 6
    LOWER = 7

    def __init__(self,name):
        self.name = name
        self.scores = [ 0 for i in range(self.UPPER + self.LOWER)]
        self.used = [False for i in range(self.UPPER + self.LOWER)]

    def setScore(self, score, index):
        pass
    def getUpperScore(self):
        pass
    def getLowerScore(self):
        pass
    def getUsed(self):
        pass
    def getTotalScore(self):
        pass
    def toString(self):
        return self.name
    def allUpperUsed(self):

        for i in ramge(self.UPPER):
            if (self.used[i] == False):
                return False
        return True
