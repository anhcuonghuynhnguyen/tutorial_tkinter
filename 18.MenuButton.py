"""activebackground: This option used to represent the background color when the Menubutton is under the cursor.
activeforeground: This option used to represent the foreground color when the Menubutton is under the cursor.
bg: This option used to represent the normal background color displayed behind the label and indicator.
bitmap: This option used to display a monochrome image on a button.
bd: This option used to represent the size of the border around the indicator and the default value is 2 pixels.
anchor: This option specifies the exact position of the widget content when the widget is assigned more space than needed.
cursor: By using this option, the mouse cursor will change to that pattern when it is over the Menubutton.
disabledforeground: The foreground color used to render the text of a disabled Menubutton. The default is a stippled version of the default foreground color.
direction: It direction can be specified so that menu can be displayed to the specified direction of the button.
fg: This option used to represent the color used to render the text.
height: This option used to represent the number of lines of text on the Menubutton and it’s default value is 1.
highlightcolor: This option used to represent the color of the focus highlight when the Menubutton has the focus.
image: This option used to display a graphic image on the button.
justify: This option used to control how the text is justified: CENTER, LEFT, or RIGHT.
menu: It represents the menu specified with the Menubutton.
padx: This option used to represent how much space to leave to the left and right of the Menubutton and text. It’s default value is 1 pixel.
pady: This option used to represent how much space to leave above and below the Menubutton and text. It’s default value is 1 pixel.
relief: The type of the border of the Menubutton. It’s default value is set to FLAT.
state: It represents the state of the Menubutton. By default, it is set to normal. We can change it to DISABLED to make the Menubutton unresponsive. The state of the Menubutton is ACTIVE when it is under focus.
text: This option used use newlines (“\n”) to display multiple lines of text.
underline: This option used to represent the index of the character in the text which is to be underlined. The indexing starts with zero in the text.
textvariable: This option used to represents the associated variable that tracks the state of the Menubutton.
width: This option used to represents the width of the Menubutton. and also represented in the number of characters that are represented in the form of texts.
wraplength: This option will be broken text into the number of pieces."""
#w = Menubutton ( master, options )

from tkinter import *


main = Tk()
main.geometry('200x200')
halo = Label(main, text= "Hello Con Gà :))))", foreground= 'red')
halo.pack()
#chỗ này hơi rối nhưng tóm lại là tạo ra cái menu con là manubutton1
# của menu chính là menubutton
menubutton = Menubutton(main, text= "Chosse")
menubutton1 = Menu(menubutton, tearoff= 0)
menubutton["menu"] = menubutton1

var1 = IntVar(main, 1)
var2 = IntVar()
var3 = IntVar(main, 1)
var4 = IntVar()
var5 = IntVar(main, 1)
var6 = IntVar()

menubutton1.add_checkbutton(label = "Courses",
                                variable = var1)  
menubutton1.add_checkbutton(label = "Students",
                                variable = var2)
menubutton1.add_separator()
menubutton1.add_checkbutton(label = "Careers",
                                variable = var3)

#tạo ra một cái nữa đẻ dễ so sánh
menubutton_1 = Menubutton(main, text= "Chosse 1")
menubutton_1.menu = Menu(menubutton_1, tearoff= 0)  
menubutton_1["menu"]= menubutton_1.menu  
  
menubutton_1.menu.add_checkbutton(label = "Khóa học",
                                variable = var4)  
menubutton_1.menu.add_checkbutton(label = "Học sinh",
                                variable = var5)
menubutton_1.menu.add_checkbutton(label = "Nghề nghiệp",
                                variable = var6)


menubutton.pack()
menubutton_1.pack()
main.mainloop()