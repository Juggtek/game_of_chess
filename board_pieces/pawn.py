from piece import Piece
import imp
move_error = imp.load_source('move_error.py', '/home/felix/game_of_chess/helper_func/move_error.py')
capture_error = imp.load_source('capture_error.py', '/home/felix/game_of_chess/helper_func/capture_error.py')


class Pawn(Piece):
    def move(self, new_col, new_row):
        if (
               self.move_count == 0 and \
               self.board[7-new_row][new_col] == "0 " and \
               (new_col == self.col and new_row <= self.row + 2 and new_row > self.row)
           ) ^ ( \
               self.move_count > 0 and \
               self.board[7-new_row][new_col] == "0 " and \
               (new_col == self.col and new_row == self.row + 1)
           ):
            self.movement(new_col, new_row)
            self.move_count += 1
        else:
            move_error.print_move_error()

    def capture(self, new_col, new_row):
        if self.move_count > 0 and \
           self.board[7-new_row][new_col][1] != self.colour and \
           self.board[7-new_row][new_col][1] != " " and \
           (new_col == self.col + 1 or new_col == self.col - 1) and new_row == self.row + 1:
            self.movement(new_col, new_row)
            self.move_count += 1
        else:
            capture_error.print_capture_error()
    # TODO Transformation missing

    def __repr__(self):
        return "P" + self.colour
