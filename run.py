from multiprocessing.sharedctypes import Value
from pickle import TRUE
from re import X
from tkinter import N, Y
import random

from scripts.Player_Board import Player_Board
from scripts.Computer_Board import Computer_Board

boardSize = 5
shipNum = 4



def populate_board(board):
    """
    while True:
        newship = random.randint(0, board.size-1),random.randint(0, board.size-1)
        if newship not in board.ships:
            board.ships.append(newship)
            break"""
    board.ships.append((3,0))
    board.ships.append((2,4))
    board.ships.append((0,1))
    board.ships.append((4,1))
    





def play_game(player_board, computer_board):
    player_board.display_player_ships()
    computer_board.display_computer_ships()
    print("---")
    for i in computer_board.ships:
        print(i)
    player_score = 0
    computer_score = 0
    while player_score < shipNum and computer_score < shipNum:
        
        computer_board.print_board()
        player_board.print_board()
        x,y = make_guess(computer_board)
        if computer_board.guess(x,y) == True:
            player_score += 1
        player_board.guess(random.randint(0,boardSize-1),random.randint(0,boardSize-1))
        print(f"player score: {player_score}, ship number : {shipNum}")

        
    
    



def Menu():
    global boardSize
    global shipNum

    print("           "+"-" * 35)
    print("               Welcome to BATTLE BOATS")
    print(f"           board size: {boardSize}, number of ships: {shipNum}")
    #print(f"           current score -- player: {player_score}   computer: {computer_score}")
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

def valid_coordinates(x, y, board):
    if (x,y) not in board.guesses:
        return True
    else:
        print(f"co-ordinates ({x}, {y}) have already been guessed, pick again")
        return False


def newGame():
    player_name = input("What is your name?: ")
    
    player_board = Player_Board(player_name, boardSize, shipNum, "player")
    computer_board = Computer_Board("computer", boardSize, shipNum, "computer")
    player_board.board.reverse()
    computer_board.board.reverse()

    for i in range(shipNum):
        populate_board(player_board)
        populate_board(computer_board)

    play_game(player_board, computer_board)

def make_guess(board):
    while True:
        x_guess = input("please choose an x coordinate: ")
        validate_int(x_guess, 1 if boardSize < 10 else 2, 0, boardSize -1)
        
        y_guess = input("please choose a y coordinate: ")
        validate_int(y_guess, 1 if boardSize < 10 else 2, 0, boardSize -1)

        if valid_coordinates(x_guess, y_guess, board) == True:
            break
    return x_guess, y_guess


def Main():
    Menu()


Main()