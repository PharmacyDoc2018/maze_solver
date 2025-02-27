from window import *
from point import *
from line import *
from cell import *
from maze import *

def main():
    win = Window(800, 600)

    maze = Maze(10, 10, 10, 10, 20, 20, win)
    maze.break_entrance_and_exit_walls()

    win.wait_for_close() 

main()
