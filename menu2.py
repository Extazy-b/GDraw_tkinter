from tkinter import *

class Menu2():
    def __init__(self, canvas, master, x, y, width, height):
        self.x = x
        self.y = y
        self.x1 = width
        self.y1 = height
        self.canvas = canvas
        self.root = master

        self.points = []


        self.canvas.create_rectangle(x, y, width, height, fill='gray', width=5)
        self.square_but = Button(self.canvas, text='■', font='Verdana 25')
        self.triangle_but = Button(self.canvas, text='▲', font='Verdana 25')
        self.circle_but = Button(self.canvas, text='⚫', font='Verdana 40')
        self.polyangle_but = Button(self.canvas, text='⬢', font='Verdana 30')

        self.square_but.bind('<Button-1>', self.square_menu)
        self.triangle_but.bind('<Button-1>', self.triangle_menu)
        self.circle_but.bind('<Button-1>', self.circle_menu)
        self.polyangle_but.bind('<Button-1>', self.polyangle_menu)


        self.main_draw()
    
    def main_draw(self):
        delta = (self.x1-self.x) / 6.5
        self.square_but.place(x=self.x + delta * 0.5, y=self.y+10, width=delta, height=delta)
        self.triangle_but.place(x=self.x + delta * 2, y=self.y+10, width=delta, height=delta)
        self.circle_but.place(x=self.x + delta * 3.5, y=self.y+10, width=delta, height=delta)
        self.polyangle_but.place(x=self.x + delta * 5, y=self.y+10, width=delta, height=delta)


    def square_menu(self, event):
        self.points = [self.root.drawing.x+100, self.root.drawing.y+100,
                       self.root.drawing.x1-100, self.root.drawing.y1-100]
        self.root.drawing.clear()
        self.root.drawing.square(self.points)

    
    def triangle_menu(self, event):
        self.points = [self.root.drawing.x+100, self.root.drawing.y1-150,
                       self.root.drawing.x1-100, self.root.drawing.y1-150]
        self.root.drawing.clear()
        self.root.drawing.triangle(self.points)


    def circle_menu(self, event):
        self.root.drawing.clear()
        print('circle')


    def polyangle_menu(self, event):
        self.root.drawing.clear()
        print('polyangle')

        
