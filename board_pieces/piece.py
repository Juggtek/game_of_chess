from piece_pin import piece_pin
import sys
sys.path.append('/home/felix/game_of_chess')
from board_pieces.cell import Cell

class Piece(Cell):
    def __init__(self, board, board_attack, name, colour, col, row):
        self.name = name
        self.colour = colour
        self.col = col
        self.row = row
        self.move_count = 0
        self.board = board
        self.board_attack = board_attack

    def movement(self, to_col, to_row):
        self.board[self.col][self.row].set_piece(None)
        self.board[to_col][to_row].set_piece(self)
        if not piece_pin(self.board, self.board[to_col][to_row].piece.colour):
            self.board[self.col][self.row].set_piece(self)
            self.board[to_col][to_row].set_piece(None)
        else:
            self.col = to_col
            self.row = to_row
            self.move_count += 1
        return

    def __repr__(self):
        return "%"
