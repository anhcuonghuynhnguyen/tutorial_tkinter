#listbox = Listbox(root, bg, fg, bd, height, width, font, ..) 
'''Common methods
    yview – allows the widget to be vertically scrollable.
    xview – allows the widget to be horizontally scrollable.
    get() – to get the list items in a given range.
    activate(index) – to select the lines with a specified index.
    size() – return the number of lines present.
    delete(start, last) – delete lines in the specified range.
    nearest(y) – returns the index of the nearest line.
    curseselection() – returns a tuple for all the line numbers that are being selected.'''

from tkinter import *

main =Tk()
main.geometry("300x250")

listbox = Listbox(main, height= 10, width= 15, background= "light blue", activestyle= "dotbox", fg= "green", font= ("Helvetica",10))
label = Label(main, text = "FOOD ITEMS")
scroll = Scrollbar(main)
scroll.pack( side= RIGHT, fill= BOTH)

listbox.config( yscrollcommand= scroll.set)
scroll.config(command= listbox.yview)


listbox.insert(0, "Nachos")
listbox.insert(1, "Sandwich")
listbox.insert(2, "Burger")
listbox.insert(3, "Pizza")
listbox.insert(4, "Burrito")
#delete items from the list by  specifying the index
listbox.delete(2)
  
# pack the widgets
label.pack()
listbox.pack()
  
  
# Display untill User 
# exits themselves.
mainloop()

# insert(<INDEX>,<ELEMENT>)