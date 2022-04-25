from tkinter import N

boardSize = 5
shipNum = 4


def Menu():
    print("           "+"-" * 35)
    print("               Welcome to BATTLE BOATS")
    print(f"           board size: {boardSize}, number of ships: {shipNum}")
    print("           " +"-" * 35)
    print(f"q: start game    w: change Board size    e: Change Ship Number \n")

    option = input("Please choose and option").lower()

    print(option)

Menu()