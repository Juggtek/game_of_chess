class Pawn(Piece):
    def move(self, new_col, new_row):
        if (
               self.move_count == 0 and \
               board[7-new_row][new_col] == "0 " and \
               (new_col == self.col and new_row <= self.row + 2 and new_row > self.row)
           ) ^ ( \
               self.move_count > 0 and \
               board[7-new_row][new_col] == "0 " and \
               (new_col == self.col and new_row == self.row + 1)
           ):
            self.movement(board, new_col, new_row)
            self.move_count += 1
        else:
            print "Invalid movement!"
        return board, self.move_count

    def capture(self, new_col, new_row):
        if self.move_count > 0 and \
           board[7-new_row][new_col][1] != self.colour and \
           board[7-new_row][new_col][1] != " " and \
           (new_col == self.col + 1 or new_col == self.col - 1) and new_row == self.row + 1:
            self.movement(board, new_col, new_row)
            self.move_count += 1
        else:
            print "Nothing to capture!"
        return board
    #Transformation missing
