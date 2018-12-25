"""Game of Chess"""
from math import *
import numpy as np

from board_pieces.piece import Piece
from board_pieces.pawn import Pawn
from board_pieces.knight import Knight

board = np.array([["0 "]*8]*8)



class Bishop(Piece):
    def move(self, new_col, new_row):
        next_col = self.col
        next_row = self.row

        if self.col < new_col and self.row < new_row and \
           (new_col - self.col) == (new_row - self.row):
            while next_col != new_col and next_row != new_row:
                next_col += 1
                next_row += 1
                if board[7-next_row][next_col] == "0 ":
                    pass
                else:
                    print "Invalid Movement!"
            next_col = self.col
            next_row = self.row
            self.movement(next_col, next_row)
            self.move_count += 1

        elif self.col < new_col and self.row > new_row and \
             (new_col - self.col) == (self.row - new_row):
            while next_col != new_col and next_row != new_row:
                next_col += 1
                next_row -= 1
                if board[7-next_row][next_col] == "0 ":
                    pass
                else:
                    print "Invalid Movement!"
            next_col = self.col
            next_row = self.row
            self.movement(next_col, next_row)
            self.move_count += 1

        elif self.col > new_col and self.row < new_row and \
             (self.col - new_col) == (new_row - self.row):
            while next_col != new_col and next_row != new_row:
                next_col -= 1
                next_row += 1
                if board[7-next_row][next_col] == "0 ":
                    pass
                else:
                    print "Invalid Movement!"
            next_col = self.col
            next_row = self.row
            self.movement(next_col, next_row)
            self.move_count += 1

        elif self.col > new_col and self.row > new_row and \
             (self.col - new_col) == (self.row - new_row):
            while next_col != new_col and next_row != new_row:
                next_col -= 1
                next_row -= 1
                if board[7-next_row][next_col] == "0 ":
                    pass
                else:
                    print "Invalid Movement!"
            next_col = self.col
            next_row = self.row
            self.movement(next_col, next_row)
            self.move_count += 1

        else:
            print "Invalid Movement!"
        return board

    def capture(self, new_col, new_row):
        next_col = self.col
        next_row = self.row

        if self.col < new_col and self.row < new_row and \
           (new_col - self.col) == (new_row - self.row):
            while next_col != new_col and next_row != new_row:
                next_col += 1
                next_row += 1
                if board[7-next_row][next_col] != "0 " and \
                     board[7-next_row][next_col][1] != self.colour:
                    self.movement(next_col, next_row)
                elif board[7-next_row][next_col] == "0 ":
                    print "Nothing to capture!"
                else:
                    print "Invalid Movement!"
            self.move_count += 1

        elif self.col < new_col and self.row > new_row and \
             (new_col - self.col) == (self.row - new_row):
            while next_col != new_col and next_row != new_row:
                next_col += 1
                next_row -= 1
                if board[7-next_row][next_col] != "0 " and \
                     board[7-next_row][next_col][1] != self.colour:
                    self.movement(next_col, next_row)
                elif board[7-next_row][next_col] == "0 ":
                    print "Nothing to capture!"
                else:
                    print "Invalid Movement!"
            self.move_count += 1

        elif self.col > new_col and self.row < new_row and \
             (self.col - new_col) == (new_row - self.row):
            while next_col != new_col and next_row != new_row:
                next_col -= 1
                next_row += 1
                if board[7-next_row][next_col] != "0 " and \
                     board[7-next_row][next_col][1] != self.colour:
                    self.movement(next_col, next_row)
                elif board[7-next_row][next_col] == "0 ":
                    print "Nothing to capture!"
                else:
                    print "Invalid Movement!"
            self.move_count += 1

        elif self.col > new_col and self.row > new_row and \
             (self.col - new_col) == (self.row - new_row):
            while next_col != new_col and next_row != new_row:
                next_col -= 1
                next_row -= 1
                if board[7-next_row][next_col] != "0 " and \
                     board[7-next_row][next_col][1] != self.colour:
                    self.movement(next_col, next_row)
                elif board[7-next_row][next_col] == "0 ":
                    print "Nothing to capture!"
                else:
                    print "Invalid Movement!"
            self.move_count += 1

        else:
            print "Invalid Movement!"
        return board


class Queen(Piece):
    def move(self, new_col, new_row):
        print "Queen"

        return



white_pawns = [None] * 8
for i in range(0,8):
    white_pawns[i] = Pawn(board, "P", "w",i,1)

k1 = Knight(board,"K","w",1,0)
k2 = Knight(board,"K","w",6,0)
b1 = Bishop(board,"B","w",2,0)

black_pawns = [None] * 8
for i in range(0,8):
    black_pawns[i] = Pawn(board, "P", "w",i,1)


white_pawns[3].move(3,2)

print board
