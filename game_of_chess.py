"""Game of Chess"""
from math import *
from board import Board, Cell


board = Board()
print board

board.move(6,1,6,2)
board.move(5,0,6,1)
board.move(6,0,5,2)
board.move(1,1,1,2)
board.move(2,0,1,1)
board.move(1,0,2,2)
board.move(3,1,3,3)
board.move(3,0,3,2)
board.move(4,0,2,0)

board.move(1,6,1,5)
board.move(2,7,1,6)
board.move(1,7,2,5)
board.move(3,6,3,4)
board.move(3,7,3,5)
board.move(6,6,6,5)
board.move(6,7,5,5)
board.move(5,7,6,6)
board.move(4,7,2,7)
board.move(2,7,0,7)
