from board_attack import board_attack

def castle(board, from_col, row, to_col, colour):
    board_att = board_attack(board, colour)

    if (from_col > to_col and \
       board_att[from_col-1][row] == 0 and \
       board_att[from_col-2][row] == 0 and \
       board_att[from_col-3][row] == 0) or \
       (from_col < to_col and \
       board_att[from_col+1][row] == 0 and \
       board_att[from_col+2][row] == 0):
        return True
    else:
        return False
