class Cell:
    def __init__(self):
        self.piece = None

    def set_piece(self, piece):
        self.piece = piece

    def __repr__(self):
        if self.piece != None:
            return self.piece.__repr__()
        else:
            return "0"
