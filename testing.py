from tkinter import *

root = Tk()
canvas = Canvas(root,height = 300, width = 500)
canvas.pack()
canvas.create_rectangle(50,50,160,160)
root.mainloop()