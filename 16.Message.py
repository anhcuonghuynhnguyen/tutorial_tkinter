'''anchor: This option is used to decide the exact position of the text within the space .Its default value is CENTER.
bg: This option used to represent the normal background color.
bitmap: This option used to display a monochrome image.
bd: This option used to represent the size of the border and the default value is 2 pixels.
cursor: By using this option, the mouse cursor will change to that pattern when it is over type.
font: This option used to represent the font used for the text.
fg: This option used to represent the color used to render the text.
height: This option used to represent the number of lines of text on the message.
image: This option used to display a graphic image on the widget.
justify: This option used to control how the text is justified: CENTER, LEFT, or RIGHT.
padx: This option used to represent how much space to leave to the left and right of the widget and text. It’s default value is 1 pixel.
pady: This option used to represent how much space to leave above and below the widget. It’s default value is 1 pixel.
relief: The type of the border of the widget. It’s default value is set to FLAT.
text: This option used use newlines (“\n”) to display multiple lines of text.
variable: This option used to represents the associated variable that tracks the state of the widget.
width: This option used to represents the width of the widget. and also represented in the number of characters that are represented in the form of texts.
wraplength: This option will be broken text into the number of pieces.'''
from tkinter import *

root = Tk()
root.geometry("300x200")

w = Label(root, text ='GeeksForGeeks', font = "50")
w.pack()
	
msg = Message( root, text = "A computer science portal for geeks hahahaha muhahaha")
	
msg.pack()

root.mainloop()

#like label but more than one line 
