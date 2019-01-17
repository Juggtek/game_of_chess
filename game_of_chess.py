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
        frame = StartBoard(container, self)
        self.frames.append(frame)
        frame.grid(column=0, row=0, sticky="nsew")

        self.show_frame(0)

    def show_frame(self, turn):
        frame = self.frames[turn]
        frame.tkraise()

class StartBoard(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        for col in range(8):
            for row in range(8):
                cell_input = board.__getitem__(col, row)
                if cell_input == "0":
                    cell_input = "".ljust(6)
                else:
                    cell_input.ljust(6)
                if float(col+row) % 2 > 0:
                    cell = tk.Button(self, text=cell_input, bg="white", relief="flat", takefocus="off")
                    cell.grid(column=col, row=row)
                else:
                    cell = tk.Button(self, text=cell_input, bg="lightblue", relief="flat", takefocus="off")
                    cell.grid(column=col, row=row)
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
app.mainloop()
