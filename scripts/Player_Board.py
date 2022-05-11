from scripts.Board import Board


class Player_Board(Board):

        def display_player_ships(self):
            """
            cycles through the players ships and marks their location on the players board
            """
            for i in self.ships:
                a, b = i
                self.board[b][a] = "@"


        
