#https://www.geeksforgeeks.org/python-tkinter-label/
from tkinter import *
from tkinter.ttk import *
#create main window
main = Tk()
main.title("label")
main.geometry("300x100")
#creae style 
style = Style()
#first style 
style.configure('W.TButton', font = ('Time New Roman',10, 'bold'), foreground = 'blue')
style.map('W.TButton', foreground= [('active', 'green')])
#second style
style.configure('W1.TButton', font = ('Time New Roman',10, 'bold'), foreground = 'blue')
style.map('W1.TButton', foreground= [('active', 'red')])

#create label for entry 
user_name = Label(main, text= "User Name ",
                                          foreground= 'black').place(x= 2,
                                                                                  y= 10)
password = Label(main,text= "Password ",
                                      foreground= 'black').place(x=2,
                                                                                y=30)
#create entry for user name and passwword                                                                              
us_en = Entry(main, width=30).place(x= 70, y= 10)
pass_en = Entry(main, width=30).place(x= 70, y= 30)
#create button based on two style above
enter = Button(main, text= 'Sign in', style= 'W.TButton').place(x=50, y= 55)
escape = Button(main, text= 'Quit', style= 'W1.TButton',
                                     command= main.destroy).place(x=150, y= 55)
                                     
main.mainloop()