"""Game of Chess"""
from math import *
from board import Board, Cell


board = Board()
print board

board.move(3,7,4,6)
board.move(6,0,7,2)
board.move(6,0,4,1)
board.move(4,1,5,3)
board.move(2,0,4,2)
board.move(7,7,7,0)
board.move(4,2,6,0)
