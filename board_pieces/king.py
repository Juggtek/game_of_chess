from piece import Piece
from piece_pin import piece_pin
import sys
sys.path.append('/home/felix/game_of_chess')
from helper_func.attack_cell import attack_cell
from helper_func.board_attack import board_attack

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
           self.board[0][7].piece.move_count == 0)) and \
           self.castle(self.board, self.col, self.row, to_col, self.colour):
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
           self.board[7][7].piece.move_count == 0)) and \
           self.castle(self.board, self.col, self.row, to_col, self.colour):
            self.board[7][self.row].piece.movement(5, self.row)
            return True

        elif (self.board[to_col][to_row].__repr__() != "0" and \
           self.board[to_col][to_row].__repr__()[1] == self.colour) or \
           (self.col == to_col and self.row == to_row) or \
           self.castle(self.board, self.col, self.row, to_col, self.colour):
            return False

        else:
            return False

# TODO check!

    def castle(self, board, from_col, row, to_col, colour):
        board_att = board_attack(board, colour)

        if (from_col > to_col and \
           board_att[from_col][row] == 0 and \
           board_att[from_col-1][row] == 0 and \
           board_att[from_col-2][row] == 0 and \
           board_att[from_col-3][row] == 0) or \
           (from_col < to_col and \
           board_att[from_col][row] == 0 and \
           board_att[from_col+1][row] == 0 and \
           board_att[from_col+2][row] == 0):
            return True
        else:
            return False

    def cells_attacked(self, board, col, row):
        attack_cell(board, col, row+1)
        attack_cell(board, col, row-1)
        attack_cell(board, col+1, row)
        attack_cell(board, col-1, row)
        attack_cell(board, col+1, row+1)
        attack_cell(board, col+1, row-1)
        attack_cell(board, col-1, row+1)
        attack_cell(board, col-1, row-1)

    def __repr__(self):
        return "K" + self.colour
