"""Game of Chess"""
from math import *
from board import Board, Cell


board = Board()
print board

board.move(1,1,1,2)
board.move(2,0,1,1)
board.move(3,1,3,2)
board.move(3,0,3,1)
board.move(1,0,2,2)
board.move(4,0,2,0)
