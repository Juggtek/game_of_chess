from helper_func.repr_helper import get_piece_initials
from board_pieces.pawn import Pawn
from board_pieces.cell import Cell

class Board:
    def __init__(self):
        self.board = [ [Cell() for i in range(8)] for j in range(8)]

        for i in range(0,8):
            self.board[i][7-1].set_piece(Pawn(self.board,"P","w",i,1))
            self.board[i][7-6].set_piece(Pawn(self.board,"P","b",i,6))
        # white_knight_1 = Knight(board,"K","w",1,0)
        # white_knight_2 = Knight(board,"K","w",6,0)
        # white_bishop_1 = Bishop(board,"B","w",2,0)
        # white_bishop_2 = Bishop(board,"B","w",5,0)
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
        return tmp

    def move(self,from_col, from_row, to_col, to_row):
        self.board[from_col][7-from_row].piece.try_to_move(to_col, to_row)


    # def move(self, fromCol, fromRow, toCol, toRow):
    #     self.board[ocl][row].piece.try_to_move()
