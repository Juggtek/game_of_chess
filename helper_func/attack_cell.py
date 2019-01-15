def attack_cell(board, col, row):
    if col >= 0 and col <= 7 and row >= 0 and row <=7:
        board[col][row] += 1
    return board
