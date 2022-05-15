class Board():
    def __init__(self, name, size, num_of_ships, board_type):
        self.name = name
        self.size = size
        self.board = [["." for x in range(size)] for y in range(size)]
        self.num_of_ships = num_of_ships
        self.type = board_type
        self.subs = []
        self.frigates = []
        self.ships = []
        self.guesses = []

    def print_board(self):
        """
        function that prints the game board
        """
        print(f"{self.name}'s Board")
        for row in reversed(self.board):
            print(" "+" ".join(row))


    def guess_against(self, x, y, enemy):
        """
        function that is called when making a guess against this board, notifies if it was a 
        hit or a miss and returns true or false respectively
        """
        x = int(x)
        y = int(y)
        self.guesses.append([x,y])
        self.board[y][x] = "X"

        if (x,y) in self.subs:
            self.board[y][x] = "!"
            print(f"{enemy.name} has hit!")
            return True
        else:
            print(f"{enemy.name} has missed.\n")
            return False
