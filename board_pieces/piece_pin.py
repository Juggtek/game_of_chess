import sys
sys.path.append('/home/felix/game_of_chess')
from helper_func.attack_cell import attack_cell

def piece_pin(board, colour):
    board_attack = [[0 for i in range(8)] for j in range(8)]
    for col in range(8):
        for row in range(8):
            if board[col][row].__repr__() != "0" and board[col][row].__repr__()[1] != colour:
                board[col][row].piece.cells_attacked(board_attack, col, row, "attack")
            if board[col][row].__repr__()[0] == "K":
                king_col = col
                king_row = row

    if board_attack[king_col][king_row] != 0:
        return False
    else:
        return True
