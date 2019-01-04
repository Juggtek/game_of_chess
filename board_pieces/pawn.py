from piece import Piece
import imp # TODO https://stackoverflow.com/questions/67631/how-to-import-a-module-given-the-full-path
move_error = imp.load_source('move_error.py', '/home/felix/game_of_chess/helper_func/move_error.py')
capture_error = imp.load_source('capture_error.py', '/home/felix/game_of_chess/helper_func/capture_error.py')


class Pawn(Piece):
    def try_to_move(self, to_col, to_row):
        if self.colour == "w":
            if (
                    self.move_count == 0 and \
                    self.board[to_col][7-to_row].__repr__() == "0" and \
                    (to_col == self.col and to_row <= self.row + 2 and to_row > self.row)
               ) ^ ( \
                    self.move_count > 0 and \
                    self.board[to_col][7-to_row].__repr__() == "0" and \
                    (to_col == self.col and to_row == self.row + 1)
               ) ^ ( \
                    self.move_count > 0 and \
                    self.board[to_col][7-to_row].__repr__() != "0" and \
                    self.board[to_col][7-to_row].piece.colour == "b" and \
                    (to_col == self.col + 1 or to_col == self.col - 1) and to_row == self.row + 1):
                self.movement(to_col, to_row)
                self.move_count += 1
            else:
                move_error.print_move_error()
        elif self.colour == "b":
            if (
                    self.move_count == 0 and \
                    self.board[to_col][7-to_row].__repr__() == "0" and \
                    (to_col == self.col and to_row >= self.row - 2 and to_row < self.row)
               ) ^ ( \
                    self.move_count > 0 and \
                    self.board[to_col][7-to_row].__repr__() == "0" and \
                    (to_col == self.col and to_row == self.row - 1)
               ) ^ ( \
                    self.move_count > 0 and \
                    self.board[to_col][7-to_row].__repr__() != "0" and \
                    self.board[to_col][7-to_row].piece.colour == "w" and \
                    (to_col == self.col + 1 or to_col == self.col - 1) and to_row == self.row - 1):
                self.movement(to_col, to_row)
                self.move_count += 1
            else:
                move_error.print_move_error()
        else:
            move_error.print_move_error()


    # TODO only Ture or False output for try_to_move()
    # TODO Transformation missing
    # TODO en passant

    def __repr__(self):
        return "P" + self.colour
