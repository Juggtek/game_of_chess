import imp
cell = imp.load_source('cell.py', '/home/felix/game_of_chess/board_pieces/cell.py')

class Piece(cell.Cell):
    def __init__(self, board, name, colour, col, row):
        self.name = name
        self.colour = colour
        self.col = col
        self.row = row
        self.move_count = 0
        self.board = board

    def movement(self, new_col, new_row):
        self.board[7-self.row][self.col] = "0 " # = Cell()
        self.col = new_col
        self.row = new_row
        self.board[7-self.row][self.col] = self.name + self.colour # = self.board[7-self.row][self.col].set_piece(self)
        self.move_count += 1
        return

    def get_position(self):
        return self.col, self.row
