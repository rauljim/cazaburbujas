from time import time
from tkinter import font

import configuracion



class Marcador:
    def __init__(self, canvas):
        self.canvas = canvas
        self.puntos = 0
        self.tiempo_fin = time() + 10
        self.hundido = False
        self.escudos = 0
        self.final_mostrado = False
        canvas.create_text(50, 30, text="TIEMPO", fill="white")
        canvas.create_text(150, 30, text="PUNTOS", fill="white")
        canvas.create_text(770, 30, text="ESCUDOS", fill="white")
        self.texto_tiempo = canvas.create_text(50, 50, fill="white")
        self.texto_puntos = canvas.create_text(150, 50, fill="white")
        self.texto_escudos = canvas.create_text(770, 50, fill="white")
        self.actualizar()

    def actualizar(self):
        if self.has_perdido():
            self.mostrar_has_perdido()
            return
        tiempo_restante = self.tiempo_fin - time()
        self.canvas.itemconfig(self.texto_tiempo, text=str(int(tiempo_restante)))
        self.canvas.itemconfig(self.texto_puntos, text=str(self.puntos))
        self.canvas.itemconfig(self.texto_escudos, text=str(int(self.escudos)))


    def mostrar_has_perdido(self):
        if self.final_mostrado:
            return
        self.final_mostrado = True
        FUENTE_TITULO = font.Font(family='Helvetica', size=36, weight='bold')
        texto_puntuacion = f"{self.puntos} puntos "
        self.canvas.create_text(configuracion.CENTRO_X, configuracion.CENTRO_Y, text=texto_puntuacion, fill="white",
                                font=FUENTE_TITULO)
        f = open("record.txt", "r")
        linea = f.readline()
        try:
            maxima_puntuacion = int(linea)
        except:
            maxima_puntuacion = 0
        if self.puntos > maxima_puntuacion:
            texto_record = "nuevo record"
            f = open("record.txt", "w")
            f.write(str(self.puntos))
        else:
            texto_record = f"record {maxima_puntuacion}"
        posicion_y = configuracion.CENTRO_Y + 70

        self.canvas.create_text(configuracion.CENTRO_X, posicion_y, text=texto_record, fill="white",
                                font=FUENTE_TITULO)


    def has_perdido(self):
        return time() > self.tiempo_fin or self.hundido

    def registrar_impacto_con_torpedo(self):
        self.hundido = True




