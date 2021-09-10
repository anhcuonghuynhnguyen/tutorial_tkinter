'''Methods used in this widgets are as follows:

    delete(startindex, endindex): This method is used to delete the characters present at the specified range.
    get(startindex, endindex): This method is used to get the characters present in the specified range.
    identify(x, y): This method is used to identify the widget’s element within the specified range.
    index(index): This method is used to get the absolute value of the given index.
    insert(index, string): This method is used to insert the string at the specified index.
    invoke(element): This method is used to invoke the callback associated with the widget.'''

#w = Spinbox ( master, from_= int, to = int,,options)

from tkinter import *

root = Tk()
root.geometry("200x200")

w = Label(root, text= "Hello !!!")
w.pack()

sp = Spinbox(root, from_= 0, to= 10, state= 'readonly')
sp.pack()
root.mainloop()