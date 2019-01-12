"""Game of Chess"""
from math import *
from board import Board, Cell
#from board_pieces.board_attack import BoardAttack


board = Board()
print board

board.move(4,0,4,1)
board.move(4,1,4,2)
