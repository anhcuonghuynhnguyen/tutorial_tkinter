from tkinter import *
from tkinter.ttk import *
#create main window
main = Tk() 
main.title('text')
main.geometry('500x500')
#create style for button
style = Style()
style.configure('W1.TButton', font = ('Comic Sans MS', 20, 'bold'), foreground = 'blue')
style.map('W1.TButton', foreground= [('active', 'green')])
#path of image 
photo = PhotoImage(file= r'D:\Python\app\Python.PNG')
#edit image
photo = photo.subsample(5,5)
#create button
but = Button(main, text = 'Đẹp trai',style= 'W1.TButton',
                                                         image= photo, 
                                                         compound=LEFT, 
                                                         command= main.destroy)
but.pack(fill= BOTH, side= BOTTOM) 

main.mainloop()
