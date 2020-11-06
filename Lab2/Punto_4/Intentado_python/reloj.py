import sys
from tkinter import *
import time
from cliente import main as update
ojiva=1000
from threading import Thread


def times(reloj):
    current_time = time.strftime("%H:%M:%S")
    reloj.config(text= current_time,bg="black",fg="green", font= "Arial 50 bold")
    retardo = update()
    print('El retardo es= ' ,retardo)
    #ojiva= calcular_ojiva(current_time, retardo)
    reloj.after(ojiva,times,(reloj))
    #cliente.main()


def crearVentana():

    #Ventana
    root= Tk()
    root.geometry("485x250")
    root.title("Reloj digital")

    #Espacio para hora
    reloj = Label(root,font = ("times", 50,"bold"))
    reloj.grid(row=2, column=1, pady=25,padx=100)
    times(reloj)
        
    root.mainloop()
def calcular_ojiva(reloj,retardo):
          
        return 100

#thread.start_new_thread(root.mainlopp)

def main():
    #t2= Thread(target=update)
    t = Thread(target=crearVentana)
    t.start()
    #t2.start()
    print('retardo')

main()
