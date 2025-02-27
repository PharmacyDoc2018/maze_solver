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

        self.center = Point((self.x2 + self.x1)/2, (self.y2 + self.y1)/2)

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
        else:
            left.draw(self.win.canvas,"#d9d9d9")

        if self.has_right_wall == True:
            right.draw(self.win.canvas,"red")
        else:
            right.draw(self.win.canvas,"#d9d9d9")

        if self.has_top_wall == True:
            top.draw(self.win.canvas,"red")
        else:
            top.draw(self.win.canvas,"#d9d9d9")

        if self.has_bottom_wall == True:
            bottom.draw(self.win.canvas,"red")
        else:
            bottom.draw(self.win.canvas,"#d9d9d9")

    def draw_move(self, to_cell, undo=False):
        if undo == False:
            fill_color = "red"
        else:
            fill_color = "gray"
        
        move_line = Line(self.center, to_cell.center)
        move_line.draw(self.win.canvas, fill_color)