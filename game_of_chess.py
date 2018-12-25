"""Game of Chess"""
from math import *
import numpy as np

from board_pieces.piece import Piece
from board_pieces.pawn import Pawn
from board_pieces.knight import Knight
from board_pieces.bishop import Bishop

board = np.array([["0 "]*8]*8)


class Queen(Piece):
    def move(self, new_col, new_row):
        print "Queen"

        return



white_pawns = [None] * 8
for i in range(0,8):
    white_pawns[i] = Pawn(board, "P", "w",i,1)

white_knight_1 = Knight(board,"K","w",1,0)
white_knight_2 = Knight(board,"K","w",6,0)
white_bishop_1 = Bishop(board,"B","w",2,0)
white_bishop_2 = Bishop(board,"B","w",5,0)

black_pawns = [None] * 8
for i in range(0,8):
    black_pawns[i] = Pawn(board, "P", "w",i,1)


white_pawns[3].move(3,2)

print board
white_bishop_1.move(5,3)
print board
white_bishop_1.move(4,4)
print board
white_bishop_1.move(3,3)
print board
white_bishop_1.move(1,1)


print board
