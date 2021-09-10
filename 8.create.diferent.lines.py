from tkinter import *
from tkinter.ttk import *

class CreateLine:
    def __init__(self, master):
        self.main = master
        #calls create() method of class CreateLine
        self.create()
    
    def create(self):
        #this í create a object of class
        self.canvas = Canvas(self.main, background='light blue')
        # This creates a line of length 200 (straight horizontal line)
        self.canvas.create_line(15, 25, 200, 25)
 
        # This creates a lines of 300 (straight vertical dashed line)
        self.canvas.create_line(300, 35, 300, 200, dash = (5, 2))
         
        # This creates a triangle (triangle can be created by other methods also)
        self.canvas.create_line(55, 85, 155, 85, 105, 180, 55, 85)
         
        # This pack the canvas to the main window and make it expandable
        self.canvas.pack(fill = BOTH, expand = True)

        
if __name__ == '__main__' :
    #object of class Tk, responsible for creating
    #a tkinter toplevel window
    master = Tk()
    lines = CreateLine(master)
    #this sets the title to lines
    master.title('Lines')
    master.geometry('400x300')
    style = Style()
    style.configure('TButton', font = ('Time New Roman', 10, 'bold'))
    style.map('TButton', 
                    foreground = [('pressed', 'red'), ('active','green')],
                    background = [('pressed', 'blue'), ('active', 'yellow')])
    but = Button(master, text =' Quit', command = master.destroy).pack(side = BOTTOM)

    master.mainloop()
