def transform(cell):
    try:
        col = cell[0].lower()
        row =  int(cell[1]) - 1
        if (col == ("a" or "b" or "c" or "d" or "e" or "f" or "g" or "h")) and \
           (row >= 0 and row < 8):
            col = ord(cell[0]) - 65
            return "%s%s" % (col, row)
        else:
            return False
    except:
        return False
