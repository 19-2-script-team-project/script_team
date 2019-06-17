class Player:
    UPPER = 6
    LOWER = 7

    def __init__(self,name):
        self.name = name
        self.scores = [ 0 for i in range(self.UPPER + self.LOWER)]
        self.used = [False for i in range(self.UPPER + self.LOWER)]

    def setScore(self, score, index):
        self.scores[index] = score

    def setAtUsed(self, index):
        self.used[index] = True

    def getUpperScore(self):
        upperTotal = 0
        for i in range(self.UPPER):
            upperTotal += self.scores[i]
        return upperTotal

    def getLowerScore(self):
        lowerTotal = 0
        for i in range(self.UPPER, self.UPPER + self.LOWER):
            lowerTotal += self.scores[i]
        return lowerTotal

    def getUsed(self):
        pass

    def getTotalScore(self):
        total = 0
        for i in scores:
            total += i
        return total

    def toString(self):
        return self.name

    def allUpperUsed(self):
        for i in range(self.UPPER):
            if (self.used[i] == False):
                return False
        return True

    def allLowerUsed(self):
        for i in range(self.UPPER, self.UPPER + self.LOWER):
            if (self.used[i] == False):
                return False;
        return True;
