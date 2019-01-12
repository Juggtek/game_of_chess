from piece import Piece
import sys
sys.path.append('/home/felix/game_of_chess')
from helper_func.attack_cell import attack_cell

class Knight(Piece):
    def try_movement(self, to_col, to_row):
        if self.board[to_col][to_row].__repr__() == "0" and \
           ((to_col == self.col + 1 and to_row == self.row + 2) or \
           (to_col == self.col + 1 and to_row == self.row - 2) or \
           (to_col == self.col + 2 and to_row == self.row + 1) or \
           (to_col == self.col + 2 and to_row == self.row - 1) or \
           (to_col == self.col - 1 and to_row == self.row + 2) or \
           (to_col == self.col - 1 and to_row == self.row - 2) or \
           (to_col == self.col - 2 and to_row == self.row + 1) or \
           (to_col == self.col - 2 and to_row == self.row - 1)):
            return True
        elif (self.board[to_col][to_row].__repr__() != "0" and \
           (self.board[to_col][to_row].piece.colour != self.board[self.col][self.row].piece.colour)) and \
           ((to_col == self.col + 1 and to_row == self.row + 2) or \
           (to_col == self.col + 1 and to_row == self.row - 2) or \
           (to_col == self.col + 2 and to_row == self.row + 1) or \
           (to_col == self.col + 2 and to_row == self.row - 1) or \
           (to_col == self.col - 1 and to_row == self.row + 2) or \
           (to_col == self.col - 1 and to_row == self.row - 2) or \
           (to_col == self.col - 2 and to_row == self.row + 1) or \
           (to_col == self.col - 2 and to_row == self.row - 1)):
            return True
        else:
            return False

    def cells_attacked(self, board, col, row, att_or_stop):
        attack_cell(board, col+1, row+2, att_or_stop)
        attack_cell(board, col+1, row-2, att_or_stop)
        attack_cell(board, col+2, row+1, att_or_stop)
        attack_cell(board, col+2, row-1, att_or_stop)
        attack_cell(board, col-1, row+2, att_or_stop)
        attack_cell(board, col-1, row-2, att_or_stop)
        attack_cell(board, col-2, row+1, att_or_stop)
        attack_cell(board, col-2, row-1, att_or_stop)
        return board

    def __repr__(self):
        return "N" + self.colour
