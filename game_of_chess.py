"""Game of Chess"""
from math import *
from board import Board, Cell
from Tkinter import *
import Tkinter as tk

board = Board()
print board


class Window(tk.Tk):
    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = []
        frame = Board(container, self)
        self.frames.append(frame)
        frame.grid(column=0, row=0, sticky="nsew")

        self.show_frame()

        # while True:
        #     if frame.check_input():
        #         turn = frame.turn
        #         board.move(turn[0][0], turn[0][1], turn[1][0], turn[1][1])
        #         frame = Board(container, self)
        #         frame.turn = []
        #         self.frames.append(frame)
        #         frame.grid(column=0, row=0, sticky="nsew")
        #         self.show_frame()
        #         break
        #     else:
        #         pass
        #         print "passed"

    def show_frame(self):
        frame = self.frames[-1]
        frame.tkraise()

    # def button_command(self, cell):
    #     print "x", cell.winfo_rootx()
    #     print "y", cell.winfo_rooty()

class Board(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.turn = []

        for col in range(8):
            for row in range(8):
                cell_input = board.__getitem__(col, row)

                if cell_input == "0":
                    cell_input = "".ljust(6)
                else:
                    cell_input.ljust(6)
                if float(col+row) % 2 > 0:
                    cell = self.button_def(cell_input, "white")
                    cell.grid(column=col, row=row)
                else:
                    cell = self.button_def(cell_input, "lightblue")
                    cell.grid(column=col, row=row)

    def check_input(self):
        if len(self.turn) == 2:
            return True
        else:
            return False

    def button_def(self, cell_input, colour):
        tk.Button(self, text=cell_input, bg=colour, relief="flat", takefocus="off", command= self.button_command(cell))
        return

    def button_command(self, cell):
        x, y = self.cell.winfo_rootx(), self.cell.winfo_rooty()
        print "x", cell.winfo_rootx()
        print "y", cell.winfo_rooty()


    # def move_command(self, col, row):
    #     self.turn.append([col,row])
    #     print "self.turn", self.turn
            # if len(self.turn) == 2:
            #     board.move(self.turn[0][0], self.turn[0][1], self.turn[1][0], self.turn[1][1])
            #     self.turn = []





    #     self.frames = {}
    #     frame = Start(container, self)
    #     self.frames[Start] = frame
    #
    #     frame.grid(row=0, column=0, sticky="nsew")
    #
    #     self.show_frame(Start)
    #
    # def show_frame(self, cont):
    #
    #     frame = self.frames[cont]
    #     frame.tkraise()


# class Start(tk.Frame):
#
#     def __init__(self, parent, controller):
#         tk.Frame.__init__(self, parent)
#         button = tk.Button(self, text="Button", font=("Verdana", 12))
#         button.pack()

    # def init_window(self):
    #     self.master.title("Chess")
    #     self.pack(fill=BOTH, expand=1)
    #
    #     button1 = Button(self, text="P", bg="brown", relief=FLAT, takefocus="off", highlightthickness="0")
    #     button1.grid(column=0,row=0)


#root.geometry("400x400")
app= Window()
app.geometry("400x400")
app.mainloop()
