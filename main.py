from window import *
from point import *
from line import *

def main():
   win = Window(800, 600)
   point_1 = Point(0, 0)
   point_2 = Point(400, 300)
   line = Line(point_1, point_2)
   win.draw_line(line,"red")
   win.wait_for_close() 

main()