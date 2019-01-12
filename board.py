from helper_func.repr_helper import get_piece_initials
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
        self.board_white_attack = [[0 for i in range(8)] for j in range(8)]
        self.board_black_attack = [[0 for i in range(8)] for j in range(8)]

        # for i in range(0,8):
        #     self.board[i][1].set_piece(Pawn(self.board,"P","w",i,1))
        #     self.board[i][6].set_piece(Pawn(self.board,"P","b",i,6))
        # self.board[1][0].set_piece(Knight(self.board,"N","w",1,0))
        # self.board[6][0].set_piece(Knight(self.board,"N","w",6,0))
        # self.board[1][7].set_piece(Knight(self.board,"N","b",1,7))
        # self.board[6][7].set_piece(Knight(self.board,"N","b",6,7))
        # self.board[2][0].set_piece(Bishop(self.board,"B","w",2,0))
        # self.board[5][0].set_piece(Bishop(self.board,"B","w",5,0))
        # self.board[2][7].set_piece(Bishop(self.board,"B","b",2,7))
        # self.board[5][7].set_piece(Bishop(self.board,"B","b",5,7))
        self.board[0][0].set_piece(Rook(self.board,"R","w",0,0))
        self.board[7][0].set_piece(Rook(self.board,"R","w",7,0))
        self.board[0][7].set_piece(Rook(self.board,"R","b",0,7))
        self.board[7][7].set_piece(Rook(self.board,"R","b",7,7))
        # self.board[3][0].set_piece(Queen(self.board,"Q","w",3,0))
        # self.board[3][7].set_piece(Queen(self.board,"Q","b",3,7))
        # self.board[4][0].set_piece(King(self.board,"K","w",4,0))
        # self.board[4][7].set_piece(King(self.board,"K","b",4,7))
        #
        #
        # for i in range(0,8):
        #     self.board[i][1].piece.cells_attacked(self.board_white_attack,i,1,"attack")
        #     self.board[i][6].piece.cells_attacked(self.board_black_attack,i,6,"attack")
        # self.board[1][0].piece.cells_attacked(self.board_white_attack,1,0,"attack")
        # self.board[6][0].piece.cells_attacked(self.board_white_attack,6,0,"attack")
        # self.board[1][7].piece.cells_attacked(self.board_black_attack,1,7,"attack")
        # self.board[6][7].piece.cells_attacked(self.board_black_attack,6,7,"attack")
        # self.board[2][0].piece.cells_attacked(self.board_white_attack,2,0,"attack")
        # self.board[5][0].piece.cells_attacked(self.board_white_attack,5,0,"attack")
        # self.board[2][7].piece.cells_attacked(self.board_black_attack,2,7,"attack")
        # self.board[5][7].piece.cells_attacked(self.board_black_attack,5,7,"attack")
        self.board[0][0].piece.cells_attacked(self.board_white_attack,0,0,"attack")
        self.board[7][0].piece.cells_attacked(self.board_white_attack,7,0,"attack")
        self.board[0][7].piece.cells_attacked(self.board_black_attack,0,7,"attack")
        self.board[7][7].piece.cells_attacked(self.board_black_attack,7,7,"attack")


    def move(self,from_col, from_row, to_col, to_row):
        if self.board[from_col][from_row].piece.try_movement(to_col, to_row):
            print "Moved from %s %s to %s %s" % (from_col, from_row, to_col, to_row)

            if self.board[from_col][from_row].piece.colour == "w":
                self.board[from_col][from_row].piece.cells_attacked(self.board_white_attack, from_col, from_row,"stop")
            elif self.board[from_col][from_row].piece.colour == "b":
                self.board[from_col][from_row].piece.cells_attacked(self.board_black_attack, from_col, from_row,"stop")

            self.board[from_col][from_row].piece.movement(to_col, to_row)

            if self.board[to_col][to_row].piece.colour == "w":
                self.board[to_col][to_row].piece.cells_attacked(self.board_white_attack, to_col, to_row,"attack")
            elif self.board[to_col][to_row].piece.colour == "b":
                self.board[to_col][to_row].piece.cells_attacked(self.board_black_attack, to_col, to_row,"attack")

            print self.__repr__()
        else:
            print "Moved from %s %s to %s %s" % (from_col, from_row, to_col, to_row)
            print_move_error()
            print self.__repr__()

    def __repr__(self):
        board = ""
        board_attack = ""
        for row in range(0,8):
            for col in range(0,8):
                board += get_piece_initials(self.board[col][7-row]).ljust(3)
                board_attack += "%s%s".ljust(5) % (self.board_white_attack[col][7-row], self.board_black_attack[col][7-row])
            board += "\n"
            board_attack += "\n"
        board += "\n"
        board_attack += "\n"
        return "\n" + board + "\n" + board_attack + "\n"
