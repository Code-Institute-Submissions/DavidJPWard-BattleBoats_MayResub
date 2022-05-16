"""
this is the "Board" abstract class which holds all the methods and variables
for the board.two classes inherit from here, player board and enemy board,
which hold methods only used by those classes.
"""


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

        print(f"\n{self.name}'s Board")
        for row in reversed(self.board):
            print(" "+" ".join(row))

    def guess_against(self, x, y, enemy):
        """
        function that is called when making a guess against this board, it
        prints the guess, identifies if it was a hit or a miss and returns
        true or false respectively
        """
        x, y = int(x), int(y)
        self.guesses.append([x, y])
        self.board[y][x] = "X"
        print(f"{enemy.name} has guessed [{x}, {y}]")

        if (x, y) in self.ships:
            self.board[y][x] = "!"
            print(f"{enemy.name} has hit!")
            return True
        else:
            print(f"{enemy.name} has missed.")
            return False
