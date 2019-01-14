from piece import Piece
from piece_pin import piece_pin
import sys
sys.path.append('/home/felix/game_of_chess')
from helper_func.attack_cell import attack_cell

class Pawn(Piece):
    def try_movement(self, to_col, to_row):
        if self.colour == "w":
            if (
                    self.move_count == 0 and \
                    self.board[to_col][to_row].__repr__() == "0" and \
                    (to_col == self.col and to_row <= self.row + 2 and to_row > self.row)
               ) ^ ( \
                    self.move_count > 0 and \
                    self.board[to_col][to_row].__repr__() == "0" and \
                    (to_col == self.col and to_row == self.row + 1)
               ) ^ ( \
                    self.move_count > 0 and \
                    self.board[to_col][to_row].__repr__() != "0" and \
                    self.board[to_col][to_row].piece.colour == "b" and \
                    (to_col == self.col + 1 or to_col == self.col - 1) and to_row == self.row + 1):
                return True
            else:
                return False
        elif self.colour == "b":
            if (
                    self.move_count == 0 and \
                    self.board[to_col][to_row].__repr__() == "0" and \
                    (to_col == self.col and to_row >= self.row - 2 and to_row < self.row)
               ) ^ ( \
                    self.move_count > 0 and \
                    self.board[to_col][to_row].__repr__() == "0" and \
                    (to_col == self.col and to_row == self.row - 1)
               ) ^ ( \
                    self.move_count > 0 and \
                    self.board[to_col][to_row].__repr__() != "0" and \
                    self.board[to_col][to_row].piece.colour == "w" and \
                    (to_col == self.col + 1 or to_col == self.col - 1) and to_row == self.row - 1):
                return True
            else:
                return False
        else:
            return False

    # TODO Transformation missing
    # TODO en passant

    def cells_attacked(self, board, col, row, att_or_stop):
        if self.colour == "w":
            attack_cell(board, col+1, row+1, att_or_stop)
            attack_cell(board, col-1, row+1, att_or_stop)
        else:
            attack_cell(board, col+1, row-1, att_or_stop)
            attack_cell(board, col-1, row-1, att_or_stop)
        return board


    def __repr__(self):
        return "P" + self.colour
