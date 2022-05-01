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
        i = 0
        print(f"{self.name}'s board")
        for row in reversed(self.board):
            i = i + 1
            print(str(i) + " " + " ".join(row))


    """
    def print_board(self):
        j = int(0)
        print(f"{self.name}'s board")
        for row in reversed(self.board):
            j = 0
            for i in row:
                row[j] = j
                j = j + 1
        print(" ".join(str(row)))
    """

    def guess(self, x, y):
        x = int(x)
        y = int(y)
        self.guesses.append([x,y])
        self.board[y][x] = "X"

        print(f"{self.type} board, guesses: {self.guesses}")

        if (x,y) in self.ships:
            self.board[y][x] = "!"
            return True
        else:
            return False



