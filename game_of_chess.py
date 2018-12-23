"""Game of Chess"""
from math import *
import numpy as np

board = np.array([["0 "]*8]*8)

class Piece:
    def __init__(self, name, colour, col, row):
        self.name = name
        self.colour = colour
        self.col = col
        self.row = row
        self.move_count = 0

    def position(self):
        board[7-self.row][self.col] = self.name + self.colour
        return board

    def movement(self, new_col, new_row):
        board[7-self.row][self.col] = "0 "
        self.col = new_col
        self.row = new_row
        board[7-self.row][self.col] = self.name + self.colour
        return board


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
            self.movement(new_col, new_row)
            self.move_count += 1
        else:
            print "Invalid movement!"
        return board, self.move_count

    def capture(self, new_col, new_row):
        if self.move_count > 0 and \
           board[7-new_row][new_col][1] != self.colour and \
           board[7-new_row][new_col][1] != " " and \
           (new_col == self.col + 1 or new_col == self.col - 1) and new_row == self.row + 1:
            self.movement(new_col, new_row)
            self.move_count += 1
        else:
            print "Nothing to capture!"
        return board
    #Transformation missing

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
            self.movement(new_col, new_row)
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
            self.movement(new_col, new_row)
            self.move_count += 1
        else:
            print "Invalid movement!"
        return board

class Bishop(Piece):
    def move(self, new_col, new_row):
        next_col = self.col
        next_row = self.row
        if self.col < new_col and self.row < new_row:
            while next_col != new_col and next_row != new_row:
                next_col += 1
                next_row += 1
                if board[7-next_row][next_col] == "0 ":
                    self.movement(next_col, next_row)

                else:
                    print "Invalid Movement"
        #elif self.col < new_col and self.row > new_row














        return


p1 = Pawn("P","w",0,1)
p2 = Pawn("P","w",1,1)
p3 = Pawn("P","w",2,1)
p4 = Pawn("P","w",3,1)
p5 = Pawn("P","w",4,1)
p6 = Pawn("P","w",5,1)
p7 = Pawn("P","w",6,1)
p8 = Pawn("P","w",7,1)
p1.position()
p2.position()
p3.position()
p4.position()
p5.position()
p6.position()
p7.position()
p8.position()
k1 = Knight("K","w",1,0)
k2 = Knight("K","w",6,0)
k1.position()
k2.position()
b1 = Bishop("B","w",2,0)
b1.position()

p4.move(3,2)
b1.move(7,4)

print board
