"""Game of Chess"""
from math import *
from board import Board, Cell
#from board_pieces.board_attack import BoardAttack


board = Board()
print board

board.move(6,0,4,1)
board.move(3,7,4,7)
board.move(4,1,5,3)
board.move(4,0,5,0)
board.move(4,7,1,4)
board.move(4,1,5,3)
