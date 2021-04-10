from time import time
from tkinter import font
import configuracion

TEXTO_REINICIAR = "Pulsa espacio para seguir jugando"

class Marcador:
    def __init__(self, canvas):
        self.canvas = canvas
        self.objetos_canvas = list()
        self.puntos = 0
        self.tiempo_fin = time() + 15
        self.hundido = False
        self.escudos = 0
        self.final_mostrado = False
        self.objetos_canvas.append(canvas.create_text(50, 30, text="TIEMPO", fill="white"))
        self.objetos_canvas.append(canvas.create_text(150, 30, text="PUNTOS", fill="white"))
        self.objetos_canvas.append(canvas.create_text(770, 30, text="ESCUDOS", fill="white"))
        self.texto_tiempo = canvas.create_text(50, 50, fill="white")
        self.texto_puntos = canvas.create_text(150, 50, fill="white")
        self.texto_escudos = canvas.create_text(770, 50, fill="white")
        self.objetos_canvas.extend((self.texto_tiempo, self.texto_puntos, self.texto_escudos))
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
        FUENTE_TITULO = font.Font(family='Helvetica', size=36, weight='bold')
        FUENTE_NORMAL = font.Font(family='Helvetica', size=20, weight='bold')

        if self.final_mostrado:
            return
        self.final_mostrado = True
        texto_puntuacion = f"{self.puntos} puntos "
        self.objetos_canvas.append(
            self.canvas.create_text(configuracion.CENTRO_X, configuracion.CENTRO_Y, text=texto_puntuacion, fill="white",
                                    font=FUENTE_TITULO))
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
        self.objetos_canvas.append(
            self.canvas.create_text(configuracion.CENTRO_X, posicion_y, text=texto_record, fill="white",
                                    font=FUENTE_TITULO))
        self.objetos_canvas.append(self.canvas.create_text(400, 450, text=TEXTO_REINICIAR, fill="white",
                                                           font=FUENTE_NORMAL))

    def has_perdido(self):
        return time() > self.tiempo_fin or self.hundido

    def registrar_impacto_con_torpedo(self):
        self.hundido = True

    def borrar_pantalla(self):
        for objeto_canvas in self.objetos_canvas:
            self.canvas.delete(objeto_canvas)
