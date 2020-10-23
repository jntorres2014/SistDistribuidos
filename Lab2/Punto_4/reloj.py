
import time
import tkinter as tk
import datetime
from datetime import date
from random import randrange


class Digital_clock():
    def __init__(self):
        self.mywindow = tk.Tk()
        self.mywindow.geometry("600x380")
        self.mywindow.title("Reloj")
        self.current_time_label = tk.Label(text="", font=('Tahoma', 44), fg='#ffffff', bg='#72a922', pady=5, padx=5)
        self.current_time_label.place(x=175, y=50)
        self.update_clock()
        self.mywindow.mainloop()

    def update_clock(self):
        hola  =randrange(10) 
        now = time.strftime("%H:%M:%S")
        self.current_time_label.configure(text=hola)
        self.mywindow.after(10, self.update_clock)

main=Digital_clock()
'''
import tkinter as tk
import time
import pdb
ROOT = tk.Tk()
ROOT.geometry("350x110")
ROOT.title("Hora actual")
ROOT.configure(bg="Black")
lblReloj = tk.Label(ROOT, text="00:00", fg="white",
                    bg="black", font=("Arial Black", 50))
lblReloj.pack()


def reloj():
    
    global hora
    #pdb.set_trace()
    hora = time.strftime("%I:%M:%S %p").lower()
    lblReloj.config(text=hora)
    lblReloj.after(1, reloj)


reloj()

ROOT.mainloop()
'''