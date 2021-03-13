from time import time
from tkinter import font

import configuracion



class Marcador:
    def __init__(self, canvas):
        self.canvas = canvas
        self.puntos = 0
        self.tiempo_fin = time() + 30
        self.hundido = False
        canvas.create_text(50, 30, text="TIEMPO", fill="white")
        canvas.create_text(150, 30, text="PUNTOS", fill="white")
        self.texto_tiempo = canvas.create_text(50, 50, fill="white")
        self.texto_puntos = canvas.create_text(150, 50, fill="white")
        self.actualizar()

    def actualizar(self):
        if self.has_perdido():
            FUENTE_TITULO = font.Font(family='Helvetica', size=36, weight='bold')
            self.canvas.create_text(configuracion.CENTRO_X, configuracion.CENTRO_Y, text="¡HAS PERDIDO!", fill="white",
                                    font=FUENTE_TITULO)
            return
        tiempo_restante = self.tiempo_fin - time()
        self.canvas.itemconfig(self.texto_tiempo, text=str(int(tiempo_restante)))
        self.canvas.itemconfig(self.texto_puntos, text=str(self.puntos))

    def has_perdido(self):
        return time() > self.tiempo_fin or self.hundido

    def registrar_impacto_con_torpedo(self):
        self.hundido = True
