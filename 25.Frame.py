#A frame is a rectangular region on the screen. A frame can also be used as a foundation class to implement complex widgets. 
# It is used to organize a group of widgets.
'''Options:

    bg: This option used to represent the normal background color displayed behind the label and indicator.
    bd: This option used to represent the size of the border around the indicator and the default value is 2 pixels.
    cursor: By using this option, the mouse cursor will change to that pattern when it is over the frame.
    height: The vertical dimension of the new frame.
    highlightcolor: This option used to represent the color of the focus highlight when the frame has the focus.
    highlightthickness: This option used to represent the color of the focus highlight when the frame does not have focus.
    highlightbackground: This option used to represent the thickness of the focus highlight..
    relief: The type of the border of the frame. It’s default value is set to FLAT.
    width: This option used to represents the width of the frame.'''

from tkinter import *

main= Tk()

fr = Frame(main, background= 'red')
fr.pack()

bottomfr = Frame(main)
bottomfr.pack(side= RIGHT)

Label1 = Label(fr, text= "Tkinter").pack()

b1_button = Button(fr, text ="Geeks1", fg ="red")
b1_button.pack( side = LEFT)
  
b2_button = Button(fr, text ="Geeks2", fg ="brown")
b2_button.pack( side = RIGHT )
  
b3_button = Button(fr, text ="Geeks3", fg ="blue")
b3_button.pack( side = LEFT )
  
b4_button = Button(bottomfr, text ="Geeks4", fg ="green")
b4_button.pack( side = BOTTOM)
  
b5_button = Button(bottomfr, text ="Geeks5", fg ="green")
b5_button.pack( side = BOTTOM)
  
b6_button = Button(bottomfr, text ="Geeks6", fg ="green")
b6_button.pack( side = BOTTOM)
  
mainloop()