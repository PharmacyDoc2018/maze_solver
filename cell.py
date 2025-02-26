from line import *
from point import *

class Cell:
    def __init__(self, p1, p2, win, has_left_wall=False, has_right_wall=False, has_top_wall=False, has_bottom_wall=False):
        self.p1 = p1
        self.x1 = p1.x
        self.y1 = p1.y

        self.p2 = p2
        self.x2 = p2.x
        self.y2 = p2.y

        self.win = win

        self.has_left_wall = has_left_wall
        self.has_right_wall = has_right_wall
        self.has_top_wall = has_top_wall
        self.has_bottom_wall = has_bottom_wall

    def draw(self):
        top = Line(self.p1, Point(self.x2, self.y1))
        bottom = Line(Point(self.x1, self.y2),self.p2)
        left = Line(self.p1, Point(self.x1, self.y2))
        right = Line(Point(self.x2, self.y1),self.p2)

        if self.has_left_wall == True:
            left.draw(self.win.canvas,"red")

        if self.has_right_wall == True:
            right.draw(self.win.canvas,"red")

        if self.has_top_wall == True:
            top.draw(self.win.canvas,"red")

        if self.has_bottom_wall == True:
            bottom.draw(self.win.canvas,"red")
