def board_attack(board, colour):
    board_attack = [[0 for i in range(8)] for j in range(8)]
    for col in range(8):
        for row in range(8):
            if board[col][row].__repr__() != "0" and board[col][row].__repr__()[1] != colour:
                board[col][row].piece.cells_attacked(board_attack, col, row)
    return board_attack
