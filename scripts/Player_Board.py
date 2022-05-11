from scripts.Board import Board


class Player_Board(Board):
        def display_player_ships(self):
            for i in self.ships:
                print(i)
                a, b = i
                self.board[b][a] = "@"
        
        def make_guess(board, validate_int):
            while True:
                while True:
                    x_guess = input("please choose an x coordinate: ")
                    if validate_int(x_guess, 1, 0, board.size -1) == True:
                        break
                    print("please pick again")

                while True:
                    y_guess = input("please choose an x coordinate: ")
                    if validate_int(y_guess, 1, 0, board.size -1) == True:
                        break
                    print("please pick again")

                if valid_coordinates(x_guess, y_guess, board) == True:
                    break

            return x_guess, y_guess
