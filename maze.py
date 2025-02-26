import time
from cell import *
from point import *

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win

        self.create_cells()

    def create_cells(self):
        self.cells = []

        for i in range(0, self.num_cols):
            self.cells.append([])
            for j in range(0, self.num_rows):
                point_1 = Point(self.x1 + (self.cell_size_x * i), self.y1 + (self.cell_size_y * j))
                point_2 = Point(self.x1 + (self.cell_size_x * (i+1)), self.y1 + (self.cell_size_y * (j+1)))
                self.cells[i].append(Cell(point_1, point_2, self.win, True, True, True, True))
                self.draw_cell(self.cells[i][j])

    def draw_cell(self, cell):
        cell.draw()
        self.animate()

    def animate(self):
        self.win.redraw()
        time.sleep(0.05)