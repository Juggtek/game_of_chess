"""Game of Chess"""
from math import *
from board import Board, Cell
#from board_pieces.board_attack import BoardAttack


board = Board()
print board

board.move(4,0,3,1)
board.move(4,0,2,0)
board.move(4,0,6,0)
