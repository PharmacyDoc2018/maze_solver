from window import *
from point import *
from line import *
from cell import *

def main():
    win = Window(800, 600)

    space = 5 
    length = 50
    height = 50
    initial_space = 10
    
    point_1 = Point(10, 10)
    point_2 = Point(60, 60)
    cell_1 = Cell(point_1, point_2, win, True, True, True, True)
    cell_1.draw()

    point_3 = Point(170, 10)
    point_4 = Point(220, 60)
    cell_2 = Cell(point_3, point_4, win, True, True, True, True)
    cell_2.draw()

    cell_1.draw_move(cell_2, True)

    win.wait_for_close() 

main()
