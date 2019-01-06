from piece import Piece

class Bishop(Piece):
    def try_movement(self, to_col, to_row):
        next_col = self.col
        next_row = self.row

        while next_col != to_col and next_row != to_row:
            if self.col < to_col and self.row < to_row and \
               (to_col - self.col) == (to_row - self.row):
                next_col += 1
                next_row += 1
            elif self.col < to_col and self.row > to_row and \
                 (to_col - self.col) == (self.row - to_row):
                next_col += 1
                next_row -= 1
            elif self.col > to_col and self.row < to_row and \
                 (self.col - to_col) == (to_row - self.row):
                next_col -= 1
                next_row += 1
            elif self.col > to_col and self.row > to_row and \
                 (self.col - to_col) == (self.row - to_row):
                next_col -= 1
                next_row -= 1
            else:
                bool = False
                break

            if (self.board[next_col][7-next_row].__repr__() == "0" and \
               (next_col < to_col or next_col > to_col)) or \
               ((self.board[next_col][7-next_row].__repr__() == "0" or \
               (self.board[next_col][7-next_row].__repr__() != "0" and \
               self.board[next_col][7-next_row].piece.colour != self.colour)) and \
               next_col == to_col):
                bool = True
            elif self.board[next_col][7-next_row].__repr__() != "0" and \
                 self.board[next_col][7-next_row].piece.colour == self.colour and \
                 next_col == to_col:
                bool = False
                break
            else:
                bool = False
                break

        return bool

    def __repr__(self):
        return "B" + self.colour
