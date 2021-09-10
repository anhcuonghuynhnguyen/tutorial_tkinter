# entry = tk.Entry(parent, option)
'''bg : The normal background color displayed behind the label and indicator. 
    bd : The size of the border around the indicator. Default is 2 pixels. 
    font : The font used for the text. 
    fg : The color used to render the text. 
    justify : If the text contains multiple lines, this option controls how the text is justified: CENTER, LEFT, or RIGHT. 
    relief : With the default value, relief=FLAT. You may set this option to any of the other styles like : SUNKEN, RIGID, RAISED, GROOVE 
    show : Normally, the characters that the user types appear in the entry. To make a .password. entry that echoes each character as an asterisk, set show=”*”. 
    textvariable : In order to be able to retrieve the current text from your entry widget, you must set this option to an instance of the StringVar class.
    state = default is 'normal', different options is 'readonly' and 'disable'
Methods: The various methods provided by the entry widget are: 
    get() : Returns the entry’s current text as a string. 
    delete() : Deletes characters from the widget 
    insert ( index, ‘name’) : Inserts string ‘name’ before the character at the given index. '''

from tkinter import *
from tkinter.ttk import *

root = Tk()
root.maxsize(500,500)
root.minsize(300,300)
# declaring string and integer variable
# for storing name and password
name_var = StringVar()
pass_var = StringVar()

#defining a function that wil get the name and password 
def submit():
    name = name_var.get()
    password = pass_var.get()
    # if name and pass is right
    if name == 'admin' and password == 'admin123':
        print('Welcome')
    else:
        print("User or Password wrong")
    # set name and pass is empty
    name_var.set("")
    pass_var.set("")

name_label = Label(root, text = 'User',font=('calibre',10, 'bold'))
pass_label = Label(root, text = 'Password', font = ('calibre',10,'bold'))
#creating a entry for name and pass
name_entry = Entry(root, textvariable= name_var, font=('calibre',10,'normal'))
pass_entry = Entry(root, textvariable= pass_var, show= '*', font=('calibre',10,'normal'))
#creating a button using the widget, button wil call the submit function
sub_but = Button(root, text = 'Submit', command = submit)

#set postion for widgets
name_label.grid(row= 0, column= 0)
pass_label.grid(row= 1, column= 0)
name_entry.grid(row= 0, column= 1)
pass_entry.grid(row= 1, column= 1)
sub_but.grid(row= 2, column= 1)

root.mainloop()