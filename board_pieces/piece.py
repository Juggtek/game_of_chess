class Piece:
    def __init__(self, board, name, colour, col, row):
        self.name = name
        self.colour = colour
        self.col = col
        self.row = row
        self.move_count = 0
        self.board = board
        self.position()

    def position(self):
        self.board[7-self.row][self.col] = self.name + self.colour
        return

    def movement(self, new_col, new_row):
        self.board[7-self.row][self.col] = "0 "
        self.col = new_col
        self.row = new_row
        self.board[7-self.row][self.col] = self.name + self.colour
        return
