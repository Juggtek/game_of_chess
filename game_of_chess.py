"""Game of Chess"""
from math import *
from board import Board, Cell
from helper_func.move_error import print_move_error


board = Board()
print board


def check_input(cell):
    if ((cell[0].lower() == "a") or \
       (cell[0].lower() == "b") or \
       (cell[0].lower() == "c") or \
       (cell[0].lower() == "d") or \
       (cell[0].lower() == "e") or \
       (cell[0].lower() == "f") or \
       (cell[0].lower() == "g") or \
       (cell[0].lower() == "h")) and \
       (int(cell[1]) > 0 and int(cell[1]) < 9):
        return True
    else:
        return False

while True:
    from_col_row = raw_input("From column/row: ")
    to_col_row = raw_input("To column/row: ")
    if check_input(from_col_row) and check_input(from_col_row):
        from_row =  int(from_col_row[1]) - 1
        from_col = ord(from_col_row[0].lower()) - 97
        to_row =  int(to_col_row[1]) - 1
        to_col = ord(to_col_row[0].lower()) - 97
        board.move(from_col, from_row, to_col, to_row)
    else:
        print_move_error()

#
# while True:
#
#     from_col_row = raw_input("From column/row: ")
#     to_col_row = raw_input("To column/row: ")
#     print "t", transform(from_col_row)
#     print check_input(to_col_row) == True
#     if (check_input(from_col_row) and check_input(to_col_row)) == True:
#         trans_from = transform(from_col_row)
#         trans_to = transform(to_col_row)
#         board.move(trans_from[0],trans_from[1],trans_to[0],trans_to[1])
#     else:
#         print_move_error()
