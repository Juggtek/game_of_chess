from piece import Piece

class Pawn(Piece):
    def try_move(self, to_col, to_row):
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
                return True
            else:
                return False
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
                return True
            else:
                return False
        else:
            return False


    # TODO only Ture or False output for try_to_move()
    # TODO Transformation missing
    # TODO en passant

    def __repr__(self):
        return "P" + self.colour
