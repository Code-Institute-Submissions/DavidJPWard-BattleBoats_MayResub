from scripts.Board import Board


class Player_Board(Board):
        def display_player_ships(self):
            for i in self.ships:
                print(i)
                a, b = i
                self.board[b][a] = "@"