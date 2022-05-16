from scripts.Board import Board

"""
this is the "Computer_Board" class.
"""


class Computer_Board(Board):

        def print_player_guesses(self):
            """
            function thats prints outs the previous guesses made against the computers board.
            this infomation is only useful to the player has the computer has a data list 
            of guesses already made.
            """
            print(f"previous guesses: {self.guesses}")