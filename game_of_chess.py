"""Game of Chess"""
from math import *
from board import Board, Cell


board = Board()
print board


board.move(3,1,3,3)
board.move(4,6,4,4)
board.move(4,4,3,3)
board.move(4,1,4,3)
board.move(4,3,4,4)
board.move(5,6,5,4)
board.move(4,4,5,5)
