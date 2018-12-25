"""Game of Chess"""
from math import *
import numpy as np

from board_pieces.piece import Piece
from board_pieces.pawn import Pawn
from board_pieces.knight import knight

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
            self.movement(board, next_col, next_row)
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
            self.movement(board, next_col, next_row)
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
            self.movement(board, next_col, next_row)
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
            self.movement(board, next_col, next_row)
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
                    self.movement(board, next_col, next_row)
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
                    self.movement(board, next_col, next_row)
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
                    self.movement(board, next_col, next_row)
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
                    self.movement(board, next_col, next_row)
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




p1 = Pawn("P","w",0,1)
p2 = Pawn("P","w",1,1)
p3 = Pawn("P","w",2,1)
p4 = Pawn("P","w",3,1)
p5 = Pawn("P","w",4,1)
p6 = Pawn("P","w",5,1)
p7 = Pawn("P","w",6,1)
p8 = Pawn("P","w",7,1)
p1.position(board)
p2.position(board)
p3.position(board)
p4.position(board)
p5.position(board)
p6.position(board)
p7.position(board)
p8.position(board)
k1 = Knight("K","w",1,0)
k2 = Knight("K","w",6,0)
k1.position(board)
k2.position(board)
b1 = Bishop("B","w",2,0)
b1.position(board)

pb1 = Pawn("P","b",0,6)
pb2 = Pawn("P","b",1,6)
pb3 = Pawn("P","b",2,6)
pb4 = Pawn("P","b",3,6)
pb5 = Pawn("P","b",4,6)
pb6 = Pawn("P","b",5,6)
pb7 = Pawn("P","b",6,6)
pb8 = Pawn("P","b",7,6)
pb1.position()
pb2.position()
pb3.position()
pb4.position()
pb5.position()
pb6.position()
pb7.position()
pb8.position()


p4.move(3,2)
b1.move(5,3)



print board