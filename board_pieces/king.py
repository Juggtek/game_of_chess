from piece import Piece

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
            print "Invalid Movement"

        else:
            print "Invalid Movement"


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
            print "Invalid Movement"

        else:
            print "Invalid Movement"
