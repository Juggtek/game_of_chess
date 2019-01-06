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

board.move(4,1,4,2)
board.move(3,0,5,2)
board.move(5,2,5,0)
board.move(5,2,4,2)
