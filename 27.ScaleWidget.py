#The Scale widget is used whenever we want to select a specific value from a range of values. 
# It provides a sliding bar through which we can select the values by sliding 
# from left to right or top to bottom depending upon the orientation of our sliding bar.
'''Optional parameters

    root – root window.
    bg – background colour
    fg – foreground colour
    bd – border
    orient – orientation(vertical or horizontal)
    from_ – starting value
    to – ending value
    troughcolor – set colour for trough.
    state – decides if the widget will be responsive or unresponsive.
    sliderlength – decides the length of the slider.
    label – to display label in the widget.
    highlightbackground – the colour of the focus when widget is not focused.
    cursor – The cursor on the widget ehich could be arrow, circle, dot etc'''

from tkinter import *

main = Tk()
main.geometry("400x500")

var1 = DoubleVar()
var2 =DoubleVar()

def show1():
    sel = "Horizontal Scale Value =  %s " %str(var1.get())
    l1.config(text = sel, font = ("Courier", 10))
def show2():
    sel = "Vertictal Scale Value =  %s " %str(var2.get())
    l2.config(text = sel, font = ("Courier", 10))


s1 = Scale(main, variable= var1, from_ = 1, to= 100, orient= "horizontal")
s2 = Scale(main, variable= var2, from_ = 1, to= 100, orient= "vertical")

l3 = Label(main, text = "Horizontal Scaler")
  
b1 = Button(main, text ="Display Horizontal", 
            command = show1, 
            bg = "yellow")  
b2 = Button(main, text ="Display Vertical", 
            command = show2, 
            bg = "purple")  


l1 = Label(main)
l2 = Label(main)

s1.pack(anchor= CENTER)
s2.pack(anchor= CENTER)
l3.pack()
b1.pack(anchor= CENTER)
b2.pack(anchor= CENTER)
l1.pack()
l2.pack()

mainloop()