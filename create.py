from tkinter import *

class Create():
    def __init__(self, canvas, root, x, y, height):
        self.x = x
        self.x1 = self.x + height
        self.y = y
        self.y1 = self.y + height
        self.centre = (self.x1-self.x / 2,  self.y1-self.y / 2)

        self.count = 1
        self.height = height

        self.root = root
        self.canvas = canvas

        self.canvas.create_rectangle(x, y, x+height, y+height, fill='white', width=5)
        self.main_draw()

            
    
    def main_draw(self):
        pass
                        
    def MousePress(self, event):
        print('create')
    
    def backspace(self, event):
        print('back1')

    def square(self, points):
        self.canvas.create_rectangle(*points, width=5)
    
    def triangle(self, points):
        self.canvas.create_line(*points, width=5)

    def clear(self):
        self.canvas.create_rectangle(self.x, self.y, self.x1, self.y1, fill='white', width=5)