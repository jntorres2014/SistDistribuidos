import ntplib
from time import sleep
import threading
import pdb
import datetime
from tkinter import *
host2= 'europe.pool.ntp.org'
host = 'pool.ntp.org'


#def tablas(respose):
#arreglo=[]    
def main():
    c = ntplib.NTPClient()
    r4.set(host2)
    response = c.request(host2, version=3)
    r2.set(response.offset)
    r3.set(response.version)
    r.set(datetime.datetime.fromtimestamp(response.tx_time).strftime("%Y %m %d, %H:%M:%-S") )
    Label(root, text="Ofsset").pack()
    Entry(root, justify="center", textvariable=response.offset ).pack() 
    #r2.set('')
    #arreglo.append(r2)
    #print(r3.get())


# Configuración de la raíz
root = Tk()
root.config(bd=20)
r = StringVar()
r2 = StringVar()
r3 = StringVar()
r4 = StringVar()
Label(root, text="Host Hora").pack()
Entry(root, justify="center", textvariable=r4).pack()

Label(root, text="Version").pack()
Entry(root, justify="center", textvariable=r3).pack()

Label(root, text="Hora ").pack()
Entry(root, justify="center", textvariable=r).pack()

Label(root, text="Ofsset").pack()
Entry(root, justify="center", textvariable=r2 ).pack()
#r2.set('')
#arreglo.append(r2)

#print(arreglo)
Button(root, text="Pedir hora", command=main).pack(side="right")
'''
height = 5
width = 5
for i in range(height): #Rows
       for j in range(width): #Columns
           b = Entry(root, text=r2).pack()
           
           #pdb.set_trace()
           #b.pack(row=i, column=j)
           #b.grid(row=i, column=j)


# Finalmente bucle de la aplicación
'''
root.mainloop()
