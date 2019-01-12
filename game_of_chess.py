"""Game of Chess"""
from math import *
from board import Board, Cell
#from board_pieces.board_attack import BoardAttack


board = Board()
print board

board.move(0,0,3,0)
board.move(3,0,3,3)
