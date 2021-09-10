# Import all files from
# tkinter and overwrite
# all the tkinter files
# by tkinter.ttk
from tkinter import *
from tkinter.ttk import *

# creates tkinter window or root window
root = Tk()
root.geometry('200x100')

# function to be called when
# keyboard buttons are pressed
def key_press(event):
	key = event.char
	print(key, 'is pressed')

# function to be called when button-1 of mouse is pressed
def pressed1(event):
	print('Tham lam')

# function to be called when button-2 of mouse is pressed
def pressed2(event):
	print('Ngu dốt')

# function to be called when button-3 of mouse is pressed
def pressed3(event):
	print('Còn cái nịt')

## function to be called when button-1 is double clocked
def double_click(event):
	print('Chăm chỉ')

frame1 = Frame(root, height = 100, width = 200)

# these lines are binding mouse
# buttons with the Frame widget
frame1.bind('<Button-1>', pressed1)
frame1.bind('<Button-2>', pressed2)
frame1.bind('<Button-3>', pressed3)
frame1.bind('<Double 1>', double_click)
# here we are binding keyboard
# with the main window
root.bind('<Key>', key_press)
root.bind

frame1.pack()

mainloop()
