from piece import Piece
from piece_pin import piece_pin
import sys
sys.path.append('/home/felix/game_of_chess')
from helper_func.attack_cell import attack_cell
from helper_func.piece_pin import piece_pin

class Pawn(Piece):
    en_passant_attackable = False

    def try_movement(self, to_col, to_row):
        if self.colour == "w":
            if self.move_count == 0 and \
               self.board[to_col][to_row].__repr__() == "0" and \
               (to_col == self.col and to_row <= self.row + 2 and to_row > self.row):
                self.en_passant(self.board, self.colour, self.col, self.row)
                return True

            elif (self.move_count > 0 and \
               self.board[to_col][to_row].__repr__() == "0" and \
               (to_col == self.col and to_row == self.row + 1) \
               ) or ( \
               self.move_count > 0 and \
               self.board[to_col][to_row].__repr__() != "0" and \
               self.board[to_col][to_row].piece.colour == "b" and \
               (to_col == self.col + 1 or to_col == self.col - 1) and to_row == self.row + 1):
                return True

            elif to_row == self.row + 1 and \
               (to_col == self.col + 1 or to_col == self.col - 1) and \
               self.en_passant_attack(self.board, self.col, self.row, to_col, to_row, self.colour):
                self.board[to_col][to_row-1].set_piece(None)
                return True
            else:
                return False

        elif self.colour == "b":
            if self.move_count == 0 and \
               self.board[to_col][to_row].__repr__() == "0" and \
               (to_col == self.col and to_row >= self.row - 2 and to_row < self.row):
                self.en_passant(self.board, self.colour, self.col, self.row)
                return True

            elif (self.move_count > 0 and \
               self.board[to_col][to_row].__repr__() == "0" and \
               (to_col == self.col and to_row == self.row - 1) \
               ) or ( \
               self.move_count > 0 and \
               self.board[to_col][to_row].__repr__() != "0" and \
               self.board[to_col][to_row].piece.colour == "w" and \
               (to_col == self.col + 1 or to_col == self.col - 1) and to_row == self.row - 1):
                return True

            elif to_row == self.row - 1 and \
               (to_col == self.col + 1 or to_col == self.col - 1) and \
               self.en_passant_attack(self.board, self.col, self.row, to_col, to_row, self.colour):
                self.board[to_col][to_row+1].set_piece(None)
                return True
            else:
                return False
        else:
            return False

    # TODO Transformation missing

    def cells_attacked(self, board, col, row, att_or_stop):
        if self.colour == "w":
            attack_cell(board, col+1, row+1, att_or_stop)
            attack_cell(board, col-1, row+1, att_or_stop)
        else:
            attack_cell(board, col+1, row-1, att_or_stop)
            attack_cell(board, col-1, row-1, att_or_stop)
        return board

    def en_passant(self, board, colour, col, row):
        print col, row
        if (colour == "w" and row == 1 and \
           ((col == 0 and board[1][3].__repr__() == "Pb") or \
           (col == 7 and board[6][3].__repr__() == "Pb") or \
           (col > 0 and col < 7 and (board[col+1][3].__repr__() == "Pb" or board[col-1][3].__repr__() == "Pb"))) \
           ) or ( \
           colour == "b" and row == 6 and \
           ((col == 0 and board[1][4].__repr__() == "Pw") or \
           (col == 7 and board[6][4].__repr__() == "Pw") or \
           (col > 0 and col < 7 and (board[col+1][4].__repr__() == "Pw" or board[col-1][4].__repr__() == "Pw"))) \
           ):
            self.board[col][row].piece.en_passant_attackable = True
        else:
            self.board[col][row].piece.en_passant_attackable = False

    def en_passant_attack(self, board, from_col, from_row, to_col, to_row, colour):
        if (colour == "w" and from_row == 4 and \
           ((from_col == 0 and board[1][4].piece.en_passant_attackable == True) or \
           (from_col == 7 and board[6][4].piece.en_passant_attackable == True) or \
           (from_col > 0 and from_col < 7 and \
           board[to_col][4].piece.en_passant_attackable == True)) \
           ) or ( \
           colour == "b" and from_row == 3 and \
           ((from_col == 0 and board[1][3].piece.en_passant == True) or \
           (from_col == 7 and board[6][3].piece.en_passant == True) or \
           (from_col > 0 and from_col < 7 and board[to_col][3].piece.en_passant_attackable == True))):

            self.board[from_col][from_row].piece.movement(to_row, to_col)
            if self.board[from_col][from_row].__repr__() != "0":
                return False
            else:
                self.board[to_col][to_row].piece.movement(from_row, from_col)
                self.board[from_col][from_row].piece.move_count -= 2
                return True
        else:
            return False

    def __repr__(self):
        return "P" + self.colour
