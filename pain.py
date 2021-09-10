from tkinter import *
from typing import Collection


root = Tk()
# Create Title
root.title( "Paint App ")
# specify size
root.geometry("500x500")

# define function when
# mouse double click is enabled
def display(event):
	# Co-ordinates.
	x1, y1, x2, y2 = ( event.x -10),( event.y -10), ( event.x +10),( event.y +10)
	# Colour
	Colour = "#000fff000"
	# specify type of display
	e.create_oval( x1, y1, x2,y2, fill = Colour )
def display1(event):
	# Co-ordinates.
	x1, y1, x2, y2 = ( event.x -10),( event.y -10), ( event.x +10),( event.y +10)
	# Colour
	Colour = "#000fff000"
	# specify type of display
	w.create_oval( x1, y1, x2,y2, fill = Colour )

# create canvas widget.
w = Canvas(root, width = 400, height = 200, bg= 'red')
e = Canvas(root, width= 400, height= 200, bg = 'blue')
# call function when double
# click is enabled.
e.bind( "<B1-Motion>", lambda a: display(a))
w.bind( "<B1-Motion>", lambda a: display1(a))

# create label.
l = Label( root, text = "Double Click and Drag to draw." )
l.pack()
w.pack(side= BOTTOM)
e.pack(side= TOP)

mainloop()

'''Creating an Oval 
 oval = C.create_oval(x0, y0, x1, y1, options)
Creating an arc 
 arc = C.create_arc(20, 50, 190, 240, start=0, extent=110, fill="red")
Creating a Line 
 line = C.create_line(x0, y0, x1, y1, ..., xn, yn, options)
Creating a polygon 
 polygon = C.create_polygon(x0, y0, x1, y1, ...xn, yn, options)
Creating a rectangle
 rectangle = C.create_rectangle(x0, y0, x1, y1, fill= 'color') '''
