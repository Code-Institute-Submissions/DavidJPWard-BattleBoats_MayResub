from multiprocessing.sharedctypes import Value
from pickle import TRUE
from tkinter import N

boardSize = 5
shipNum = 4

class board():
    def __init__(self, name, size, numOfShips, type):
        self.name = name
        self.size = size
        self.board = [["." for x in range(size)] for y in range(size)]
        self.numOfShips = numOfShips
        self.type = type
        self.ships = []
        self.guesses = []

    def print_board(self):
        for row in self.board:
            print(" ".join(row))


def populate_board(board):
    
def make_guess():

def valid_coordinates(x, y, board)

def play_game(computer_board, player_board)


def Menu():
    global boardSize
    global shipNum

    print("           "+"-" * 35)
    print("               Welcome to BATTLE BOATS")
    print(f"           board size: {boardSize}, number of ships: {shipNum}")
    print(f"           current score -- player: {player_score}   computer: {computer_score}")
    print("           " +"-" * 35)
    print(f"q: start game    w: change Board size    e: Change Ship Number \n")

    option = input("Please choose and option: ").lower()

    if(option == "q"):
        newGame()
    elif(option == "w"):
        boardSize = int(changeBoardSize())
        Menu()
    elif(option == "e"):
        shipNum = changeShipNum()
        Menu()
    else:
        print("Invalid option, please pick again")


def changeBoardSize():
    print("please pick a number between 4 and 10 to change the game board")
    while True:
        new_size = input()
        if(validate_int(new_size, 2, 4, 10)):
            break
        print("Please Pick Again: ")
    return new_size


def changeShipNum():
    print("please pick a number between 1 and 9 to change ship number")
    while True:
        new_ship_num =  input()
        if(validate_int(new_ship_num, 1, 1, 9)):
            break
        print("please pick again")
    return new_ship_num


def validate_int(input, length, min_value, max_value):
    try:
        if(str(input).isdigit() != True):
            raise ValueError(f"input must be an integer")
        input = int(input)
        if(len(str(input)) > length):
            raise ValueError(f"input has exceeded the maximum length of {length} chracters")
        if(input < min_value):
            raise ValueError(f"input cannot be less than {min_value}")
        if(input > max_value):
            raise ValueError(f"input cannot be more than {max_value}")
    except ValueError as e:
        print(f"invalid input, {e}\n")
        return False
    print("passed validation")
    return True


def newGame():
    player_name = input("What is your name")
    
    player_Board = board(player_name, boardSize, shipNum, "player")
    computer_board = board("computer", boardSize, shipNum, "computer")



def Main():
    Menu()


Main()