from scripts.Board import Board

"""
this is the "Player_Board" class
"""

class Player_Board(Board):

        def display_player_ships(self):
            """
            cycles through the players ships and marks their location on the players board
            """
            #print(f" subs: {self.subs} --- ships: {self.ships}")

            for i in self.subs:
                a, b = i
                self.board[b][a] = "@"
            
            #print(f" frigates: {self.frigates} --- ships: {self.ships}")
            for i in self.frigates:
                a, b = i
                self.board[b][a] = "#"


        
