from tkinter import *
from tkinter.ttk import *
#way to create differnent shapes by class() and create()
class shape :
    def __init__(self, master):
        self.main = master
        #calls create method of class shape
        self.create()

    def create(self):
        #create objiect of class method
        #with the help of this we can  create diferent shapes
        self.canvas = Canvas(self.main)
        #create a circl of diameter 80
        self.canvas.create_oval(10, 10, 80, 80,
                            outline = "black", fill = "white",
                            width = 2)
         
        # Creates an ellipse with horizontal diameter
        # of 210 and vertical diameter of 80
        self.canvas.create_oval(110, 10, 210, 80,
                            outline = "red", fill = "green",
                            width = 2)
         
        # Creates a rectangle of 50x60 (heightxwidth)
        self.canvas.create_rectangle(230, 10, 290, 60,
                                outline = "black", fill = "blue",
                                width = 2)
         
        # Creates an arc of 210 deg
        self.canvas.create_arc(30, 200, 90, 100, start = 0,
                          extent = 210, outline = "green",
                          fill = "red", width = 2)
         
        points = [150, 100, 200, 120, 240, 180,
                  210, 200, 150, 150, 100, 200]
         
        # Creates a polygon
        self.canvas.create_polygon(points, outline = "blue",
                              fill = "orange", width = 2)
        # Pack the canvas to the main window and make it expandable
        self.canvas.pack(fill = BOTH, expand = 1)

        #create button
        but = Button(self.canvas, text= 'Quit', command= self.main.destroy)
        but.pack(side= BOTTOM)

if __name__ == '__main__':
    #object of class Tk, responsible for creating
    #a tkinter toplevel window 
    master = Tk()
    shape = shape(master)
    #set the geometry and position 
    #of window on the screen
    master.geometry("330x220")
    
    master.mainloop()

        
