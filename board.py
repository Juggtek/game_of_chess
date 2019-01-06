from helper_func.repr_helper import get_piece_initials
from helper_func.move_error import print_move_error
from board_pieces.cell import Cell
from board_pieces.pawn import Pawn
from board_pieces.knight import Knight
from board_pieces.bishop import Bishop
from board_pieces.rook import Rook
from board_pieces.queen import Queen
#from board_pieces.king import King

class Board:
    def __init__(self):
        self.board = [ [Cell() for i in range(8)] for j in range(8)]

        for i in range(0,8):
            self.board[i][7-1].set_piece(Pawn(self.board,"P","w",i,1))
            self.board[i][7-6].set_piece(Pawn(self.board,"P","b",i,6))
        self.board[2][7-0].set_piece(Knight(self.board,"K","w",2,0))
        self.board[5][7-0].set_piece(Knight(self.board,"K","w",5,0))
        self.board[2][7-7].set_piece(Knight(self.board,"K","b",2,7))
        self.board[5][7-7].set_piece(Knight(self.board,"K","b",5,7))
        self.board[1][7-0].set_piece(Bishop(self.board,"B","w",1,0))
        self.board[6][7-0].set_piece(Bishop(self.board,"B","w",6,0))
        self.board[1][7-7].set_piece(Bishop(self.board,"B","b",1,7))
        self.board[6][7-7].set_piece(Bishop(self.board,"B","b",6,7))
        self.board[0][7-0].set_piece(Rook(self.board,"R","w",0,0))
        self.board[7][7-0].set_piece(Rook(self.board,"R","w",7,0))
        self.board[0][7-7].set_piece(Rook(self.board,"R","b",0,7))
        self.board[7][7-7].set_piece(Rook(self.board,"R","b",7,7))
        # white_rook_1 = Rook(board,"R","w",0,0)
        # white_rook_2 = Rook(board,"R","w",7,0)
        # white_queen = Queen(board,"Q","w",3,0)
        # white_king = King(board,"K","w",2,0)
        #
        # black_pawns = [None] * 8
        # for i in range(0,8):
        #     black_pawns[i] = Pawn(board, "P", "b",i,6)

    def __repr__(self):
        tmp = ""
        for row in range(0,8):
            for col in range(0,8):
                tmp += get_piece_initials(self.board[col][row]).ljust(3)
            tmp += "\n"
        tmp += "\n"
        return "\n" + tmp + "\n"

    def move(self,from_col, from_row, to_col, to_row):
        if self.board[from_col][7-from_row].piece.try_movement(to_col, to_row):
            print "Moved from %s %s to %s %s" % (from_col, from_row, to_col, to_row)
            self.board[from_col][7-from_row].piece.movement(to_col, to_row)
            print self.__repr__()
        else:
            print "Moved from %s %s to %s %s" % (from_col, from_row, to_col, to_row)
            print_move_error()
            print self.__repr__()
