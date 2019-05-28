from tkinter import *

turn = 1
Table
L1
winstone
direction
endcount = 0
def judgement(row, column, color, cnt = 0, dir = 0 ):
    if cnt == 4:
        global direction
        direction = dir
        return color
    if dir == 0:
        cnt += 1
        if judgement(row, column, color, cnt, dir = 1) != 0 or judgement(row, column, color, cnt, dir = 2) != 0 or judgement(row, column, color, cnt, dir = 3) != 0 or judgement(row, column, color, cnt, dir = 4) != 0 or judgement(row, column, color, cnt, dir = 5) != 0: 
            global winstone
            winstone = (row, column)
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
        self.create_oval(10,10,40,40,fill = "white", tag = "grim")
        self.bind("<Button-1>", self.click)

    def push(self):
        global turn
        global endcount
        endcount += 1
        if(turn == 1):
            self.state = 1
            self.delete("grim")
            self.create_oval(10,10,40,40,fill = "red", tag = "grim")
            turn = 2
        elif(turn == 2):
            self.state = 2
            self.delete("grim")
            self.create_oval(10,10,40,40,fill = "yellow", tag = "grim")
            turn = 1
        if(endcount == 41):
            L1.configure(text = ")
            turn = -1

    def click(self, event):
        global Table
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
            self.blink()

    def blink(self):
        global winstone
        global Table
        row, column = winstone
        print(direction)
        print("WWW")
        while True:
            self.after(200)
            self.update()
            if direction == 1:
                Table[row][column].delete("grim")
                Table[row][column - 1].delete("grim")
                Table[row][column - 2].delete("grim")
                Table[row][column - 3].delete("grim")

                Table[row][column].create_oval(10,10,40,40,fill = "red", tag = "grim")
                Table[row][column - 1].create_oval(10,10,40,40,fill = "red", tag = "grim")
                Table[row][column - 2].create_oval(10,10,40,40,fill = "red", tag = "grim")
                Table[row][column - 3].create_oval(10,10,40,40,fill = "red", tag = "grim")
            elif direction == 2:
                Table[row][column].delete("grim")
                Table[row+1][column - 1].delete("grim")
                Table[row+2][column - 2].delete("grim")
                Table[row+3][column - 3].delete("grim")

                Table[row][column].create_oval(10,10,40,40,fill = "red", tag = "grim")
                Table[row+1][column - 1].create_oval(10,10,40,40,fill = "red", tag = "grim")
                Table[row+2][column - 2].create_oval(10,10,40,40,fill = "red", tag = "grim")
                Table[row+3][column - 3].create_oval(10,10,40,40,fill = "red", tag = "grim")
            elif direction == 3:
                Table[row][column].delete("grim")
                Table[row+1][column].delete("grim")
                Table[row+2][column].delete("grim")
                Table[row+3][column].delete("grim")

                Table[row][column].create_oval(10,10,40,40,fill = "red", tag = "grim")
                Table[row+1][column].create_oval(10,10,40,40,fill = "red", tag = "grim")
                Table[row+2][column].create_oval(10,10,40,40,fill = "red", tag = "grim")
                Table[row+3][column].create_oval(10,10,40,40,fill = "red", tag = "grim")
            elif direction == 4:
                Table[row][column].delete("grim")
                Table[row+1][column+1].delete("grim")
                Table[row+2][column+2].delete("grim")
                Table[row+3][column+3].delete("grim")

                Table[row][column].create_oval(10,10,40,40,fill = "red", tag = "grim")
                Table[row+1][column+1].create_oval(10,10,40,40,fill = "red", tag = "grim")
                Table[row+2][column+2].create_oval(10,10,40,40,fill = "red", tag = "grim")
                Table[row+3][column+3].create_oval(10,10,40,40,fill = "red", tag = "grim")
            elif direction == 5:
                Table[row][column].delete("grim")
                Table[row][column+1].delete("grim")
                Table[row][column+2].delete("grim")
                Table[row][column+3].delete("grim")

                Table[row][column].create_oval(10,10,40,40,fill = "red", tag = "grim")
                Table[row][column+1].create_oval(10,10,40,40,fill = "red", tag = "grim")
                Table[row][column+2].create_oval(10,10,40,40,fill = "red", tag = "grim")
                Table[row][column+3].create_oval(10,10,40,40,fill = "red", tag = "grim")

            self.after(200)
            self.update()
            if direction == 1:
                Table[row][column].delete("grim")
                Table[row][column - 1].delete("grim")
                Table[row][column - 2].delete("grim")
                Table[row][column - 3].delete("grim")
                Table[row][column].create_oval(10,10,40,40,fill = "yellow", tag = "grim")
                Table[row][column - 1].create_oval(10,10,40,40,fill = "yellow", tag = "grim")
                Table[row][column - 2].create_oval(10,10,40,40,fill = "yellow", tag = "grim")
                Table[row][column - 3].create_oval(10,10,40,40,fill = "yellow", tag = "grim")
            elif direction == 2:
                Table[row][column].delete("grim")
                Table[row+1][column - 1].delete("grim")
                Table[row+2][column - 2].delete("grim")
                Table[row+3][column - 3].delete("grim")
                Table[row][column].create_oval(10,10,40,40,fill = "yellow", tag = "grim")
                Table[row+1][column - 1].create_oval(10,10,40,40,fill = "yellow", tag = "grim")
                Table[row+2][column - 2].create_oval(10,10,40,40,fill = "yellow", tag = "grim")
                Table[row+3][column - 3].create_oval(10,10,40,40,fill = "yellow", tag = "grim")
            elif direction == 3:
                Table[row][column].delete("grim")
                Table[row+1][column].delete("grim")
                Table[row+2][column].delete("grim")
                Table[row+3][column].delete("grim")
                Table[row][column].create_oval(10,10,40,40,fill = "yellow", tag = "grim")
                Table[row+1][column].create_oval(10,10,40,40,fill = "yellow", tag = "grim")
                Table[row+2][column].create_oval(10,10,40,40,fill = "yellow", tag = "grim")
                Table[row+3][column].create_oval(10,10,40,40,fill = "yellow", tag = "grim")
            elif direction == 4:
                Table[row][column].delete("grim")
                Table[row+1][column+1].delete("grim")
                Table[row+2][column+2].delete("grim")
                Table[row+3][column+3].delete("grim")
                Table[row][column].create_oval(10,10,40,40,fill = "yellow", tag = "grim")
                Table[row+1][column+1].create_oval(10,10,40,40,fill = "yellow", tag = "grim")
                Table[row+2][column+2].create_oval(10,10,40,40,fill = "yellow", tag = "grim")
                Table[row+3][column+3].create_oval(10,10,40,40,fill = "yellow", tag = "grim")
            elif direction == 5:
                Table[row][column].delete("grim")
                Table[row][column+1].delete("grim")
                Table[row][column+2].delete("grim")
                Table[row][column+3].delete("grim")
                Table[row][column].create_oval(10,10,40,40,fill = "yellow", tag = "grim")
                Table[row][column+1].create_oval(10,10,40,40,fill = "yellow", tag = "grim")
                Table[row][column+2].create_oval(10,10,40,40,fill = "yellow", tag = "grim")
                Table[row][column+3].create_oval(10,10,40,40,fill = "yellow", tag = "grim")

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