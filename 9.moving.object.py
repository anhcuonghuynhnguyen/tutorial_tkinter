#Canvas class of Tkinter supports a functions which is used to move 
# objects from one position to another in any canvas or tkinter toplevel.
#https://www.geeksforgeeks.org/python-tkinter-moving-objects-using-canvas-move-method/
#Member functions used: 
'''movement() 
left() 
right() 
up() 
down()'''
#Tkinter method used: 
'''Canvas.move(canvas_object, x, y)
x is horizontal distance from upper-left corner. 
y is vertical distance from upper-left corner.
pack() 
Canvas.move() 
after() 
bind() '''

from tkinter import *
from tkinter import *

class Moving :
    def __init__(self, master):
        self.master = master
        # to take care movement in x,y direction
        self.x = 1
        self.y = 1
        #create canvas
        self.canvas = Canvas(self.master)
        #create rectangle
        self.rectangle = self.canvas.create_rectangle(
                                                    5, 5, 25, 25, fill = "black")
        self.canvas.pack()
        #calling class's movement method to move the revtanggle 
        self.movement()
    
    def movement(self):
        #this í where move() is called
        self.canvas.move(self.rectangle, self.x, self.y)

        self.canvas.after(100, self.movement,)
    # for motion in negative x direction
    def left(self, event):
        self.x = -10
        self.y = 0
    def right(self, event):
        self.x = 10
        self.y = 0
    def up(self, event):
        self.x = 0
        self.y = -10
    def down(self, event):
        self.x = 0
        self.y = 10

if __name__ == '__main__' :
    # object of class Tk, responsible for creating
    #a tkinter toplevel window
    master = Tk()
    moving = Moving(master)
    master.bind("<KeyPress-Left>", lambda e: moving.left(e))
    master.bind("<KeyPress-Right>", lambda e: moving.right(e))
    master.bind("<KeyPress-Up>", lambda e: moving.up(e) )
    master.bind("<KeyPress-Down>", lambda e: moving.down(e))

    mainloop()
