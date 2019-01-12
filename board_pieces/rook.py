from piece import Piece

class Rook(Piece):
    def try_movement(self, to_col, to_row):
        if self.col == to_col and self.row != to_row:
            if self.row < to_row:
                for row in range(self.row + 1, to_row + 1):
                    if self.board[self.col][row].__repr__() == "0" and \
                       row <= to_row:
                        bool = True
                    elif self.board[self.col][row].__repr__() != "0" and \
                       self.board[self.col][row].piece.colour != self.colour and \
                       row == to_row:
                        bool = True
                    elif self.board[self.col][row].__repr__() != "0" and \
                       self.board[self.col][row].piece.colour != self.colour and \
                       row < to_row:
                        bool = False
                        break
                    else:
                        bool = False
                        break

            elif self.row > to_row:
                for row in range(self.row - 1, to_row - 1, -1):
                    if self.board[self.col][row].__repr__() == "0" and \
                       row >= to_row:
                        bool = True
                    elif self.board[self.col][row].__repr__() != "0" and \
                       self.board[self.col][row].piece.colour != self.colour and \
                       row == to_row:
                        bool = True
                    elif self.board[self.col][row].__repr__() != "0" and \
                       self.board[self.col][row].piece.colour != self.colour and \
                       row > to_row:
                        bool = False
                        break
                    else:
                        bool = False
                        break

        elif self.col != to_col and self.row == to_row:
            if self.col < to_col:
                for col in range(self.col + 1, to_col + 1):
                    if self.board[col][self.row].__repr__() == "0" and \
                       col <= to_col:
                        bool = True
                    elif self.board[col][self.row].__repr__() != "0" and \
                       self.board[col][self.row].piece.colour != self.colour and \
                       col == to_col:
                        bool = True
                    elif self.board[col][self.row].__repr__() != "0" and \
                       self.board[col][self.row].piece.colour != self.colour and \
                       col < to_col:
                        bool = False
                        break
                    else:
                        return False
                        break

            elif self.col > to_col:
                for col in range(self.col - 1, to_col - 1, -1):
                    if self.board[col][self.row].__repr__() == "0" and \
                       col >= to_col:
                        bool = True
                    elif self.board[col][self.row].__repr__() != "0" and \
                       self.board[col][self.row].piece.colour != self.colour and \
                       col == to_col:
                        bool = True
                    elif self.board[col][self.row].__repr__() != "0" and \
                       self.board[col][self.row].piece.colour != self.colour and \
                       col > to_col:
                        bool = False
                    else:
                        return False
                        break
        else:
            bool = False
        return bool

    def __repr__(self):
        return "R" + self.colour
