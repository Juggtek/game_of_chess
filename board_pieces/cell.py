class Cell:
    def __init__(self):
        self.piece = None
        self.attacked_from_white = False
        self.attacked_from_black = False

    def set_piece(self, piece):
        self.piece = piece

    def attack_cell(self, colour):
        if colour == "w":
            self.attacked_from_white = True
        elif colour == "b":
            self.attacked_from_black = True
        else:
            print "No colour entered"

    def __repr__(self):
        if self.piece != None:
            return self.piece.__repr__()
        else:
            return "0"
