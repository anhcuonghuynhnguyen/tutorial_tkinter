from tkinter import *
#create main window
main = Tk()
#create canvas
Cplace = Canvas(bg = 'yellow', height= 250, width= 300)
#create line
line = Cplace.create_line(100, 120,
                                        320, 40)
#create arc 
arc = Cplace.create_arc(180, 150, 80,
                   210, start=0,
                   extent=120,
                   fill="red")
#create oval
oval = Cplace.create_oval(80, 30, 140,
                     150,
                     fill="blue")      
#create polygon
polygon = Cplace.create_polygon(100,10,20,10,30,20,40,50, fill='red')    
Cplace.pack()     
main.mainloop()