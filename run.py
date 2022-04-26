from multiprocessing.sharedctypes import Value
from pickle import TRUE
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
        boardSize = changeBoardSize()
        Menu()
    elif(option == "e"):
        changeShipNumber()
    else:
        print("Invalid option, please pick again")

def changeBoardSize():
    print("please pick a number between 4 and 10 to change the game board\n")
    while True:
        new_size = input()
        if(validate_int(new_size, 2, 4, 10)):
            break
        print("Please Pick Again: ")
    return new_size()



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
    return True


Menu()