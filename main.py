from window import *
from point import *
from line import *
from cell import *

def main():
   win = Window(800, 600)

   point_1 = Point(0, 0)
   point_2 = Point(400, 300)
   line = Line(point_1, point_2)
   win.draw_line(line,"red")

   point_3 = Point(400, 300)
   point_4 = Point(450, 350)
   cell = Cell(point_3, point_4, win, True, True, True, True)
   cell.draw()

   win.wait_for_close() 

main()
