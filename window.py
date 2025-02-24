from tkinter import Tk, BOTH, Canvas

class Window():
    def __init__(self, width, height,):
        self.root = Tk()
        self.root.title = "Maze Solver"
        self.root.winfo_x = width
        self.root.winfo_y = height

        self.canvas = Canvas(self.root)