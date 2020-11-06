from tkinter import *
from time import sleep
from datetime import datetime
import threading
import cliente
class Reloj ():
   
    def obtenerRetardo(self):
        hora_server= cliente.main()
        hora_mia= self.ahora
        date_time_obj = datetime.strptime(hora_mia, '%y/%m/%d %H:%M:%S.%f')
        self.ojiva=cliente.calcular_ojiva(hora_server, date_time_obj)
        #self.ojiva=cliente.calcular_ojiva(hora_server, hora_mia)


    def __init__(self):
        self.ahora=0
        self.hora=0
        self.minutos=0
        self.segundos=0
        self.mili=0
        self.ojiva=0.01

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
        while True:
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
            #print(self.hora,' ',self.minutos,' ',self.segundos,'', self.mili)
            self.ahora = repr(20) + '/' + repr(11) + '/' + repr(5)+' '+ repr(self.hora) +':'+ repr(self.minutos)+':' + repr(self.segundos)+'.' + repr(self.mili)
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
        
        
        Button(root, text='obtener retardo', command=self.obtenerRetardo).pack(side= "left")


        # Finalmente bucle de la aplicación
        root.mainloop()



reloj= Reloj()
hilo1 = threading.Thread(target=reloj.iniciar_ventana)
hilo2 = threading.Thread(target=reloj.iniciarReloj)
hilo2.start()
hilo1.start()
#reloj.iniciar_ventana()
#reloj.iniciarReloj()
