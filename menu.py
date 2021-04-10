from time import time
from tkinter import font
import configuracion
from cazaburbujas import Cazaburbujas

TEXTO_TITULO = "CAZABURBUJAS"
TEXTO_INICIAR = "Pulsa ESPACIO para jugar o ESC para salir"
TEXTO_NIVEL = "Nivel de dificultad"
TITULO_Y = 100
NIVEL_Y = 200
RECORD_Y = 300
SALIR_Y = 350
INICIAR_Y = 450

class Menu:
    def __init__(self, ventana, canvas):
        self.ventana = ventana
        self.canvas = canvas
        self.activo = True
        self.objetos_canvas = list()
        self.cazaburbujas = None

        FUENTE_TITULO = font.Font(family='Helvetica', size=36, weight='bold')
        FUENTE_NORMAL = font.Font(family='Helvetica', size=20, weight='bold')

        self.objetos_canvas.append(
            self.canvas.create_text(configuracion.CENTRO_X, TITULO_Y, text=TEXTO_TITULO, fill="white",
                                    font=FUENTE_TITULO))
        self.objetos_canvas.append(
            self.canvas.create_text(configuracion.CENTRO_X, NIVEL_Y, text=TEXTO_NIVEL, fill="white",
                                    font=FUENTE_NORMAL))
        self.objetos_canvas.append(
            self.canvas.create_text(configuracion.CENTRO_X, INICIAR_Y, text=TEXTO_INICIAR, fill="white",
                                    font=FUENTE_NORMAL))
        f = open("record.txt", "r")
        linea = f.readline()
        try:
            maxima_puntuacion = int(linea)
        except:
            maxima_puntuacion = 0
        texto_record = f"Record: {maxima_puntuacion}"
        posicion_y = configuracion.CENTRO_Y + 70
        self.objetos_canvas.append(
            self.canvas.create_text(configuracion.CENTRO_X, RECORD_Y, text=texto_record, fill="white",
                                    font=FUENTE_NORMAL))

    def borrar_pantalla(self):
        for objeto_canvas in self.objetos_canvas:
            self.canvas.delete(objeto_canvas)
        self.ventana.update()

    def reaccionar_a_tecla_pulsada(self, evento):
        if evento.keysym == 'Escape':
            self.activo = False
            return
        if self.cazaburbujas:
            self.cazaburbujas.reaccionar_a_tecla_pulsada(evento)
            return
        if evento.keysym == 'space':
            self.borrar_pantalla()
            self.cazaburbujas = Cazaburbujas(self.ventana, self.canvas)
            self.cazaburbujas.reiniciar_partida()

    def siguiente_paso(self):
        if self.cazaburbujas:
            self.cazaburbujas.siguiente_paso()

