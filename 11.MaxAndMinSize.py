# master.maxsize(height, width) 
# master.minsize(height, width)

from tkinter import  *
from tkinter.ttk import *

root = Tk()

# Fixing the size of the root window
# No one can now expand the size of the root window than the specified one
root. maxsize(300,300)
root.minsize(100,100)


Label(root, text= 'Studio', font = ('Time New Roman', 20, 'underline', 'bold')).pack(side = TOP)

Button(root, text = 'Click Me !', command= root.destroy ).pack(side = TOP)
mainloop()