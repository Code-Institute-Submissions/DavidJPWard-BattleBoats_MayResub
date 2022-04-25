from multiprocessing.sharedctypes import Value
from tkinter import N

boardSize = 5
shipNum = 4


def Menu():
    print("           "+"-" * 35)
    print("               Welcome to BATTLE BOATS")
    print(f"           board size: {boardSize}, number of ships: {shipNum}")
    print("           " +"-" * 35)
    print(f"q: start game    w: change Board size    e: Change Ship Number \n")

    option = input("Please choose and option: ").lower()

    if(option == "q"):
        print("q")
    elif(option == "w"):
        changeBoardSize()
    elif(option == "e"):
        changeShipNumber()
    else:
        print("Invalid option, please pick again")

def changeBoardSize():
    print("please pick a number between 4 and 10 to change the game board")

def validate_int(input, length, min_value, max_value):
    try:
        int(input)
        if(len(input)>length):
            raise ValueError(f"input has exceeded the maximum length of {length} chracters")
        if(input < min_value):
            raise ValueError(f"input cannot be less than {min_value}")
        if(input > max_value):
            raise ValueError(f"input cannot be more than {max_value}")
    except ValueError as e:
        print(f"invalid input, please input an integer")
        return False;
    return True


Menu()