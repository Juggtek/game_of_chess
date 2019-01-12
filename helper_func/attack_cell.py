def attack_cell(board, row, col, att_or_stop):
    if att_or_stop == "attack" and \
       col >= 0 and col <= 7 and row >= 0 and row <=7:
        print "col ", col, " row ", row
        board[col][row] += 1
    elif att_or_stop == "stop" and \
       col >= 0 and col <= 7 and row >= 0 and row <=7:
            board[col][row] -= 1
    return board
