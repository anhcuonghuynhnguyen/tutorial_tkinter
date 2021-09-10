#https://www.geeksforgeeks.org/python-tkinter-create-labelframe-and-add-widgets-to-it/
'''LabelFrame can be createed as follows:
        import tkinter
        create main
        creat LabelFrame as child of main'''
#import tkinter
from tkinter import *
from tkinter.ttk import *
#creat main window
main = Tk()
main.title('LabelFrame')
main.geometry('300x250')
#create first labelframe 
label_frame = LabelFrame(main, text = 'This is Label Frame one')
label_frame.pack(expand = 'yes', fill = 'both')

label1 = Label(label_frame, text = 'Please choose:')
label1.grid()

button1 = Button(label_frame, text = 'Helloo!!!').grid(row=1,column= 0)
button2 = Button(label_frame, text = 'Fuck you!!!', command = main.destroy).grid(row= 1, column= 1)

label2 = Label(label_frame, text= ' Heloo continue \n F*** you stop!!!').place(x= 0, y= 45)

#create second labelframe
label_frame2 = LabelFrame(main, text= 'This is Label Frame two')
label_frame2.pack(expand= 'yes', fill= 'both')

label1 = Label(label_frame2, text = 'Please choose:')
label1.place(x = 0, y= 0)
check_button1 = Checkbutton(label_frame2, text= 'Love you').place(x= 0, y= 20)
check_button2 = Checkbutton(label_frame2, text= ' Just Friend').place(x= 0, y= 40)


# This creates an infinite loop which generally
# waits for any interrupt (like keyboard or
# mouse) to terminate
mainloop()



