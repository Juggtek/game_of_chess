from board_pieces.pawn import Pawn

def get_piece_initials(obj):
    if obj != None:
        if isinstance(obj, Pawn):
            return "P" + obj.colour
        else:
            return "-"
    else:
        return "0"
