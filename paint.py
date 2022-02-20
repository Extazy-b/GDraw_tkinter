from tkinter import *

class Paint():
    def __init__(self, canvas, root, x, y, height):
        self.x = x
        self.x1 = self.x + height
        self.y = y
        self.y1 = self.y + height
        self.height = height
        
        self.points = []
        self.lines = []
        self.data = {}

        self.end = False

        self.result = Button(canvas, text='Result', bg='#bb4050',
                    activebackground='#cc5060', font="Verdana 11")

        self.canvas = canvas
        self.main_draw()

        self.result.bind('<Button-1>', root.results)
    
    def main_draw(self):
        self.canvas.create_rectangle(self.x, self.y, self.x1, self.y1, fill='white', width=5)
        delta = self.height // 35
        for i in range(1, 36):
            self.canvas.create_line(i * delta + self.x, self.y,
                                    i * delta + self.x, self.y1,
                                    width=1)
            self.canvas.create_line(self.x, i * delta + self.y,
                                    self.x1, i * delta + self.y,
                                    width=1)
        self.second_draw()
        self.result.place(x=self.height * .77, y=self.height / .8 * .773, 
                          width=self.height * .204, height=self.height / .8 * .07)
                                    
    def second_draw(self):
        for i in range(len(self.lines) - 1):
            self.canvas.create_line(*self.lines[i], *self.lines[i+1], width=4, fill='blue') 
        for point in self.points:
            self.canvas.create_oval(point[0] - 5, point[1] -5, point[0] + 5, point[1] + 5, fill='red')
    
    def MousePress(self, event, side):
        if side == 'left' and not self.end:
            self.points.append((event.x, event.y))
            self.lines.append((event.x, event.y))
        elif self.points and side == 'right':
            self.lines.append(self.lines[0])
            self.points.append(self.points[0])
            self.end = True
        self.second_draw()
    
    def backspace(self, event):
        if len(self.points) > 0:
            self.points.pop(-1)
            self.lines.pop(-1)
            self.main_draw()
            self.end = False
    
    def delete(self):
        self.points = []
        self.lines = []
        self.flag = False
        self.main_draw()
    
    def get_results(self):
        return {'test': 'Hello'}