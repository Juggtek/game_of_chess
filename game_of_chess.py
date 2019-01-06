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
print board

board.move(0,1,0,3)
board.move(0,0,0,2)
board.move(0,2,7,2)
board.move(7,2,1,2)
board.move(1,2,1,6)
board.move(1,6,3,6)
