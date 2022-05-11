from scripts.Board import Board


class Computer_Board(Board):

        def print_player_guesses(self):
            """
            function thats prints outs the previous guesses made against the computers board
            """
            print(f"previous guesses: {self.guesses}")