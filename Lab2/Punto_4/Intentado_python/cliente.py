import ntplib
from time import sleep
import threading
import pdb
from datetime import datetime
from tkinter import *
host2= 'ar.pool.ntp.org'
host = 'jp.pool.ntp.org'
import sys
from tkinter import *
import time

ojiva=1
from threading import Thread

def main():
    c = ntplib.NTPClient()
    #r4.set(host2)
    cont=0
    menor_rtt=0
    prom_ret=0
    #retardos=[]
    while cont <3:
        hora_mia1= datetime.now()
        response = c.request(host2, version=3)
        hora_mia2= datetime.now()
        #Obtengo hora del server en datetime.datetime

        #Obtengo hora del server en float (microsegundos)
        #hora_server= response.tx_time
        hora_server= datetime.utcfromtimestamp(response.tx_time)
        #Mi tiempo de viaje Tviaje
        rtt= (hora_mia2 - hora_mia1)/2
        #rtt en dateTime.timeDelta 
        print(type(rtt))
        # Hora a la que tengo que ajustar en dateTime
        hora_server_rtt=  hora_server + rtt
        print(type(hora_server_rtt))
        #Promedio de horas
        #prom_ret += to_integer(hora_server_rtt)
        
        if  menor_rtt == 0 :
            menor_rtt = hora_server_rtt
        else: 
            if hora_server_rtt < menor_rtt:
                menor_rtt = hora_server_rtt
        
        
        cont= cont+1
    #prom_ret= prom_ret/cont
    print('promedio',prom_ret)
    return menor_rtt
    #return prom_ret
    #return hora_server_rtt


def calcular_ojiva(hora_server,hora_mia):
    resta= hora_mia - hora_server
    print('hora mira y hora server', hora_mia, hora_server) 
    print ('resta!_',hora_mia - hora_server)
    neutro= '5/11/20 00:00:00'
    neutrod= datetime.strptime(neutro, '%d/%m/%y %H:%M:%S')

    if hora_server > hora_mia:
        ojiva = 0.001
    elif hora_server < hora_mia:
        ojiva = 2
    else:
        ojiva= 0.001
    print('nueva ojiva',ojiva)
    return ojiva 

def to_integer(dt_time):
    return 10000*dt_time.year + 100*dt_time.month + dt_time.day
'''
def times(reloj):
    
    #sleep(1)
    mi_hora = int(round(time.time()))
    print('mi hora: ',mi_hora)
    current_time = time.strftime("%H:%M:%S")
    print('current_time',current_time)
    #c2= datetime.now()
    #while True:
    val=main()
    #val = int(round(val))
    print('la que viene ', val)
    ojivanew= calcular_ojiva(val, mi_hora) 
    sleep(ojivanew)
    mi_hora+= 1
    reloj.config(text= mi_hora,bg="black",fg="green", font= "Arial 50 bold")
    print(time.strftime(mi_hora,"%H:%M:%S"))


def crearVentana():
    #Ventana
    root= Tk()
    root.geometry("485x250")
    root.title("Reloj digital")
    #Espacio para hora
    reloj = Label(root,font = ("times", 50,"bold"))
    mi_boton = Button(text= "mi boton")
    mi_boton.pack()
    reloj.grid(row=2, column=1, pady=25,padx=100)
    times(reloj)
        
    root.mainloop()
crearVentana()
'''