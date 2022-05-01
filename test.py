from audioop import reverse


size = 5
board = [["." for x in range(size)] for y in range(size)]
name = "lol"

def create_board():
    print(board)
    k = 0
    for i in range(size):
        for j in range(size):
            board[i][j] = str(k)
            k = k + 1
    print(board)


def reverse_board(_board):
    reversed_board = _board.reverse()
    return reversed_board

    
def print_board():
        i = 0
        k = 0
        print(f"{name}'s board")
        for row in board:
            """
            j = 0
            for l in row:
                l = i
                row[j]= str(l)
                j += 1
                i += 1
            k = k + 1
            """
            print(str(k) + ": " + " ".join(row))



create_board()
board.reverse()
print(board)
print_board()