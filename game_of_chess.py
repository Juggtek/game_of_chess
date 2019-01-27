"""Game of Chess"""
from math import *
from board import Board, Cell
from helper_func.move_error import print_move_error
from Tkinter import *
import Tkinter as tk

board = Board()
print board


def transform_input(cell):
    if (cell[0] == "1" or \
       cell[0] == "2" or \
       cell[0] == "3" or \
       cell[0] == "4" or \
       cell[0] == "5" or \
       cell[0] == "6" or \
       cell[0] == "7" or \
       cell[0] == "8") and \
       (int(cell[1]) > 0 and int(cell[1]) < 9):
        return "%s%s" % (int(cell[0])-1, int(cell[1])-1)
    elif (cell[0].lower() == "a" or \
       cell[0].lower() == "b" or \
       cell[0].lower() == "c" or \
       cell[0].lower() == "d" or \
       cell[0].lower() == "e" or \
       cell[0].lower() == "f" or \
       cell[0].lower() == "g" or \
       cell[0].lower() == "h") and \
       (int(cell[1]) > 0 and int(cell[1]) < 9):
        return "%s%s" % (ord(cell[0].lower()) - 97, int(cell[1])-1)
    else:
        print_move_error()

while True:
    from_col_row = raw_input("From column/row: ")
    to_col_row = raw_input("To column/row: ")
    if len(from_col_row) == 2 and len(to_col_row) == 2:
        from_trans = transform_input(from_col_row)
        to_trans = transform_input(to_col_row)
        temp_board = board.move(int(from_trans[0]), int(from_trans[1]), int(to_trans[0]), int(to_trans[1]))
    else:
        print_move_error()

# while True:
#     from_col_row = raw_input("From column/row: ")
#     to_col_row = raw_input("To column/row: ")
#     if check_input(from_col_row) and check_input(from_col_row):
#         if isinstance(from_col_row[0], str) and isinstance(to_col_row[0], str):
#             from_col = int(from_col_row[0]) - 1
#             to_col = int(to_col_row[0]) - 1
#         else:
#             from_col = ord(from_col_row[0].lower()) - 97
#             to_col = ord(to_col_row[0].lower()) - 97
#         from_row =  int(from_col_row[1]) - 1
#         to_row =  int(to_col_row[1]) - 1
#         temp_board = board.move(from_col, from_row, to_col, to_row)
#     else:
#         print_move_error()


# class Window(tk.Tk):
#     def __init__(self, *args, **kwargs):
#
#         tk.Tk.__init__(self, *args, **kwargs)
#         container = tk.Frame(self)
#
#         container.pack(side="top", fill="both", expand=True)
#
#         container.grid_rowconfigure(0, weight=1)
#         container.grid_columnconfigure(0, weight=1)
#
#         self.frames = []
#         frame = Board(container, self)
#         self.frames.append(frame)
#         frame.grid(column=0, row=0, sticky="nsew")
#
#         self.show_frame()
#
#         # while True:
#         #     if frame.check_input():
#         #         turn = frame.turn
#         #         board.move(turn[0][0], turn[0][1], turn[1][0], turn[1][1])
#         #         frame = Board(container, self)
#         #         frame.turn = []
#         #         self.frames.append(frame)
#         #         frame.grid(column=0, row=0, sticky="nsew")
#         #         self.show_frame()
#         #         break
#         #     else:
#         #         pass
#         #         print "passed"
#
#     def show_frame(self):
#         frame = self.frames[-1]
#         frame.tkraise()
#
#     # def button_command(self, cell):
#     #     print "x", cell.winfo_rootx()
#     #     print "y", cell.winfo_rooty()
#
# class Board(tk.Frame):
#
#     def __init__(self, parent, controller):
#         tk.Frame.__init__(self, parent)
#         self.turn = []
#
#         for col in range(8):
#             for row in range(8):
#                 cell_input = board.__getitem__(col, row)
#
#                 if cell_input == "0":
#                     cell_input = "".ljust(6)
#                 else:
#                     cell_input.ljust(6)
#                 if float(col+row) % 2 > 0:
#                     cell = self.button_def(cell_input, "white")
#                     cell.grid(column=col, row=row)
#                 else:
#                     cell = self.button_def(cell_input, "lightblue")
#                     cell.grid(column=col, row=row)
#
#     def check_input(self):
#         if len(self.turn) == 2:
#             return True
#         else:
#             return False
#
#     def button_def(self, cell_input, colour):
#         tk.Button(self, text=cell_input, bg=colour, relief="flat", takefocus="off", command= self.button_command(cell))
#         return
#
#     def button_command(self, cell):
#         x, y = self.cell.winfo_rootx(), self.cell.winfo_rooty()
#         print "x", cell.winfo_rootx()
#         print "y", cell.winfo_rooty()
#
#
#     # def move_command(self, col, row):
#     #     self.turn.append([col,row])
#     #     print "self.turn", self.turn
#             # if len(self.turn) == 2:
#             #     board.move(self.turn[0][0], self.turn[0][1], self.turn[1][0], self.turn[1][1])
#             #     self.turn = []
#
#
#
#
#
#     #     self.frames = {}
#     #     frame = Start(container, self)
#     #     self.frames[Start] = frame
#     #
#     #     frame.grid(row=0, column=0, sticky="nsew")
#     #
#     #     self.show_frame(Start)
#     #
#     # def show_frame(self, cont):
#     #
#     #     frame = self.frames[cont]
#     #     frame.tkraise()
#
#
# # class Start(tk.Frame):
# #
# #     def __init__(self, parent, controller):
# #         tk.Frame.__init__(self, parent)
# #         button = tk.Button(self, text="Button", font=("Verdana", 12))
# #         button.pack()
#
#     # def init_window(self):
#     #     self.master.title("Chess")
#     #     self.pack(fill=BOTH, expand=1)
#     #
#     #     button1 = Button(self, text="P", bg="brown", relief=FLAT, takefocus="off", highlightthickness="0")
#     #     button1.grid(column=0,row=0)
#
#
# #root.geometry("400x400")
# app= Window()
# app.geometry("400x400")
# app.mainloop()
