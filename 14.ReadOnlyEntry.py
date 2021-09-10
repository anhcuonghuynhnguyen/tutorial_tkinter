#there are cases when a certain text needs to be in a read-only format to prevent alterations by the user. 
# This can be achieved by the Entry widget and the various options available under the Entry widget.
#https://www.geeksforgeeks.org/tkinter-read-only-entry-widget/
from tkinter import *

root = Tk()

L1 = Label(root, text="User Name")
L1.grid(row=0,column=0)
L2 = Label(root, text="Password")
L2.grid(row=1,column=0)
L3 = Label(root, text= 'Password second')
L3.grid(row=2, column=0)

mystr = StringVar()
mystr.set('username@xyz.com')
passstr = StringVar()
passstr.set('12345678')

entry = Entry(textvariable=mystr,
			state=DISABLED).grid(row=0,
								column=1,
								padx=10,
								pady=10)

passwd = Entry().grid(row=1,column=1,
					padx=10,pady=10)
passwd2 = Entry(textvariable= passstr,
                    state='readonly').grid(row=2,column=1,
					padx=10,pady=10)
mainloop()


