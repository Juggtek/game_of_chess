from piece import Piece

class Queen(Piece):
    def move(self, new_col, new_row):
        #bishop movement
        next_col = self.col
        next_row = self.row
        def check_cell(next_col, next_row):
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
                check_cell(next_col, next_row)

        elif self.col < new_col and self.row > new_row and \
             (new_col - self.col) == (self.row - new_row):
            while next_col != new_col and next_row != new_row:
                next_col += 1
                next_row -= 1
                check_cell(next_col, next_row)

        elif self.col > new_col and self.row < new_row and \
             (self.col - new_col) == (new_row - self.row):
            while next_col != new_col and next_row != new_row:
                next_col -= 1
                next_row += 1
                check_cell(next_col, next_row)

        elif self.col > new_col and self.row > new_row and \
             (self.col - new_col) == (self.row - new_row):
            while next_col != new_col and next_row != new_row:
                next_col -= 1
                next_row -= 1
                check_cell(next_col, next_row)

        #rook movement
        elif self.col == new_col and self.row != new_row:
            if self.row < new_row:
                for row in range(self.row+1, new_row+1):
                    if self.board[7-row][self.col] == "0 " and \
                       row == new_row:
                       self.movement(new_col, new_row)
                    elif self.board[7-row][self.col] != "0 ":
                        print "Invalid Movement!"
                        break

            elif self.row > new_row:
                for row in range(self.row-1, new_row-1, -1):
                    if self.board[7-row][self.col] == "0 " and \
                       row == new_row:
                       self.movement(new_col, new_row)
                    elif self.board[7-row][self.col] != "0 ":
                        print "Invalid Movement!"
                        break

        elif self.col != new_col and self.row == new_row:
            if self.col < new_col:
                for col in range(self.col+1, new_col+1):
                    if self.board[7-self.row][col] == "0 " and \
                       col == new_col:
                       self.movement(new_col, new_row)
                    elif self.board[7-self.row][col] != "0 ":
                        print "Invalid Movement!"
                        break

            elif self.col > new_col:
                for col in range(self.col-1, new_col-1, -1):
                    if self.board[7-self.row][col] == "0 " and \
                       col == new_col:
                       self.movement(new_col, new_row)
                    elif self.board[7-self.row][col] != "0 ":
                        print "Invalid Movement!"
                        break
        else:
            print "Invalid Movement!"

    def capture(self, new_col, new_row):
        #bishop capture
        next_col = self.col
        next_row = self.row
        def check_cell(next_col, next_row):
            if self.board[7-next_row][next_col] != "0 " and \
               next_col != new_col:
               print "Invalid Movement!"
            elif self.board[7-next_row][next_col] != "0 " and \
                 self.board[7-next_row][next_col][1] != self.colour and \
                 next_col == new_col:
                    self.movement(next_col, next_row)
            elif self.board[7-next_row][next_col] == "0 " and \
                 next_col == new_col:
                print "Nothing to capture"
            elif self.board[7-next_row][next_col] != "0 " and \
                 self.board[7-next_row][next_col][1] == self.colour and \
                 next_col == new_col:
                 print "Invalid Movement!"

        if self.col < new_col and self.row < new_row and \
           (new_col - self.col) == (new_row - self.row):
            while next_col != new_col and next_row != new_row:
                next_col += 1
                next_row += 1
                check_cell(next_col, next_row)

        elif self.col < new_col and self.row > new_row and \
             (new_col - self.col) == (self.row - new_row):
            while next_col != new_col and next_row != new_row:
                next_col += 1
                next_row -= 1
                check_cell(next_col, next_row)

        elif self.col > new_col and self.row < new_row and \
             (self.col - new_col) == (new_row - self.row):
            while next_col != new_col and next_row != new_row:
                next_col -= 1
                next_row += 1
                check_cell(next_col, next_row)

        elif self.col > new_col and self.row > new_row and \
             (self.col - new_col) == (self.row - new_row):
            while next_col != new_col and next_row != new_row:
                next_col -= 1
                next_row -= 1
                check_cell(next_col, next_row)

        #rook movement
        elif self.col == new_col and self.row != new_row:
            if self.row < new_row:
                for row in range(self.row+1, new_row+1):
                    if self.board[7-row][self.col] != "0 " and \
                       self.board[7-row][self.col][1] != self.colour and \
                       row == new_row:
                       self.movement(new_col, new_row)
                    elif self.board[7-row][self.col] != "0 ":
                        print "Invalid Movement!"
                        break

            elif self.row > new_row:
                for row in range(self.row-1, new_row-1, -1):
                    if self.board[7-row][self.col] != "0 " and \
                       self.board[7-row][self.col][1] != self.colour and \
                       row == new_row:
                       self.movement(new_col, new_row)
                    elif self.board[7-row][self.col] != "0 ":
                        print "Invalid Movement!"
                        break

        elif self.col != new_col and self.row == new_row:
            if self.col < new_col:
                for col in range(self.col+1, new_col+1):
                    if self.board[7-self.row][col] != "0 " and \
                       self.board[7-self.row][col][1] != self.colour and \
                       col == new_col:
                       self.movement(new_col, new_row)
                    elif self.board[7-self.row][col] != "0 ":
                        print "Invalid Movement!"
                        break

            elif self.col > new_col:
                for col in range(self.col-1, new_col-1, -1):
                    print col
                    if self.board[7-self.row][col] != "0 " and \
                       self.board[7-self.row][col][1] != self.colour and \
                       col == new_col:
                       self.movement(new_col, new_row)
                    elif self.board[7-self.row][col] != "0 ":
                        print "Invalid Movement!"
                        break

        else:
            print "Invalid Movement!"
