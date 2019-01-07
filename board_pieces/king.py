from piece import Piece

class King(Piece):
    def try_movement(self, to_col, to_row):

        if ((self.col + 1 == to_col and self.row == to_row \
            ) or ( \
            self.col - 1 == to_col and self.row == to_row \
            ) or ( \
            self.col == to_col and self.row + 1 == to_row \
            ) or ( \
            self.col == to_col and self.row - 1 == to_row \
            ) or ( \
            self.col + 1 == to_col and self.row + 1 == to_row \
            ) or ( \
            self.col + 1 == to_col and self.row - 1 == to_row \
            ) or ( \
            self.col - 1 == to_col and self.row + 1 == to_row \
            ) or ( \
            self.col - 1 == to_col and self.row - 1 == to_row \
            )) and ( \
            self.board[to_col][7-to_row].__repr__() == "0" or \
            (self.board[to_col][7-to_row].__repr__() != "0" and \
            self.board[to_col][7-to_row].piece.colour != self.colour)):
            return True

        elif to_col == self.col - 2 and self.row == to_row and \
           self.move_count == 0 and to_col < self.col and \
           ((self.row == 0 and self.colour == "w" and \
           self.board[3][7-0].__repr__() == "0" and \
           self.board[2][7-0].__repr__() == "0" and \
           self.board[1][7-0].__repr__() == "0" and \
           self.board[0][7-0].__repr__() == "Rw" and \
           self.board[0][7-0].piece.move_count == 0) or \
           (self.row == 7 and self.colour == "b" and \
           self.board[3][7-7].__repr__() == "0" and \
           self.board[2][7-7].__repr__() == "0" and \
           self.board[1][7-7].__repr__() == "0" and \
           self.board[0][7-7].__repr__() == "Rb" and \
           self.board[0][7-7].piece.move_count == 0)):
            self.board[0][7-self.row].piece.movement(3, self.row)
            return True

        elif to_col == self.col + 2 and self.row == to_row and \
           self.move_count == 0 and to_col > self.col and \
           ((self.row == 0 and self.colour == "w" and \
           self.board[5][7-0].__repr__() == "0" and \
           self.board[6][7-0].__repr__() == "0" and \
           self.board[7][7-0].__repr__() == "Rw" and \
           self.board[7][7-0].piece.move_count == 0) or \
           (self.row == 7 and self.colour == "b" and \
           self.board[5][7-7].__repr__() == "0" and \
           self.board[6][7-7].__repr__() == "0" and \
           self.board[7][7-7].__repr__() == "Rb" and \
           self.board[7][7-7].piece.move_count == 0)):
            self.board[7][7-self.row].piece.movement(5, self.row)
            return True

        elif (self.board[to_col][7-to_row].__repr__() != "0" and \
           self.board[to_col][7-to_row].__repr__()[1] == self.colour) or \
           (self.col == to_col and self.row == to_row):
            print "elif false"
            return False

        else:
            print "else false"
            return False

    def __repr__(self):
        return "K" + self.colour
