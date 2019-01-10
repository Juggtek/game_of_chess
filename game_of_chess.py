"""Game of Chess"""
from math import *
from board import Board, Cell
from board_pieces.board_attack import BoardAttack
board_attack = BoardAttack()

board = Board()
print board

board.move(0,1,0,3)
