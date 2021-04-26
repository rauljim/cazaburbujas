from tkinter import font

import configuracion
import torpedo

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
        self.FUENTE_TITULO = font.Font(family='Helvetica', size=36, weight='bold')
        self.FUENTE_NORMAL = font.Font(family='Helvetica', size=20, weight='bold')
        self.ventana = ventana
        self.canvas = canvas
        self.activo = True
        self.objetos_canvas = list()



        self.objetos_canvas.append(
            self.canvas.create_text(configuracion.CENTRO_X, TITULO_Y, text=TEXTO_TITULO, fill="white",
                                    font=self.FUENTE_TITULO))
        self.objetos_canvas.append(
            self.canvas.create_text(configuracion.CENTRO_X, NIVEL_Y, text=TEXTO_NIVEL, fill="white",
                                    font=self.FUENTE_NORMAL))
        self.mostrar_nivel(1)
        self.objetos_canvas.append(
            self.canvas.create_text(configuracion.CENTRO_X, INICIAR_Y, text=TEXTO_INICIAR, fill="white",
                                    font=self.FUENTE_NORMAL))

        f = open("record.txt", "r")
        linea = f.readline()
        try:
            maxima_puntuacion = int(linea)
        except IOError:
            maxima_puntuacion = 0
        texto_record = f"Record: {maxima_puntuacion}"
        self.objetos_canvas.append(
            self.canvas.create_text(configuracion.CENTRO_X, RECORD_Y, text=texto_record, fill="white",
                                    font=self.FUENTE_NORMAL))

    def seleccionar_nivel(self, nivel):
        pass

    def borrar_pantalla(self):
        for objeto_canvas in self.objetos_canvas:
            self.canvas.delete(objeto_canvas)
        self.ventana.update()

    def reaccionar_a_tecla_pulsada(self, evento):
        if evento.keysym == 'Escape':
            self.activo = False
            return
        if evento.keysym == 'space':
            self.borrar_pantalla()
            return True
        if evento.keysym == '1':
            self.seleccionar_nivel(1)
            return True
        if evento.keysym == '2':
            self.seleccionar_nivel(2)
            return True

    def mostrar_nivel(self, nivel):
        self.objetos_canvas.append(
            self.canvas.create_text(configuracion.CENTRO_X + 150, NIVEL_Y, text="1", fill="white",
                                    font=self.FUENTE_NORMAL))
        self.objetos_canvas.append(
            self.canvas.create_text(configuracion.CENTRO_X + 180, NIVEL_Y, text="2", fill="white",
                                    font=self.FUENTE_NORMAL))
        self.objetos_canvas.append(
            self.canvas.create_text(configuracion.CENTRO_X + 210, NIVEL_Y, text="3", fill="white",
                                    font=self.FUENTE_NORMAL))
