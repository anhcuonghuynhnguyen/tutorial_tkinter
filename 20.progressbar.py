# This widget is used for reassure the user that something is happening
# syntax : <var> = Progress(root, orient= HORIZONTAL/ VERTICAL , length = <>, mode = "determinate/indeterminate")

# importing tkinter module
from tkinter import * 
from tkinter.ttk import *

# creating tkinter window
root = Tk()

# Progress bar widget
progress = Progressbar(root, orient = VERTICAL,
			length = 100, mode = 'determinate')
progress1 = Progressbar(root, orient = VERTICAL,
			length = 100, mode = 'indeterminate')

# Function responsible for the updation
# of the progress bar value
def bar():
	import time
	progress['value'] = 20
	root.update_idletasks()
	time.sleep(1)

	progress['value'] = 40
	root.update_idletasks()
	time.sleep(1)

	progress['value'] = 50
	root.update_idletasks()
	time.sleep(1)

	progress['value'] = 60
	root.update_idletasks()
	time.sleep(1)

	progress['value'] = 80
	root.update_idletasks()
	time.sleep(1)
	progress['value'] = 100
def bar1():
	import time
	progress1['value'] = 20
	root.update_idletasks()
	time.sleep(1)

	progress1['value'] = 40
	root.update_idletasks()
	time.sleep(1)

	progress1['value'] = 50
	root.update_idletasks()
	time.sleep(1)

	progress1['value'] = 60
	root.update_idletasks()
	time.sleep(1)

	progress1['value'] = 80
	root.update_idletasks()
	time.sleep(1)
	progress1['value'] = 100

progress.grid(row = 0, column= 0)
progress1.grid(row = 0, column= 1)

# This button will initialize
# the progress bar
Button(root, text = 'Start', command = bar).grid(row= 1, column= 0)
Button(root, text = 'Start', command = bar1).grid(row= 1, column= 1)


# infinite loop
mainloop()
