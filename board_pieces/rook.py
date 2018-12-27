from piece import Piece
import imp
move_error = imp.load_source('move_error.py', '/home/felix/game_of_chess/helper_func/move_error.py')
capture_error = imp.load_source('capture_error.py', '/home/felix/game_of_chess/helper_func/capture_error.py')

class Rook(Piece):
    def move(self, new_col, new_row):
        if self.col == new_col and self.row != new_row:
            if self.row < new_row:
                for row in range(self.row+1, new_row+1):
                    if self.board[7-row][self.col] == "0 " and \
                       row == new_row:
                       self.movement(new_col, new_row)
                    elif self.board[7-row][self.col] != "0 ":
                        move_error.print_move_error()
                        break

            elif self.row > new_row:
                for row in range(self.row-1, new_row-1, -1):
                    if self.board[7-row][self.col] == "0 " and \
                       row == new_row:
                       self.movement(new_col, new_row)
                    elif self.board[7-row][self.col] != "0 ":
                        move_error.print_move_error()
                        break

        elif self.col != new_col and self.row == new_row:
            if self.col < new_col:
                for col in range(self.col+1, new_col+1):
                    if self.board[7-self.row][col] == "0 " and \
                       col == new_col:
                       self.movement(new_col, new_row)
                    elif self.board[7-self.row][col] != "0 ":
                        move_error.print_move_error()
                        break

            elif self.col > new_col:
                for col in range(self.col-1, new_col-1, -1):
                    if self.board[7-self.row][col] == "0 " and \
                       col == new_col:
                       self.movement(new_col, new_row)
                    elif self.board[7-self.row][col] != "0 ":
                        move_error.print_move_error()
                        break

        else:
            move_error.print_move_error()

    def capture(self, new_col, new_row):
        if self.col == new_col and self.row != new_row:
            if self.row < new_row:
                for row in range(self.row+1, new_row+1):
                    if self.board[7-row][self.col] != "0 " and \
                       self.board[7-row][self.col][1] != self.colour and \
                       row == new_row:
                       self.movement(new_col, new_row)
                    elif self.board[7-row][self.col] != "0 ":
                        move_error.print_move_error()
                        break

            elif self.row > new_row:
                for row in range(self.row-1, new_row-1, -1):
                    if self.board[7-row][self.col] != "0 " and \
                       self.board[7-row][self.col][1] != self.colour and \
                       row == new_row:
                       self.movement(new_col, new_row)
                    elif self.board[7-row][self.col] != "0 ":
                        move_error.print_move_error()
                        break

        elif self.col != new_col and self.row == new_row:
            if self.col < new_col:
                for col in range(self.col+1, new_col+1):
                    if self.board[7-self.row][col] != "0 " and \
                       self.board[7-self.row][col][1] != self.colour and \
                       col == new_col:
                       self.movement(new_col, new_row)
                    elif self.board[7-self.row][col] != "0 ":
                        move_error.print_move_error()
                        break

            elif self.col > new_col:
                for col in range(self.col-1, new_col-1, -1):
                    print col
                    if self.board[7-self.row][col] != "0 " and \
                       self.board[7-self.row][col][1] != self.colour and \
                       col == new_col:
                       self.movement(new_col, new_row)
                    elif self.board[7-self.row][col] != "0 ":
                        move_error.print_move_error()
                        break

        else:
            move_error.print_move_error()
