"""Game of Chess"""
from math import *
import numpy as np

from board_pieces.piece import Piece
from board_pieces.pawn import Pawn
from board_pieces.knight import Knight
from board_pieces.bishop import Bishop
from board_pieces.rook import Rook
from board_pieces.queen import Queen

board = np.array([["0 "]*8]*8)



white_pawns = [None] * 8
for i in range(0,8):
    white_pawns[i] = Pawn(board, "P", "w",i,1)
white_knight_1 = Knight(board,"K","w",1,0)
white_knight_2 = Knight(board,"K","w",6,0)
white_bishop_1 = Bishop(board,"B","w",2,0)
white_bishop_2 = Bishop(board,"B","w",5,0)
white_rook_1 = Rook(board,"R","w",0,0)
white_rook_2 = Rook(board,"R","w",7,0)
white_queen = Queen(board,"Q","b",3,0)

black_pawns = [None] * 8
for i in range(0,8):
    black_pawns[i] = Pawn(board, "P", "b",i,6)


white_pawns[3].move(3,2)
print board, "\n"
