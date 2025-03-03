import time
import random

from cell import *
from point import *

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win

        if seed is not None:
            random.seed(seed)

        self.create_cells()
        self.break_entrance_and_exit_walls()
        self.break_walls_r(0, 0)
        self.reset_cells_visited()
        self.solve()
        
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
        if self.win is not None:
            cell.draw()
            self.animate()

    def animate(self):
        self.win.redraw()
        time.sleep(0.05)

    def break_entrance_and_exit_walls(self):
        self.cells[0][0].has_left_wall = False
        self.draw_cell(self.cells[0][0])

        self.cells[-1][-1].has_right_wall = False
        self.draw_cell(self.cells[-1][-1]) 

    def break_walls_r(self, i, j):
        def can_go_up(i, j):
            if (j-1 >= 0) and (self.cells[i][j-1].visited == False):
                return True
            else:
                return False

        def can_go_down(i, j):
            if (j <= self.num_rows-2) and (self.cells[i][j+1].visited == False):
                return True
            else:
                return False
            
        def can_go_left(i, j):
            if (i-1 >= 0) and (self.cells[i-1][j].visited == False):
                return True
            else:
                return False
            
        def can_go_right(i, j):
            if (i <= self.num_cols-2) and (self.cells[i+1][j].visited == False):
                return True
            else:
                return False
          
        self.cells[i][j].visited = True
        while True:
            to_visit = []
            if can_go_up(i, j) == True:
                to_visit.append([i, j-1, "up"])
            if can_go_down(i, j) == True:
                to_visit.append([i, j+1, "down"])
            if can_go_left(i, j) == True:
                to_visit.append([i-1, j, "left"])
            if can_go_right(i, j) == True:
                to_visit.append([i+1, j, "right"])

            if to_visit == []:
                self.draw_cell(self.cells[i][j])
                return
            
            rand_cell = random.choice(to_visit)
            if rand_cell[2] == "up":
                self.cells[i][j].has_top_wall = False
                self.draw_cell(self.cells[i][j])
                self.cells[i][j-1].has_bottom_wall = False
                self.draw_cell(self.cells[i][j-1])

            elif rand_cell[2] == "down":
                self.cells[i][j].has_bottom_wall = False
                self.draw_cell(self.cells[i][j])
                self.cells[i][j+1].has_top_wall = False
                self.draw_cell(self.cells[i][j+1])

            elif rand_cell[2] == "left":
                self.cells[i][j].has_left_wall = False
                self.draw_cell(self.cells[i][j])
                self.cells[i-1][j].has_right_wall = False
                self.draw_cell(self.cells[i-1][j])

            elif rand_cell[2] == "right":
                self.cells[i][j].has_right_wall = False
                self.draw_cell(self.cells[i][j])
                self.cells[i+1][j].has_left_wall = False
                self.draw_cell(self.cells[i+1][j])

            self.break_walls_r(rand_cell[0], rand_cell[1])
                
    def reset_cells_visited(self):
        for i in range(0, self.num_cols):
            for j in range(0, self.num_rows):
                self.cells[i][j].visited = False

    def solve(self):
        return self.solve_r(0, 0)

    def solve_r(self, i, j):
        self.animate()
        self.cells[i][j].visited = True
        if self.cells[i][j] == self.cells[-1][-1]:
            return True
        
        #try going right:
        if (i <= self.num_cols-2) and (self.cells[i][j].has_right_wall == False) and (self.cells[i+1][j].visited == False):
            self.cells[i][j].draw_move(self.cells[i+1][j])
            if self.solve_r(i+1, j) == True:
                return True
            else:
                self.cells[i][j].draw_move(self.cells[i+1][j], True)
            
        #try going down:
        if (j <= self.num_rows-2) and (self.cells[i][j].has_bottom_wall == False) and (self.cells[i][j+1].visited == False):
            self.cells[i][j].draw_move(self.cells[i][j+1])
            if self.solve_r(i, j+1) == True:
                return True
            else:
                self.cells[i][j].draw_move(self.cells[i][j+1], True)

        #try going up:
        if (j > 0) and (self.cells[i][j].has_top_wall == False) and (self.cells[i][j-1].visited == False):
            self.cells[i][j].draw_move(self.cells[i][j-1])
            if self.solve_r(i, j-1) == True:
                return True
            else:
                self.cells[i][j].draw_move(self.cells[i][j-1], True)
        
        #try going left:
        if (i > 0) and (self.cells[i][j].has_left_wall == False) and (self.cells[i-1][j].visited == False):
            self.cells[i][j].draw_move(self.cells[i-1][j])
            if self.solve_r(i-1, j) == True:
                return True
            else:
                self.cells[i][j].draw_move(self.cells[i-1][j], True)
            
        return False
