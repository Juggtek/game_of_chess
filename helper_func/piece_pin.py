import sys
sys.path.append('/home/felix/game_of_chess')
from helper_func.attack_cell import attack_cell

def piece_pin(in_board, colour):
    board_attack = [[0 for i in range(8)] for j in range(8)]
    board = in_board
    # piece = board[from_col][from_row]
    # board[from_col][from_row].set_piece(None)
    # board[to_col][to_row] = piece
    # print to_col,to_row

    for row in range(8):
        for col in range(8):
            if board[col][row].__repr__() != "0":
                if board[col][row].__repr__()[1] != colour:
                    board[col][row].piece.cells_attacked(board_attack, col, row, "attack")

    for i in board_attack:
        print i

    for row in range(8):
        for col in range(8):
            print board[col][row].__repr__()
            print board_attack[col][row]
            if board[col][row].__repr__() == "K" + colour and \
               board_attack[col][row] != 0:
                return False
                break
            else:
                return True
