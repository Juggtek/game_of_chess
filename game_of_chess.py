"""Game of Chess"""
from math import *
from board import Board, Cell
from helper_func.move_error import print_move_error
from helper_func.chess_language import transform


board = Board()
print board

def check_input(cell):
    if transform(cell) == True:
        return True
    else:
        return False

while True:

    from_col_row = raw_input("From column/row: ")
    to_col_row = raw_input("To column/row: ")
    print "t", transform(from_col_row)
    print check_input(to_col_row) == True
    if (check_input(from_col_row) and check_input(to_col_row)) == True:
        trans_from = transform(from_col_row)
        trans_to = transform(to_col_row)
        board.move(trans_from[0],trans_from[1],trans_to[0],trans_to[1])
    else:
        print_move_error()
