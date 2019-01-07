import sys
sys.path.append('/home/felix/game_of_chess')
from board_pieces.cell import Cell

class Piece(Cell):
    def __init__(self, board, name, colour, col, row):
        self.name = name
        self.colour = colour
        self.col = col
        self.row = row
        self.move_count = 0
        self.board = board

    def movement(self, to_col, to_row):
        self.board[self.col][7-self.row].set_piece(None)
        self.col = to_col
        self.row = to_row
        self.board[self.col][7-self.row].set_piece(self)
        self.move_count += 1
        return

    def get_position(self):
        return self.col, self.row

    def __repr__(self):
        return "%"
