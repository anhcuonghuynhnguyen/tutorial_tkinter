#https://www.geeksforgeeks.org/radiobutton-in-tkinter-python/
#button = Radiobutton(master, text=”Name on Button”, variable = “shared variable”, value = “values of each button”, options = values, …)
#shared variable = A Tkinter variable shared among all Radio buttons 
#value = each radiobutton should have different value otherwise more than 1 radiobutton will get selected.
# Importing Tkinter module
from tkinter import *
from tkinter.ttk import *

# Creating master Tkinter window
master = Tk()
master.geometry("175x175")

# Tkinter string variable
# able to store any string value
v = StringVar(master, "1")
#create style for RadioButton
style = Style()
style.configure('W.TRadiobutton', font = ("arial", 10, "bold"), background = 'light blue', 
                                                      foreground = 'black') 
style.map('W.TRadiobutton', foreground= [('active', 'green')])
#create LabelFrame 
label_frame = LabelFrame(master, text = 'This is Label Frame one')
label_frame.pack(expand = 'yes', fill = 'both')

label_frame1 = LabelFrame(master, text = 'This is Label Frame two')
label_frame1.pack(expand = 'yes', fill = 'both')
# Dictionary to create multiple buttons
values = {"RadioButton 1" : "1",
		"Đẹp trai" : "2",
		"Thông minh" : "3",
		"Nhiều tiền" : "4",
		"Fuck boy" : "5"}

# Loop is used to create multiple Radiobuttons
# rather than creating each button separately
for (text, value) in values.items():
	Radiobutton(label_frame, text = text, variable = v, style= 'W.TRadiobutton',
				value = value).pack(fill=X)
#create button
but1 = Button(label_frame1, text = 'QUIT', command= master.destroy).pack()


# Infinite loop can be terminated by
# keyboard or mouse interrupt
# or by any predefined function (destroy())
mainloop()
