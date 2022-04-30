from scripts.Board import Board


class Computer_Board(Board):
        def display_computer_ships(self):
            for i in self.ships:
                print(i)
                a, b = i
                self.board[b][a] = "0"