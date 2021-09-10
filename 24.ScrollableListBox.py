#adding scrollbar to listbox

from tkinter import *

main = Tk()

#creating a listbox and attaching it to main window
listbox = Listbox(main, height= 15, width= 10, bg= 'light blue', fg= 'black', font= ('Helvetica', 10), activestyle= "dotbox")
listbox.pack(side= LEFT, fill= BOTH)
#creating a Scrollbar and attaching it to main window
scroll = Scrollbar(main)
scroll.pack(side= RIGHT, fill= BOTH)

for x in range(100):
    listbox.insert(END, x)

#attaching listbox to scrollbar
#since we need to have a vertacal
#scroll we use yscrollcommand

listbox.config(yscrollcommand= scroll.set)
scroll.config( command= listbox.yview)

mainloop()