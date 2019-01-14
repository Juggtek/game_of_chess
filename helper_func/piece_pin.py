from board_attack import board_attack

def piece_pin(board, colour):
    board_att =  board_attack(board, colour)
    for col in range(8):
        for row in range(8):
            if board[col][row].__repr__() == "K" + colour:
                king_col = col
                king_row = row
    if board_att[king_col][king_row] != 0:
        return True
    else:
        return False
