from tkinter import *

root = Tk()
root.geometry('200x200')
#tạo hàm xử lý nè
def FocusIn(event):
	user.configure(background = 'green')
def FocusOut(event):
	user.configure(background = 'red')
#tạo widget nè
user = Entry(root, width= 30)
user.grid()
user1 = Entry(root, width= 30)
user1.grid()
#tạo phương thức kiểm tra nè
user.bind("<FocusIn>", FocusIn)
user.bind("<FocusOut>", FocusOut)
mainloop()