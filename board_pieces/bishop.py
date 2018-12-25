from piece import Piece

class Bishop(Piece):
    def move(self, new_col, new_row):
        next_col = self.col
        next_row = self.row

        def check_cell_is_empty(next_col, next_row):
            if self.board[7-next_row][next_col] == "0 " and \
                next_col == new_col:
                    self.movement(next_col, next_row)
            elif self.board[7-next_row][next_col] != "0 ":
                print "Invalid Movement!"

        if self.col < new_col and self.row < new_row and \
           (new_col - self.col) == (new_row - self.row):
            while next_col != new_col and next_row != new_row:
                next_col += 1
                next_row += 1
                check_cell_is_empty(next_col, next_row)

        elif self.col < new_col and self.row > new_row and \
             (new_col - self.col) == (self.row - new_row):
            while next_col != new_col and next_row != new_row:
                next_col += 1
                next_row -= 1
                check_cell_is_empty(next_col, next_row)

        elif self.col > new_col and self.row < new_row and \
             (self.col - new_col) == (new_row - self.row):
            while next_col != new_col and next_row != new_row:
                next_col -= 1
                next_row += 1
                check_cell_is_empty(next_col, next_row)

        elif self.col > new_col and self.row > new_row and \
             (self.col - new_col) == (self.row - new_row):
            while next_col != new_col and next_row != new_row:
                next_col -= 1
                next_row -= 1
                check_cell_is_empty(next_col, next_row)
        else:
            print "Invalid Movement!"

    # def capture(self, new_col, new_row):
    #     next_col = self.col
    #     next_row = self.row
    #
    #     if self.col < new_col and self.row < new_row and \
    #        (new_col - self.col) == (new_row - self.row):
    #         while next_col != new_col and next_row != new_row:
    #             next_col += 1
    #             next_row += 1
    #             if self.board[7-next_row][next_col] != "0 " and \
    #                  self.board[7-next_row][next_col][1] != self.colour:
    #                 self.movement(next_col, next_row)
    #             elif self.board[7-next_row][next_col] == "0 ":
    #                 print "Nothing to capture!"
    #             else:
    #                 print "Invalid Movement!"
    #         self.move_count += 1
    #
    #     elif self.col < new_col and self.row > new_row and \
    #          (new_col - self.col) == (self.row - new_row):
    #         while next_col != new_col and next_row != new_row:
    #             next_col += 1
    #             next_row -= 1
    #             if self.board[7-next_row][next_col] != "0 " and \
    #                  self.board[7-next_row][next_col][1] != self.colour:
    #                 self.movement(next_col, next_row)
    #             elif self.board[7-next_row][next_col] == "0 ":
    #                 print "Nothing to capture!"
    #             else:
    #                 print "Invalid Movement!"
    #         self.move_count += 1
    #
    #     elif self.col > new_col and self.row < new_row and \
    #          (self.col - new_col) == (new_row - self.row):
    #         while next_col != new_col and next_row != new_row:
    #             next_col -= 1
    #             next_row += 1
    #             if self.board[7-next_row][next_col] != "0 " and \
    #                  self.board[7-next_row][next_col][1] != self.colour:
    #                 self.movement(next_col, next_row)
    #             elif self.board[7-next_row][next_col] == "0 ":
    #                 print "Nothing to capture!"
    #             else:
    #                 print "Invalid Movement!"
    #         self.move_count += 1
    #
    #     elif self.col > new_col and self.row > new_row and \
    #          (self.col - new_col) == (self.row - new_row):
    #         while next_col != new_col and next_row != new_row:
    #             next_col -= 1
    #             next_row -= 1
    #             if self.board[7-next_row][next_col] != "0 " and \
    #                  self.board[7-next_row][next_col][1] != self.colour:
    #                 self.movement(next_col, next_row)
    #             elif self.board[7-next_row][next_col] == "0 ":
    #                 print "Nothing to capture!"
    #             else:
    #                 print "Invalid Movement!"
    #         self.move_count += 1
    #
    #     else:
    #         print "Invalid Movement!"
    #     return self.board