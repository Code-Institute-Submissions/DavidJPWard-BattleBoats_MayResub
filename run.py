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
    randomly populates the game board with ships. it creates a ship, checks a ship hasnt not 
    already been made at that location and then adds it to thats boards list of ships 
    """
    while True:
        newship = random.randint(0, board.size-1),random.randint(0, board.size-1)
        if newship not in board.ships:
            board.ships.append(newship)
            break






def play_game(player_board, computer_board):
    """
    called when the game has finished setting up, calls for guesses to be continously entered via a loop
    and breaks when either players score equals the number of ships. 
    """
    player_board.display_player_ships()

    player_score = 0
    computer_score = 0
    while player_score < shipNum and computer_score < shipNum:
        
        

        computer_board.print_board()
        player_board.print_board()

        if computer_board.guesses:
            print(f"Player Score: {player_score}, Computer Score : {computer_score}")
            computer_board.print_player_guesses()

        print("\n")

        x,y = make_guess(computer_board)
        if computer_board.guess_against(x, y, player_board) == True:
            player_score += 1
        
        if player_board.guess_against(random.randint(0,boardSize-1),random.randint(0,boardSize-1), computer_board) == True:
            computer_score += 1

    computer_board.print_board()
    player_board.print_board()

    print("\n")

    if player_score >= shipNum:
        print(f"{player_board.name} has won\n")
    elif computer_score >= shipNum:
        print(f"{computer_board.name} has won\n")
    else:
        print("game was a draw")
    input("please any key to continue/n")
    Menu()


def make_guess(board):
    """
    function that creates a tuple out of the inputs made by the player, checks they are valid and returns it
    """
    while True:
        while True:
            x_guess = input(f"please choose an x coordinate(a number between 0 and {boardSize -1}): ")
            if validate_int(x_guess, 1, 0, board.size -1) == True:
                break
            print("please pick again")

        while True:
            y_guess = input(f"please choose an y coordinate(a number between 0 and {boardSize-1}): ")
            if validate_int(y_guess, 1, 0, board.size -1) == True:
                break
            print("please pick again")

        if new_coordinates(x_guess, y_guess, board) == True:
            break

    return x_guess, y_guess    
        
    
    




def Menu():
    """
    Main menu of the game, here you can change settings and start a game.
    """
    global boardSize
    global shipNum

    print("           "+"-" * 35)
    print("               Welcome to BATTLE BOATS")
    print(f"           board size: {boardSize}, number of ships: {shipNum}")
    #print(f"           current score -- player: {player_score}   computer: {computer_score}")
    print("           " +"-" * 35)
    print(f"q: Start Game    w: Change Board Size    e: Change Ship Number \n")

    option = input("Please choose and option: ").lower()

    while True:
        if option in ("q", "w", "e"):
            break
        print("Invalid option, please press q, w or e\n")
        option = input("Please choose and option: ").lower()
    
    if(option == "q"):
        newGame()
    elif(option == "w"):
        boardSize = int(changeBoardSize())
        Menu()
    elif(option == "e"):
        shipNum = changeShipNum()
        Menu()


def changeBoardSize():
    """
    simply takes a value from input and assigns it to the BoardSize variable
    """
    print("please pick a number between 4 and 10 to change the game board")
    while True:
        new_size = input()
        if(validate_int(new_size, 2, 4, 10)):
            break
        print("Please pick another number between 4 and 10 ")
    return new_size


def changeShipNum():
    """        
    simply takes a value from input and assigns it to the BoardSize function
    """
    print("please pick a number between 1 and 9 to change ship number")
    while True:
        new_ship_num =  input()
        if(validate_int(new_ship_num, 1, 1, 9)):
            break
        print("Please pick another number between 1 and 9")
    return int(new_ship_num)


def validate_int(input, length, min_value, max_value):
    """
    validates interger values, checks if the input is an interger and
    that it doesnt exceed its target length, or value range
    """
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
        print(f"Invalid: {e}\n")
        return False
    return True

def new_coordinates(x, y, board):
    """
    checks if a set of co ordinates have already been guessed, returns true if they were new.
    """
    entry = [int(x),int(y)]
    if entry not in board.guesses:

        return True
    else:
        print(f"co-ordinates ({x}, {y}) have already been guessed, pick again")
        return False


def newGame():
    """
    called when a new game is started, creates 2 boards, one for each player, and populates them with ships.
    then calls the play game function.
    """

    player_name = input("What is your name?: ")
    print("\n")
    
    player_board = Player_Board(player_name, boardSize, shipNum, "player")
    computer_board = Computer_Board("computer", boardSize, shipNum, "computer")
    player_board.board.reverse()
    computer_board.board.reverse()

    for i in range(shipNum):
        populate_board(player_board)
        populate_board(computer_board)
    play_game(player_board, computer_board)



def Main():
    Menu()


Main()