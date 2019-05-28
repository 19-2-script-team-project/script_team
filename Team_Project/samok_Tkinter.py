from tkinter import *

turn = 1
Table
L1
def judgement(row, column, color, cnt = 0, dir = 0 ):
    print(cnt)
    if cnt == 4:
        return color
    if dir == 0:
        cnt += 1
        if judgement(row, column, color, cnt, dir = 1) != 0 or judgement(row, column, color, cnt, dir = 2) != 0 or judgement(row, column, color, cnt, dir = 3) != 0 or judgement(row, column, color, cnt, dir = 4) != 0 or judgement(row, column, color, cnt, dir = 5) != 0: 
            print("color : ", color)
            return color
        return 0
        #Left #Left Down #Down #Right Down #Right
    elif dir == 1:
        if column - 1 != 0:
            if Table[row][column - 1].state == color:
                cnt += 1
                return judgement(row, column - 1, color, cnt, dir = 1)
        return 0

    elif dir == 2:
        if column - 1 != 0 and row + 1 != 6:
            if Table[row + 1][column - 1].state == color:
                cnt += 1
                return judgement(row + 1, column - 1, color, cnt, dir = 2)
        return 0

    elif dir == 3:
        if row + 1 != 6:
            if Table[row + 1][column].state == color:
                cnt += 1
                return judgement(row + 1, column, color, cnt, dir = 3)
        return 0

    elif dir == 4:
        if column + 1 != 7 and row - 1 != 6:
            if Table[row - 1][column + 1].state == color:
                cnt += 1
                return judgement(row - 1, column + 1, color, cnt, dir = 4)
        return 0
        
    elif dir == 5:
       if column + 1 != 7:
            if Table[row][column + 1].state == color:
                cnt += 1
                return judgement(row, column + 1, color, cnt, dir = 5)
       return 0


class Cell(Canvas) : 
    def __init__(self, container, row, column):
        self.state = 0 #available
        self.row = row
        self.column = column

        Canvas.__init__(self, container, width = 50, height = 50, bg = 'white')
        self.create_oval(10,10,40,40,fill = "white", tag = "empty")
        self.bind("<Button-1>", self.click)

    def push(self):
        global turn
        if(turn == 1):
            self.state = 1
            self.delete("empty")
            self.create_oval(10,10,40,40,fill = "red")
            turn = 2
        elif(turn == 2):
            self.state = 2
            self.delete("empty")
            self.create_oval(10,10,40,40,fill = "yellow")
            turn = 1

    def click(self, event):
        global Table
        print(self.row, " ",self.column)
        if(self.state == 0):
            if(self.row == 5):
                self.push()
                self.Win(judgement(self.row, self.column, self.state))
            elif (Table[self.row + 1][self.column].state != 0 ):
                self.push()
                self.Win(judgement(self.row, self.column, self.state))

    def Win(self, judge):
        print("Judge : ", judge)
        global L1
        global turn
        if(judge != 0):
            L1.configure(text = "{0} 승리! 게임이 끝났습니다.".format(judge))
            turn = -1


class Samok:
    def __init__(self):
        window = Tk()
        frame1 = Frame(window)
        frame1.pack()

        global Table
        Table = [[Cell(frame1, i, j) for j in range(7)] for i in range(6)]
        for i in range(6):
            for j in range(7):
                Table[i][j].grid(row = i, column = j)
        
        
        frame2 = Frame(window)
        frame2.pack()

        global L1
        L1 = Label(frame2, text = "게임중...")
        L1.pack()

        
        window.mainloop()
Samok()