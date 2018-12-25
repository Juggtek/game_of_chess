class Knight(Piece):
    def move(self, new_col, new_row):
        if board[7-new_row][new_col] == "0 " and \
           ((new_col == self.col + 1 and new_row == self.row + 2) or \
           (new_col == self.col + 1 and new_row == self.row - 2) or \
           (new_col == self.col + 2 and new_row == self.row + 1) or \
           (new_col == self.col + 2 and new_row == self.row - 1) or \
           (new_col == self.col - 1 and new_row == self.row + 2) or \
           (new_col == self.col - 1 and new_row == self.row - 2) or \
           (new_col == self.col - 2 and new_row == self.row + 1) or \
           (new_col == self.col - 2 and new_row == self.row - 1)):
            self.movement(board, new_col, new_row)
            self.move_count += 1
        else:
            print "Invalid movement!"
        return board

    def capture(self, new_col, new_row):
        if board[7-new_row][new_col][1] != "0 " and \
           board[7-new_row][new_col][1] != self.colour and \
           ((new_col == self.col + 1 and new_row == self.row + 2) or \
           (new_col == self.col + 1 and new_row == self.row - 2) or \
           (new_col == self.col + 2 and new_row == self.row + 1) or \
           (new_col == self.col + 2 and new_row == self.row - 1) or \
           (new_col == self.col - 1 and new_row == self.row + 2) or \
           (new_col == self.col - 1 and new_row == self.row - 2) or \
           (new_col == self.col - 2 and new_row == self.row + 1) or \
           (new_col == self.col - 2 and new_row == self.row - 1)):
            self.movement(board, new_col, new_row)
            self.move_count += 1
        else:
            print "Invalid movement!"
        return board
