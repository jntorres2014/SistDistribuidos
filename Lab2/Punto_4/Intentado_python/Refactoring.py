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

class Reloj ():

    def __init__(self):
        self.ahora=0
        self.hora=0
        self.minutos=0
        self.segundos=0
        self.mili=0
        self.ojiva=0.01


    def calc_ojiva(self,hora_server,hora_mia):
        print('hora mira y hora server', hora_mia, hora_server) 
        print ('resta!_',hora_mia - hora_server)
        if hora_server > hora_mia:
            ojiva = 0.001
        elif hora_server < hora_mia:
            ojiva = 2
        else:
            ojiva= 0.001
        print('nueva ojiva',ojiva)
        return ojiva 

    def obtenerRetardo(self):
        hora_server= main()
        hora_mia= self.ahora
        date_time_obj = datetime.strptime(hora_mia, '%y/%m/%d %H:%M:%S.%f')
        self.ojiva= self.calc_ojiva(hora_server, date_time_obj)
        #self.ojiva=cliente.calcular_ojiva(hora_server, hora_mia)

    def poner_en_hora_server(self):
        c = ntplib.NTPClient()
        response = c.request(host2, version=3)
        now = datetime.utcfromtimestamp(response.tx_time)
        self.ahora= now
        self.ahora= now
        self.hora= now.hour
        self.minutos= now.minute
        self.segundos= now.second
        self.mili=0


    def poner_en_hora(self):
        now= datetime.now()
        print (now)
        self.ahora= now
        self.hora= now.hour
        self.minutos= now.minute
        self.segundos= now.second
        self.mili=0

    def iniciarReloj(self):
        #self.iniciar_ventana()
        cont =0
        while True:
            cont += 1
            sleep(self.ojiva)
            self.mili += 1 
            if (self.mili == 100): 
                self.mili= 0 
                self.segundos += 1 
                if (self.segundos == 60 ): 
                    self.segundos = 0 
                    self.minutos += 1 
                    if (self.minutos == 60 ): 
                        self.minutos= 0 
                        self.hora+= 1 
                        if (self.hora== 24 ): 
                            self.hora=0
            if cont == 1000:
                cont = 0
                self.obtenerRetardo()                
            #print(self.hora,' ',self.minutos,' ',self.segundos,'', self.mili)
            self.ahora = repr(20) + '/' + repr(11) + '/' + repr(8)+' '+ repr(self.hora) +':'+ repr(self.minutos)+':' + repr(self.segundos)+'.' + repr(self.mili)
            #import pdb; pdb.set_trace()
            print(self.ahora)
            #r.set(mostrarHora)
        #self.poner_en_hora()
        #return mostrarHora
    


    def iniciar_ventana(self):
        root = Tk()
        root.config(bd=20)
        #r = StringVar()

        #r = StringVar()

        Label(root, text="Reloj").pack()
        Entry(root, justify="center", textvariable=self.ahora).pack()


        Label(root, text="").pack()  # Separador

        #Button(root, text="Empezar reloj", command=self.iniciarReloj).pack(side="left")

        Button(root, text="Poner en hora", command=self.poner_en_hora).pack(side="left")
        
        Button(root, text="Poner en hora del servidor", command=self.poner_en_hora_server).pack(side="left")
        
        Button(root, text='obtener retardo', command=self.obtenerRetardo).pack(side= "left")


        # Finalmente bucle de la aplicación
        root.mainloop()




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


reloj= Reloj()
hilo1 = threading.Thread(target=reloj.iniciar_ventana)
hilo2 = threading.Thread(target=reloj.iniciarReloj)
hilo2.start()
hilo1.start()
#reloj.iniciar_ventana()
#reloj.iniciarReloj()
