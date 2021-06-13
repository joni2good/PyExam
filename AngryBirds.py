class Bird:
    def __init__(self, pos=[0, 0], direction=2):
        self.pos = pos
        self.direction = direction

    def forward(self):
        if self.direction == 1:
            self.pos[0] -= 1
        elif self.direction == 2:
            self.pos[1] += 1
        elif self.direction == 3:
            self.pos[0] += 1
        elif self.direction == 4:
            self.pos[1] -= 1

    def changeDir(self, change):
        if change == 'l':
            self.direction -= 1
        elif change == 'r':
            self.direction += 1


class Pig:
    def __init__(self, pos=[0, 1]):
        self.pos = pos


class Board:
    def __init__(self, boardSize=10):
        self.size = boardSize

    def makeBoard(self, bird, pig):
        for i in range(self.size):
            for j in range(self.size):
                if [i, j] == bird.pos:
                    print(' B ', end='')
                elif [i, j] == pig.pos:
                    print(' P ', end='')
                else:
                    print(' * ', end='')
            print(i)
        for i in range(self.size):
            print(' ' + str(i) + ' ',end='')


class Workspace:
    def __init__(self):
        self.inp = 'start'

    def start(self, game):
        print()
        print('What steps do you want to perform?')
        print('Options: move forward (f), turn left (l), turn right (r)')
        print('Default direction is right')
        print('Type "q" when done')
        while self.inp != 'q':
            self.inp = input('Move: ')
            if self.inp != 'q':
                game.addMove(self.inp)


class Game:
    def __init__(self):
        self.moveList = []
        self.whereList = []
        self.bool = False

    def addMove(self, move):
        self.moveList.append(move)

    def run(self, bird, pig, boardSize):
        for i in self.moveList:
            if i == 'f':
                bird.forward()
                self.whereList.append(bird.pos)
            elif i == 'l' or i == 'r':
                bird.changeDir(i)
            else:
                pass
        for i in self.whereList:
            if i[0] not in range(0, boardSize) or i[1] not in range(0, boardSize):
                self.bool = True
        if self.bool or pig.pos not in self.whereList:
            print('The bird lost the game!')
            print('Birds position: ' + str(bird.pos))
            print('Pig position: ' + str(pig.pos))
        elif pig.pos in self.whereList:
            print('Uff the pig is dead')
            print('Birds position: ' + str(bird.pos))
            print('Pig position: ' + str(pig.pos))


bird1 = Bird()
pig1 = Pig([1, 3])
board = Board(10)
board.makeBoard(bird1, pig1)
game1 = Game()
work = Workspace()
work.start(game1)
print(game1.moveList)
game1.run(bird1, pig1, board.size)


