from piece import Piece
import sys
sys.path.append('/home/felix/game_of_chess')
from helper_func.attack_cell import attack_cell

class King(Piece):
    def try_movement(self, to_col, to_row):

        if ((self.col + 1 == to_col and self.row == to_row \
            ) or ( \
            self.col - 1 == to_col and self.row == to_row \
            ) or ( \
            self.col == to_col and self.row + 1 == to_row \
            ) or ( \
            self.col == to_col and self.row - 1 == to_row \
            ) or ( \
            self.col + 1 == to_col and self.row + 1 == to_row \
            ) or ( \
            self.col + 1 == to_col and self.row - 1 == to_row \
            ) or ( \
            self.col - 1 == to_col and self.row + 1 == to_row \
            ) or ( \
            self.col - 1 == to_col and self.row - 1 == to_row \
            )) and ( \
            self.board[to_col][to_row].__repr__() == "0" or \
            (self.board[to_col][to_row].__repr__() != "0" and \
            self.board[to_col][to_row].piece.colour != self.colour)):
            return True

        elif to_col == self.col - 2 and self.row == to_row and \
           self.move_count == 0 and to_col < self.col and \
           ((self.row == 0 and self.colour == "w" and \
           self.board[3][0].__repr__() == "0" and \
           self.board[2][0].__repr__() == "0" and \
           self.board[1][0].__repr__() == "0" and \
           self.board[0][0].__repr__() == "Rw" and \
           self.board[0][0].piece.move_count == 0) or \
           (self.row == 7 and self.colour == "b" and \
           self.board[3][7].__repr__() == "0" and \
           self.board[2][7].__repr__() == "0" and \
           self.board[1][7].__repr__() == "0" and \
           self.board[0][7].__repr__() == "Rb" and \
           self.board[0][7].piece.move_count == 0)):
            self.board[0][self.row].piece.movement(3, self.row)
            return True

        elif to_col == self.col + 2 and self.row == to_row and \
           self.move_count == 0 and to_col > self.col and \
           ((self.row == 0 and self.colour == "w" and \
           self.board[5][0].__repr__() == "0" and \
           self.board[6][0].__repr__() == "0" and \
           self.board[7][0].__repr__() == "Rw" and \
           self.board[7][0].piece.move_count == 0) or \
           (self.row == 7 and self.colour == "b" and \
           self.board[5][7].__repr__() == "0" and \
           self.board[6][7].__repr__() == "0" and \
           self.board[7][7].__repr__() == "Rb" and \
           self.board[7][7].piece.move_count == 0)):
            self.board[7][self.row].piece.movement(5, self.row)
            return True

        elif (self.board[to_col][to_row].__repr__() != "0" and \
           self.board[to_col][to_row].__repr__()[1] == self.colour) or \
           (self.col == to_col and self.row == to_row):
            print "elif false"
            return False

        else:
            print "else false"
            return False

    def cells_attacked(self, board, col, row, att_or_stop):
        attack_cell(board, col, row+1, att_or_stop)
        attack_cell(board, col, row-1, att_or_stop)
        attack_cell(board, col+1, row, att_or_stop)
        attack_cell(board, col-1, row, att_or_stop)
        attack_cell(board, col+1, row+1, att_or_stop)
        attack_cell(board, col+1, row-1, att_or_stop)
        attack_cell(board, col-1, row+1, att_or_stop)
        attack_cell(board, col-1, row-1, att_or_stop)

    def __repr__(self):
        return "K" + self.colour
