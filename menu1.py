from tkinter import *

class Menu1():
    def __init__(self, canvas, master, x, y, width, height, data):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.canvas = canvas
        self.canvas.create_rectangle(x, y, width, height, fill='gray', width=5)
        self.data = data
        self.main_draw()
    
    def main_draw(self):
        #self.menu = Grid()
        """ Label(self.canvas, text='1').grid(row=1, column=1).place(x=self.x, y=self.y)
        Label(self.canvas, text='2').grid(row=2, column=1).place(x=self.x, y=self.y)
        Label(self.canvas, text='3').grid(row=3, column=1).place(x=self.x, y=self.y)
        Label(self.canvas, text='4').grid(row=4, column=1).place(x=self.x, y=self.y)
        Label(self.canvas, text='5').grid(row=5, column=1).place(x=self.x, y=self.y) """
        #self.menu.place(x=self.x, y=self.y, width = self.width, height=self.height)

    def second_draw(self, params):
        Label(self.canvas, text=str(params)).place(x=100, y=100)
