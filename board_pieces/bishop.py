from piece import Piece
import imp
move_error = imp.load_source('move_error.py', '/home/felix/game_of_chess/helper_func/move_error.py')
capture_error = imp.load_source('capture_error.py', '/home/felix/game_of_chess/helper_func/capture_error.py')

class Bishop(Piece):
    def move(self, new_col, new_row):
        next_col = self.col
        next_row = self.row

        def check_cell(next_col, next_row):
            if self.board[7-next_row][next_col] == "0 " and \
               next_col == new_col:
                    self.movement(next_col, next_row)
            elif self.board[7-next_row][next_col] != "0 ":
                move_error.print_move_error()

        if self.col < new_col and self.row < new_row and \
           (new_col - self.col) == (new_row - self.row):
            while next_col != new_col and next_row != new_row:
                next_col += 1
                next_row += 1
                check_cell(next_col, next_row)

        elif self.col < new_col and self.row > new_row and \
             (new_col - self.col) == (self.row - new_row):
            while next_col != new_col and next_row != new_row:
                next_col += 1
                next_row -= 1
                check_cell(next_col, next_row)

        elif self.col > new_col and self.row < new_row and \
             (self.col - new_col) == (new_row - self.row):
            while next_col != new_col and next_row != new_row:
                next_col -= 1
                next_row += 1
                check_cell(next_col, next_row)

        elif self.col > new_col and self.row > new_row and \
             (self.col - new_col) == (self.row - new_row):
            while next_col != new_col and next_row != new_row:
                next_col -= 1
                next_row -= 1
                check_cell(next_col, next_row)
        else:
            move_error.print_move_error()


    def capture(self, new_col, new_row):
        next_col = self.col
        next_row = self.row

        def check_cell(next_col, next_row):
            if self.board[7-next_row][next_col] != "0 " and \
               next_col != new_col:
               move_error.print_move_error()
            elif self.board[7-next_row][next_col] != "0 " and \
                 self.board[7-next_row][next_col][1] != self.colour and \
                 next_col == new_col:
                    self.movement(next_col, next_row)
            elif self.board[7-next_row][next_col] == "0 " and \
                 next_col == new_col:
                 move_error.print_move_error()
            elif self.board[7-next_row][next_col] != "0 " and \
                 self.board[7-next_row][next_col][1] == self.colour and \
                 next_col == new_col:
                 move_error.print_move_error()

        if self.col < new_col and self.row < new_row and \
           (new_col - self.col) == (new_row - self.row):
            while next_col != new_col and next_row != new_row:
                next_col += 1
                next_row += 1
                check_cell(next_col, next_row)

        elif self.col < new_col and self.row > new_row and \
             (new_col - self.col) == (self.row - new_row):
            while next_col != new_col and next_row != new_row:
                next_col += 1
                next_row -= 1
                check_cell(next_col, next_row)

        elif self.col > new_col and self.row < new_row and \
             (self.col - new_col) == (new_row - self.row):
            while next_col != new_col and next_row != new_row:
                next_col -= 1
                next_row += 1
                check_cell(next_col, next_row)

        elif self.col > new_col and self.row > new_row and \
             (self.col - new_col) == (self.row - new_row):
            while next_col != new_col and next_row != new_row:
                next_col -= 1
                next_row -= 1
                check_cell(next_col, next_row)
        else:
            move_error.print_move_error()
