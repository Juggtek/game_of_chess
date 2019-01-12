from piece import Piece
import sys
sys.path.append('/home/felix/game_of_chess')
from helper_func.attack_cell import attack_cell

class Rook(Piece):
    def try_movement(self, to_col, to_row):
        if self.col == to_col and self.row != to_row:
            if self.row < to_row:
                for row in range(self.row + 1, to_row + 1):
                    if self.board[self.col][row].__repr__() == "0" and \
                       row <= to_row:
                        bool = True
                    elif self.board[self.col][row].__repr__() != "0" and \
                       self.board[self.col][row].piece.colour != self.colour and \
                       row == to_row:
                        bool = True
                    elif self.board[self.col][row].__repr__() != "0" and \
                       self.board[self.col][row].piece.colour != self.colour and \
                       row < to_row:
                        bool = False
                        break
                    else:
                        bool = False
                        break

            elif self.row > to_row:
                for row in range(self.row - 1, to_row - 1, -1):
                    if self.board[self.col][row].__repr__() == "0" and \
                       row >= to_row:
                        bool = True
                    elif self.board[self.col][row].__repr__() != "0" and \
                       self.board[self.col][row].piece.colour != self.colour and \
                       row == to_row:
                        bool = True
                    elif self.board[self.col][row].__repr__() != "0" and \
                       self.board[self.col][row].piece.colour != self.colour and \
                       row > to_row:
                        bool = False
                        break
                    else:
                        bool = False
                        break

        elif self.col != to_col and self.row == to_row:
            if self.col < to_col:
                for col in range(self.col + 1, to_col + 1):
                    if self.board[col][self.row].__repr__() == "0" and \
                       col <= to_col:
                        bool = True
                    elif self.board[col][self.row].__repr__() != "0" and \
                       self.board[col][self.row].piece.colour != self.colour and \
                       col == to_col:
                        bool = True
                    elif self.board[col][self.row].__repr__() != "0" and \
                       self.board[col][self.row].piece.colour != self.colour and \
                       col < to_col:
                        bool = False
                        break
                    else:
                        return False
                        break

            elif self.col > to_col:
                for col in range(self.col - 1, to_col - 1, -1):
                    if self.board[col][self.row].__repr__() == "0" and \
                       col >= to_col:
                        bool = True
                    elif self.board[col][self.row].__repr__() != "0" and \
                       self.board[col][self.row].piece.colour != self.colour and \
                       col == to_col:
                        bool = True
                    elif self.board[col][self.row].__repr__() != "0" and \
                       self.board[col][self.row].piece.colour != self.colour and \
                       col > to_col:
                        bool = False
                    else:
                        return False
                        break
        else:
            bool = False
        return bool

    def cells_attacked(self, board, col, row, att_or_stop):
        row_p = row+1
        if row_p > 7:
            pass
        elif self.board[col][row_p].__repr__() != "0":
            attack_cell(board, col, row_p, att_or_stop)
        else:
            while self.board[col][row_p].__repr__() == "0":
                attack_cell(board, col, row_p, att_or_stop)
                row_p += 1
                if row_p > 7:
                    break
                elif self.board[col][row_p].__repr__() != "0":
                    attack_cell(board, col, row_p, att_or_stop)
                    break

        row_m = row-1
        if row_m < 0:
            pass
        elif self.board[col][row_m].__repr__() != "0":
            attack_cell(board, col, row_m, att_or_stop)
        else:
            while self.board[col][row_m].__repr__() == "0":
                attack_cell(board, col, row_m, att_or_stop)
                row_m -= 1
                if row_m < 0:
                    break
                elif self.board[col][row_m].__repr__() != "0":
                    attack_cell(board, col, row_m, att_or_stop)
                    break

        col_p = col+1
        if col_p > 7:
            pass
        elif self.board[col_p][row].__repr__() != "0":
            attack_cell(board, col_p, row, att_or_stop)
        else:
            while self.board[col_p][row].__repr__() == "0":
                attack_cell(board, col_p, row, att_or_stop)
                col_p += 1
                if col_p > 7:
                    break
                elif self.board[col_p][row].__repr__() != "0":
                    attack_cell(board, col_p, row, att_or_stop)
                    break


        col_m = col-1
        if col_m < 0:
            pass
        elif self.board[col_m][row].__repr__() != "0":
            attack_cell(board, col_m, row, att_or_stop)
        else:
            while self.board[col_m][row].__repr__() == "0":
                attack_cell(board, col_m, row, att_or_stop)
                col_m -= 1
                if col_m < 0:
                    break
                elif self.board[col_m][row].__repr__() != "0":
                    attack_cell(board, col_m, row, att_or_stop)
                    break



    def __repr__(self):
        return "R" + self.colour
