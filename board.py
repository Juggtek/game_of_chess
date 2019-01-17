from helper_func.repr_helper import get_piece_initials
from helper_func.piece_check import piece_check
from helper_func.board_attack import board_attack
from helper_func.move_error import print_move_error
from board_pieces.cell import Cell
from board_pieces.pawn import Pawn
from board_pieces.knight import Knight
from board_pieces.bishop import Bishop
from board_pieces.rook import Rook
from board_pieces.queen import Queen
from board_pieces.king import King

class Board:
    def __init__(self):
        self.board = [[Cell() for i in range(8)] for j in range(8)]

        for i in range(0,8):
            self.board[i][1].set_piece(Pawn(self.board,"P","w",i,1))
            self.board[i][6].set_piece(Pawn(self.board,"P","b",i,6))
        self.board[1][0].set_piece(Knight(self.board,"N","w",1,0))
        self.board[6][0].set_piece(Knight(self.board,"N","w",6,0))
        self.board[1][7].set_piece(Knight(self.board,"N","b",1,7))
        self.board[6][7].set_piece(Knight(self.board,"N","b",6,7))
        self.board[2][0].set_piece(Bishop(self.board,"B","w",2,0))
        self.board[5][0].set_piece(Bishop(self.board,"B","w",5,0))
        self.board[2][7].set_piece(Bishop(self.board,"B","b",2,7))
        self.board[5][7].set_piece(Bishop(self.board,"B","b",5,7))
        self.board[0][0].set_piece(Rook(self.board,"R","w",0,0))
        self.board[7][0].set_piece(Rook(self.board,"R","w",7,0))
        self.board[0][7].set_piece(Rook(self.board,"R","b",0,7))
        self.board[7][7].set_piece(Rook(self.board,"R","b",7,7))
        self.board[3][0].set_piece(Queen(self.board,"Q","w",3,0))
        self.board[3][7].set_piece(Queen(self.board,"Q","b",3,7))
        self.board[4][0].set_piece(King(self.board,"K","w",4,0))
        self.board[4][7].set_piece(King(self.board,"K","b",4,7))

    def move(self,from_col, from_row, to_col, to_row):
        print "Move from %s %s to %s %s" % (from_col, from_row, to_col, to_row)
        if self.board[from_col][from_row].piece.try_movement(to_col, to_row):
            if piece_check(self.board, self.board[from_col][from_row].piece.colour):
                self.board[from_col][from_row].piece.movement(to_col, to_row)
                if piece_check(self.board, self.board[to_col][to_row].piece.colour):
                    self.board[to_col][to_row].piece.movement(from_col, from_row)
                    self.board[from_col][from_row].piece.move_count -= 2
                    print_move_error()
            else:
                self.board[from_col][from_row].piece.movement(to_col, to_row)
                if piece_check(self.board, self.board[to_col][to_row].piece.colour):
                    self.board[to_col][to_row].piece.movement(from_col, from_row)
                    self.board[from_col][from_row].piece.move_count -= 2
                    print_move_error()
            print self.__repr__()
        else:
            print_move_error()
            print self.__repr__()

    def __getitem__(self, col, row):
        return self.board[col][row].__repr__()

    def __repr__(self):
        board = ""
        for row in range(8):
            for col in range(8):
                board += get_piece_initials(self.board[col][7-row]).ljust(3)
            board += "\n"
        board += "\n"

        board_att = ""
        for row in range(8):
            for col in range(8):
                board_att += "%s%s".ljust(5) % (board_attack(self.board,"b")[col][7-row], board_attack(self.board,"w")[col][7-row])
            board_att += "\n"
        board_att += "\n"

        return "\n" + board + "\n" + board_att + "\n"
