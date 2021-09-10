# This widget is mixed text and scrollbar
import tkinter as tk
from tkinter import scrolledtext
from tkinter.ttk import *

main = tk.Tk()

lab = tk.Label(main,
                    text= "Hallo",
                    font= ("Time New Roman", 15, "bold"),
                    bg= "light blue",
                    fg= "green")
lab.pack()

text_area = scrolledtext.ScrolledText(main,  width= 40, height= 10,font = ("Times New Roman",15))
but = Button(main, text= "alooo").pack()
text_area.pack()
#text_area.focus()
main,tk.mainloop()