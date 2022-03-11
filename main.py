from tkinter import *
from screeninfo import get_monitors
from create import Create
from paint import Paint
from menu1 import Menu1
from menu2 import Menu2


class GDraw(Frame):
    def __init__(self, width, height, root=None):
        super().__init__(root)
        self.choice = 1
        self.width= width
        self.height = height
        self.root = root
        self.draw_key_req = False
        
        self.c = Canvas(self.root, width=self.width, height=self.height, bg='white')

        self.draw_size = (0, self.height*.067, self.height*.8)
        self.menu_size = (self.height*.8, self.height*.067, self.width, self.height)

        self.choice_paint = (0, 0, self.width*.5, self.height*.067)
        self.choice_create = (self.width*.5, 0, self.width*.5, self.height*.067)

        self.paint = Button(self.c, text='Paint', font="Verdana 15", bg='#00cc00', activebackground='#00dd00')
        self.create = Button(self.c, text='Create', font="Verdana 15", bg='#777777', activebackground='#00dd00')

        self.draw()
        
        root.bind('<Button-1>', self.LeftMousePress)
        root.bind('<Button-3>', self.RigthMousePress)
        root.bind('<KeyPress>', self.keyboard)
        root.bind('<Control-z>', self.backspace)
        self.paint.bind('<Button-1>', self.mode_paint)
        self.create.bind('<Button-1>', self.mode_create)
        
        

        

    def draw(self):
        self.c.create_rectangle(0, 0, self.width, self.height, fill='white')


        self.c.create_rectangle(*self.choice_paint, width=5)
        self.c.create_rectangle(*self.choice_create, width=5)
        
        
        self.paint.place(x=self.choice_paint[0],y=self.choice_paint[1], 
                width=self.choice_paint[2], height=self.choice_paint[3])

        self.create.place(x=self.choice_create[0], y=self.choice_create[1], 
                width=self.choice_create[2], height=self.choice_create[3])

        if self.choice:
            self.drawing = Paint(self.c, self, *self.draw_size)
            self.menu = Menu1(self.c, self, *self.menu_size, self.drawing.data)

        else:
            self.menu = Menu2(self.c, self, *self.menu_size)
            self.drawing = Create(self.c, self, *self.draw_size)

        self.c.pack()
    
    def LeftMousePress(self, event):
        x, y = event.x, event.y
        
        if ((x in range(round(self.drawing.x), round(self.drawing.x1)))
            * (y in range(round(self.drawing.y), round(self.drawing.y1)))):
                self.drawing.MousePress(event, 'left')
                print(self.drawing.points)

    def RigthMousePress(self, event):
        x, y = event.x, event.y

        if ((x in range(round(self.drawing.x), round(self.drawing.x1)))
            * (y in range(round(self.drawing.y), round(self.drawing.y1)))):
                self.drawing.MousePress(event, 'right')
    
    def keyboard(self, event):
        key = event.keysym
        if key == 'Delete':
            self.drawing.delete()

    def backspace(self, event):
        self.drawing.backspace(event)
    
    def mode_paint(self, event):
        self.choice = 1
        self.paint['bg'] = '#00cc00'
        self.create['bg'] = '#777777'
        self.draw()
    
    def mode_create(self, event):
        self.choice = 0
        self.paint['bg'] = '#777777'
        self.create['bg']  = '#00cc00'
        self.draw()
    
    def results(self, event):
        self.menu.data = self.drawing.get_results()
        self.menu.second_draw(self.menu.data)


info = str(get_monitors())[8:-1].split(', ')
width = int(info[2].split('=')[1])
height = int(info[3].split('=')[1])

window = Tk()

window.geometry(f'{round(width*.6)}x{round(height*.8)}+{round(width*.2)}+{round(height*.1)}')
window.resizable(0, 0)

app = GDraw(width*.6, height*.8, root=window)
app.mainloop()