from tkinter import Tk, BOTH, Canvas

class Window():
    def __init__(self, width, height,):
        self.root = Tk()
        self.root.title = "Maze Solver"
        self.root.winfo_x = width
        self.root.winfo_y = height

        self.canvas = Canvas(self.root)
        self.canvas.pack()

        self.is_running = False

        self.root.protocol("WM_DELETE_WINDOW", self.close)
    
    def redraw(self):
        self.root.update_idletasks()
        self.root.update()

    def wait_for_close(self):
        self.is_running = True
        while self.is_running == True:
            self.redraw()

    def close(self):
        self.is_running = False