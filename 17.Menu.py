from tkinter import * 
from tkinter.ttk import *
#creatint main window
main = Tk()
main.title("App")

#creating menu
Menubar = Menu(main)

#adding file menu and commands
files = Menu( Menubar, tearoff= 0)
Menubar.add_cascade(label = "File", menu = files)
files.add_command(label = "New File", command = None)
files.add_command(label = "Open...", command = None)
files.add_command(label = "Save", command = None)
files.add_separator()
files.add_command(label = "Exit", command = main.destroy)

# Adding Edit Menu and commands
edit = Menu(Menubar, tearoff = 0)
Menubar.add_cascade(label ='Edit', menu = edit)
edit.add_command(label ='Cut', command = None)
edit.add_command(label ='Copy', command = None)
edit.add_command(label ='Paste', command = None)
edit.add_command(label ='Select All', command = None)
edit.add_separator()
edit.add_command(label ='Find...', command = None)
edit.add_command(label ='Find again', command = None)
  
# Adding Help Menu
help_ = Menu(Menubar, tearoff = 0)
Menubar.add_cascade(label ='Help', menu = help_)
help_.add_command(label ='Tk Help', command = None)
help_.add_command(label ='Demo', command = None)
help_.add_separator()
help_.add_command(label ='About Tk', command = None)

  
# display Menu
main.config(menu = Menubar)
mainloop()

#Lưu ý
# Các bước tạo menu cho app
# Bước 1 tạo của sổ chính
# Bước 2 tạo Menu chính (line 10)
# Bước 3 thêm các Menu phụ và đặt tên cho chúng (line 13,14)
# Bước 4 thêm các tiện ích con cho từng menu phụ (line 15,16,17,19), 
# có thể thêm phân cách giữa các tiện ích bằng add_separator()
# Bước 5 xuất Menu trên cửa sổ bằng lệnh <root>.config(menu = <Menu>)
