"""Game of Chess"""
from math import *


from board import Board, Cell
# from board_pieces.piece import Piece
#from board_pieces.pawn import Pawn
# from board_pieces.knight import Knight
# from board_pieces.bishop import Bishop
# from board_pieces.rook import Rook
# from board_pieces.queen import Queen
# from board_pieces.king import King
#board = np.array([["0 "]*8]*8)

board = Board()
print board, "\n"

board.move(2,1,2,2)
print board, "\n"
board.move(1,0,3,2)
print board, "\n"
board.move(3,2,1,4)
print board, "\n"
board.move(1,4,2,5)
print board, "\n"
board.move(2,5,5,2)
print board, "\n"
board.move(5,2,4,3)
print board, "\n"
board.move(4,3,6,1)
print board, "\n"
board.move(4,3,1,6)
print board, "\n"
board.move(1,6,6,1)
print board, "\n"
