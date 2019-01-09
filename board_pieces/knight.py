from piece import Piece

class Knight(Piece):
    def try_movement(self, to_col, to_row):
        if self.board[to_col][7-to_row].__repr__() == "0" and \
           ((to_col == self.col + 1 and to_row == self.row + 2) or \
           (to_col == self.col + 1 and to_row == self.row - 2) or \
           (to_col == self.col + 2 and to_row == self.row + 1) or \
           (to_col == self.col + 2 and to_row == self.row - 1) or \
           (to_col == self.col - 1 and to_row == self.row + 2) or \
           (to_col == self.col - 1 and to_row == self.row - 2) or \
           (to_col == self.col - 2 and to_row == self.row + 1) or \
           (to_col == self.col - 2 and to_row == self.row - 1)):
            return True
        elif (self.board[to_col][7-to_row].__repr__() != "0" and \
           (self.board[to_col][7-to_row].piece.colour != self.board[self.col][7-self.row].piece.colour)) and \
           ((to_col == self.col + 1 and to_row == self.row + 2) or \
           (to_col == self.col + 1 and to_row == self.row - 2) or \
           (to_col == self.col + 2 and to_row == self.row + 1) or \
           (to_col == self.col + 2 and to_row == self.row - 1) or \
           (to_col == self.col - 1 and to_row == self.row + 2) or \
           (to_col == self.col - 1 and to_row == self.row - 2) or \
           (to_col == self.col - 2 and to_row == self.row + 1) or \
           (to_col == self.col - 2 and to_row == self.row - 1)):
            return True
        else:
            return False

    def cells_attacked(self, col, row, colour):
        if col == 0:
            self.board[col+1][7-row+1].attack_cell("w")
        elif col == 7:
            self.board[col-1][7-row+1].attack_cell("w")
        else:
            self.board[col+1][7-row+1].attack_cell("w")
            self.board[col-1][7-row+1].attack_cell("w")


    def __repr__(self):
        return "N" + self.colour
