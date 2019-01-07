from piece import Piece

class Queen(Piece):
    def try_movement(self,to_col, to_row):
        if self.col == to_col and self.row != to_row:
            if self.row < to_row:
                for row in range(self.row + 1, to_row + 1):
                    if self.board[self.col][7-row].__repr__() == "0" and \
                       row <= to_row:
                        bool = True
                    elif self.board[self.col][7-row].__repr__() != "0" and \
                       self.board[self.col][7-row].piece.colour != self.colour and \
                       row == to_row:
                        bool = True
                    elif self.board[self.col][7-row].__repr__() != "0" and \
                       self.board[self.col][7-row].piece.colour != self.colour and \
                       row < to_row:
                        bool = False
                        break
                    else:
                        bool = False
                        break

            elif self.row > to_row:
                for row in range(self.row - 1, to_row - 1, -1):
                    if self.board[self.col][7-row].__repr__() == "0" and \
                       row >= to_row:
                        bool = True
                    elif self.board[self.col][7-row].__repr__() != "0" and \
                       self.board[self.col][7-row].piece.colour != self.colour and \
                       row == to_row:
                        bool = True
                    elif self.board[self.col][7-row].__repr__() != "0" and \
                       self.board[self.col][7-row].piece.colour != self.colour and \
                       row > to_row:
                        bool = False
                        break
                    else:
                        bool = False
                        break

        elif self.col != to_col and self.row == to_row:
            if self.col < to_col:
                for col in range(self.col + 1, to_col + 1):
                    if self.board[col][7-self.row].__repr__() == "0" and \
                       col <= to_col:
                        bool = True
                    elif self.board[col][7-self.row].__repr__() != "0" and \
                       self.board[col][7-self.row].piece.colour != self.colour and \
                       col == to_col:
                        bool = True
                    elif self.board[col][7-self.row].__repr__() != "0" and \
                       self.board[col][7-self.row].piece.colour != self.colour and \
                       col < to_col:
                        bool = False
                        break
                    else:
                        return False
                        break

            elif self.col > to_col:
                for col in range(self.col - 1, to_col - 1, -1):
                    if self.board[col][7-self.row].__repr__() == "0" and \
                       col >= to_col:
                        bool = True
                    elif self.board[col][7-self.row].__repr__() != "0" and \
                       self.board[col][7-self.row].piece.colour != self.colour and \
                       col == to_col:
                        bool = True
                    elif self.board[col][7-self.row].__repr__() != "0" and \
                       self.board[col][7-self.row].piece.colour != self.colour and \
                       col > to_col:
                        bool = False
                    else:
                        return False
                        break

        elif self.col != to_col and self.row != to_row:
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
        else:
            bool = False
        return bool

    def __repr__(self):
        return "Q" + self.colour
