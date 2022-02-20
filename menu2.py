from tkinter import Canvas

class Menu2():
    def __init__(self, canvas, master, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.canvas = canvas
        self.canvas.create_rectangle(x, y, width, height, fill='gray', width=5)
        self.main_draw()
    
    def main_draw(self):
        pass