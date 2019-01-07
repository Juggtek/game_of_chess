class Cell:
    def __init__(self):
        self.piece = None
        self.under_attack_from = None

    def set_piece(self, piece):
        self.piece = piece

    def attack_cell(self, piece.colour):
        self.under_attack_from = piece.colour

    def __repr__(self):
        if self.piece != None:
            return self.piece.__repr__()
        else:
            return "0"
