#격자를 생성하자

class Grid:

    def __init__(self):
        self.grid_size = 13
        self.grid_long = 6
        self.grid_tool = []
        self.game_count = 0
        self.text = ["빨간색", "노란색"]

        self.game_true = True

        self.push_count =[5] * self.grid_long

        self.answer = 0
        self.init()

    def init(self):

        #count 초기화
        for i in range(self.grid_long):
            self.push_count[i] = 5

        for i in range(self.grid_long):
            temp_tool = []
            for j in range(self.grid_size):
                if j & 1:
                    temp_tool.append(' ')
                else:
                    temp_tool.append('|')

            self.grid_tool.append(temp_tool)

    def draw(self):
        # 출력 부분은 나중에 만들자
        for i in self.grid_tool:
            print(i)

    def game_manager(self):
        while(self.game_true):
            #떨어트리는 디스크
            if self.game_count & 1:
                print(self.text[0])
            else:
                print(self.text[1])

            self.answer = eval(input("디스크를 0-6 열에 떨어트리세요: "))
            #1, 3, 5, 7, 9, 10
            if self.game_count & 1:
                self.grid_tool[self.push_count[self.answer]][self.answer + 1] = 'B'
            else:
                self.grid_tool[self.push_count[self.answer]][self.answer + 1] = 'Y'
            self.push_count[self.answer] -= 1

            self.draw()
            self.game_count+= 1

grid = Grid()

grid.game_manager()