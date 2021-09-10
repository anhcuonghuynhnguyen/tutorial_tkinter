from tkinter import *
from tkinter.ttk import *

root = Tk()
root.geometry("300x200")

w = Label(root, text ='GeeksForGeeks', font = "50")
w.pack()

#create style of Button by ttk.style
style = Style()
style.configure("TButton" , font = ('Time New Roman',10,'underline'))
style.map("TButton",
    foreground=[('pressed', 'red'), ('active', 'blue')],
    background=[('pressed', '!disabled', 'green'), ('active', 'red')])

style.configure("TCheckbutton" , font = ('Time New Roman',10,'bold'))
style.map("TCheckbutton",
    foreground=[('pressed', 'red'), ('active', 'blue')],
    background=[('pressed', '!disabled', 'light yellow'), ('active', 'light green')])

#creat button
colored_btn = Button(root, text="Heloo").pack()
but1 = Button(root, text = "Quit", command = root.destroy).pack(side=BOTTOM)

#create default of Checkbutton
Checkbutton1 = BooleanVar(root, 1)
Checkbutton2 = IntVar(root, 1)
Checkbutton3 = IntVar(root, 0)
#create Checkbutton
Button1 = Checkbutton(root, text = "Tutorial",
					variable = Checkbutton1)
Button2 = Checkbutton(root, text = "Student",
					variable = Checkbutton2)
Button3 = Checkbutton(root, text = "Courses",
					variable = Checkbutton3)
	
Button1.pack()
Button2.pack()
Button3.pack()

mainloop()
