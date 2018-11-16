from tkinter import *


"""
For building application I am going to use tkinter and SQLite

"""

#creating window
window = Tk()

#creating button
b1 = Button(window,text="Execute")
b1.grid(row=0,column=0)

#creating entry
e1 = Entry(window)
e1.grid(row=0,column=1)

#crearing text widget
t1 = Text(window, height=1, width=20)
t1.grid(row=0, column=2)


window.mainloop()#without this window will be closed by itself
