from piece import Piece
import imp
move_error = imp.load_source('move_error.py', '/home/felix/game_of_chess/helper_func/move_error.py')
capture_error = imp.load_source('capture_error.py', '/home/felix/game_of_chess/helper_func/capture_error.py')

class King(Piece):
    def move(self, new_col, new_row):
        if  (
            self.col + 1 == new_col and self.row == new_row \
            ) ^ ( \
            self.col - 1 == new_col and self.row == new_row \
            ) ^ ( \
            self.col == new_col and self.row + 1 == new_row \
            ) ^ ( \
            self.col == new_col and self.row - 1 == new_row \
            ) ^ ( \
            self.col + 1 == new_col and self.row + 1 == new_row \
            ) ^ ( \
            self.col + 1 == new_col and self.row - 1 == new_row \
            ) ^ ( \
            self.col - 1 == new_col and self.row + 1 == new_row \
            ) ^ ( \
            self.col - 1 == new_col and self.row - 1 == new_row \
            ) and \
            self.board[7-new_row][new_col] == "0 ":
            self.movement(new_col, new_row)

        elif self.board[7-new_row][new_col][1] == self.colour or \
             new_col > self.col + 1 or new_row > self.row + 1 or \
             (self.col == new_col and self.row == new_row):
            move_error.print_move_error()

        else:
            move_error.print_move_error()


    def capture(self, new_col, new_row):
        if  (
            self.col + 1 == new_col and self.row == new_row \
            ) ^ ( \
            self.col - 1 == new_col and self.row == new_row \
            ) ^ ( \
            self.col == new_col and self.row + 1 == new_row \
            ) ^ ( \
            self.col == new_col and self.row - 1 == new_row \
            ) ^ ( \
            self.col + 1 == new_col and self.row + 1 == new_row \
            ) ^ ( \
            self.col + 1 == new_col and self.row - 1 == new_row \
            ) ^ ( \
            self.col - 1 == new_col and self.row + 1 == new_row \
            ) ^ ( \
            self.col - 1 == new_col and self.row - 1 == new_row \
            ) and \
            self.board[7-new_row][new_col] != "0 " and \
            self.board[7-new_row][new_col][1] != self.colour:
            self.movement(new_col, new_row)

        elif self.board[7-new_row][new_col][1] == self.colour or \
             new_col > self.col + 1 or new_row > self.row + 1 or \
             (self.col == new_col and self.row == new_row):
            move_error.print_move_error()

        else:
            move_error.print_move_error()

    def castle(self, new_col, new_row = self.row):
        if self.colour == "w"
           (new_col == self.col + 2 ^ new_col == self.col - 2) and \
           new_row == self.row and \
           self.board[7-self.row][new_col] == "R" + self.colour and \
           ((
           self.board[7-self.row][new_col-1] == "0 " and self.board[7-self.row][new_col-2] == "0 " \
           ) ^ ( \
           self.board[7-self.row][new_col+1] == "0 " and self.board[7-self.row][new_col+2] == "0 " and self.board[7-self.row][new_col+3] == "0 " \
           )):
           self.movement(new_col, self.row)
        elif self.colour == "b"
             (new_col == self.col + 2 ^ new_col == self.col - 2) and \
             new_row == self.row and \
             self.board[7-self.row][new_col] == "R" + self.colour and \
             ((
             self.board[7-self.row][new_col-1] == "0 " and self.board[7-self.row][new_col-2] == "0 " and self.board[7-self.row][new_col-3] == "0 " \
             ) ^ ( \
             self.board[7-self.row][new_col+1] == "0 " and self.board[7-self.row][new_col+2] == "0 " \
             )):
             self.movement(new_col, self.row)
        else:
            move_error.print_move_error()
