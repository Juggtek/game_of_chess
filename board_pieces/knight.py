from piece import Piece
import sys
sys.path.append('/home/felix/game_of_chess')
from helper_func.move_error import print_move_error

class Knight(Piece):
    def move(self, new_col, new_row):
        if self.board[7-new_row][new_col] == "0 " and \
           ((new_col == self.col + 1 and new_row == self.row + 2) or \
           (new_col == self.col + 1 and new_row == self.row - 2) or \
           (new_col == self.col + 2 and new_row == self.row + 1) or \
           (new_col == self.col + 2 and new_row == self.row - 1) or \
           (new_col == self.col - 1 and new_row == self.row + 2) or \
           (new_col == self.col - 1 and new_row == self.row - 2) or \
           (new_col == self.col - 2 and new_row == self.row + 1) or \
           (new_col == self.col - 2 and new_row == self.row - 1)):
            self.movement(new_col, new_row)
            self.move_count += 1
        else:
            print_move_error()

    def capture(self, new_col, new_row):
        if self.board[7-new_row][new_col][1] != "0 " and \
           self.board[7-new_row][new_col][1] != self.colour and \
           ((new_col == self.col + 1 and new_row == self.row + 2) or \
           (new_col == self.col + 1 and new_row == self.row - 2) or \
           (new_col == self.col + 2 and new_row == self.row + 1) or \
           (new_col == self.col + 2 and new_row == self.row - 1) or \
           (new_col == self.col - 1 and new_row == self.row + 2) or \
           (new_col == self.col - 1 and new_row == self.row - 2) or \
           (new_col == self.col - 2 and new_row == self.row + 1) or \
           (new_col == self.col - 2 and new_row == self.row - 1)):
            self.movement(new_col, new_row)
            self.move_count += 1
        else:
            print_move_error()
