from line import *
from point import *

class Cell:
    def __init__(self, p1, p2, win, left_wall=False, right_wall=False, top_wall=False, bottom_wall=False):
        self.p1 = p1
        self.x1 = p1.x
        self.y1 = p1.y

        self.p2 = p2
        self.x2 = p2.x
        self.y2 = p2.y

        self.win = win

        self.has_left_wall = left_wall
        self.has_right_wall = right_wall
        self.has_top_wall = top_wall
        self.has_bottom_wall = bottom_wall

    def draw(self):
        top = Line(self.p1, Point(self.x2, self.y1))
        bottom = Line(Point(self.x1, self.y2),self.p2)
        left = Line(self.p1, Point(self.x1, self.y2))
        right = Line(Point(self.x2, self.y1),self.p2)

        if self.has_left_wall == True:
            top.draw(self.win.canvas,"red")