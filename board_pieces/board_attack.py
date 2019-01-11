# import sys
# sys.path.append('/home/felix/game_of_chess')
# from board import Board

class BoardAttack:
    def __init__(self, board):
        self.board = board
        self.board_attack = [[[0,0] for i in range(8)] for j in range(8)]

    def attack_cell(self, col, row, colour, att_or_stop):
        if att_or_stop == "attack" and \
           col >= 0 and col <= 7 and row >= 0 and col <=7:
            if colour == "w":
                self.board_attack[col][7-row][0] += 1
            elif colour == "b":
                self.board_attack[col][7-row][1] += 1
        elif att_or_stop == "stop" and \
           col >= 0 and col <= 7 and row >= 0 and col <=7:
            if colour == "w":
                self.board_attack[col][7-row][0] -= 1
            elif colour == "b":
                self.board_attack[col][7-row][1] -= 1
        else:
            pass

    def piece_attacks(self, col, row, att_or_stop):
        self.board[col][7-row].piece.cells_attacked(col, row, att_or_stop)

    def __repr__(self):
        tmp = ""
        for row in range(0,8):
            for col in range(0,8):
                tmp += str(self.board_attack[col][row]).ljust(7)
            tmp += "\n \n"
        tmp += "\n"
        return "\n" + tmp + "\n"
