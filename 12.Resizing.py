#root.resizable(height = None, width = None)
#if user want to change size of window, set integer or True, 
#if user don't want to change, set 0 or False
# importing only those functions
# which are needed
from tkinter import *
from tkinter.ttk import *
# creating tkinter window
root = Tk()
root.title('Resizable')
root.geometry('250x100')

Label(root, text = 'It\'s non-resizable').pack(side = TOP, pady = 10)

# Restricting root window to change
# it's size according to user's need
root.resizable(0, 0)

mainloop()
