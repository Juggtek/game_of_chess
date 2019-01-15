import sys
sys.path.append('/home/felix/game_of_chess')
from board_pieces.cell import Cell

class Piece(Cell):
    def __init__(self, board, name, colour, col, row):
        self.name = name
        self.colour = colour
        self.col = col
        self.row = row
        self.board = board
        self.move_count = 0

    def movement(self, to_col, to_row):
        self.board[self.col][self.row].set_piece(None)
        self.board[to_col][to_row].set_piece(self)
        self.col = to_col
        self.row = to_row
        self.move_count += 1
        return

    def __repr__(self):
        return "%"
