from tkinter import *

root = Tk()

height = 5
width = 5
for i in range(height): #Rows
       for j in range(width): #Columns
           b = Entry(root, text="hola")
           b.grid(row=i, column=j,Text= "j")

mainloop()