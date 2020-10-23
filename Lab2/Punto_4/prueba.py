from tkinter import * 
import time

def sumar():
    r.set( float(n1.get()) + float(n2.get()) )
    borrar()

def resta():
    r.set( float(n1.get()) - float(n2.get()) )
    borrar()

def producto():
    r.set( float(n1.get()) * float(n2.get()) )
    borrar()

def borrar():
    n1.set("")
    n2.set("")

#!/usr/bin/env python
# -*- coding: utf-8 -*-
from  tkinter import *
import time

#FUNCION PARA ACTUALIZAR LA HORA
def times():
    current_time=time.strftime("%H:%M:%S") 
    clock.config(text=current_time,bg="black",fg="green",font="Arial 50 bold")
    clock.after(200,times)
    
	
#VENTANA
root=Tk()
root.geometry("485x250")
root.title("Reloj digital con Tkinter")
clock=Label(root,font=("times",50,"bold"))
clock.grid(row=2,column=1,pady=25,padx=100)
times()

digi=Label(root,text=" Hora Actual",font="times 24 bold",fg="red")
digi.grid(row=0,column=1)

root.mainloop()
n1 = StringVar()
n2 = StringVar()
r = StringVar()

Label(root, text="Número 1").pack()
Entry(root, justify="center", textvariable=n1).pack()

Label(root, text="Número 2").pack()
Entry(root, justify="center", textvariable=n2).pack()

Label(root, text="Resultado").pack()
Entry(root, justify="center", textvariable=r, state="disabled").pack()

Label(root, text="").pack()  # Separador

Button(root, text="Sumar", command=sumar).pack(side="left")
Button(root, text="Resta", command=resta).pack(side="left")
Button(root, text="Producto", command=producto).pack(side="left")

# Finalmente bucle de la aplicación
root.mainloop()
