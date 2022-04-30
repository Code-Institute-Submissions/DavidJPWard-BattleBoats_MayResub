class Board():
    def __init__(self, name, size, numOfShips, type):
        self.name = name
        self.size = size
        self.board = [["." for x in range(size)] for y in range(size)]
        self.numOfShips = numOfShips
        self.type = type
        self.ships = []
        self.guesses = []

    def print_board(self):
        print(f"{self.name}'s board")
        for row in reversed(self.board):
            print(" ".join(row))

    def guess(self, x, y):
        x = int(x)
        y = int(y)
        self.guesses.append([x,y])
        self.board[x][y] = "X"

        print(f"{self.type} board, guesses: {self.guesses}")

        if (x,y) in self.ships:
            self.board[x][y] = "!"
            return True
        else:
            return False



