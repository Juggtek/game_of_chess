class Piece:
    def __init__(self, name, colour, col, row):
        self.name = name
        self.colour = colour
        self.col = col
        self.row = row
        self.move_count = 0

    def position(self, board):
        board[7-self.row][self.col] = self.name + self.colour
        return board

    def movement(self, board, new_col, new_row):
        board[7-self.row][self.col] = "0 "
        self.col = new_col
        self.row = new_row
        board[7-self.row][self.col] = self.name + self.colour
        return board
