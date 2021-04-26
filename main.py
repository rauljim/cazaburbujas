import time
from tkinter import Tk, Canvas

from cazaburbujas import Cazaburbujas
from configuracion import TITULO, CANVAS_ANCHURA, CANVAS_ALTURA, FONDO
from menu import Menu
from torpedo import Torpedo


class Main:
    def __init__(self):
        self.ventana = Tk()
        self.ventana.title(TITULO)
        self.canvas = Canvas(self.ventana, width=CANVAS_ANCHURA, heigh=CANVAS_ALTURA, bg=FONDO)
        self.canvas.pack()
        self.menu = None
        self.cazaburbujas = None
        self.salir = False

    def reaccionar_a_tecla_pulsada(self, evento):
        comenzar_juego = False
        ir_a_menu = False
        if evento.keysym == 'Escape':
            self.salir = True
        elif self.menu:
            comenzar_juego = self.menu.reaccionar_a_tecla_pulsada(evento)
        elif self.cazaburbujas:
            ir_a_menu = self.cazaburbujas.reaccionar_a_tecla_pulsada(evento)

        if comenzar_juego:
            nivel = self.menu.nivel_seleccionado
            self.cazaburbujas = Cazaburbujas(self.ventana, self.canvas, nivel)
            self.menu = None
        if ir_a_menu:
            self.cazaburbujas = None
            self.menu = Menu(self.ventana, self.canvas)

    def iniciar(self):
        self.menu = Menu(self.ventana, self.canvas)
        self.canvas.bind_all("<Key>", self.reaccionar_a_tecla_pulsada)
        while not self.salir:
            time.sleep(0.1)
            self.siguiente_paso()
            self.ventana.update()

    def siguiente_paso(self):
        if self.cazaburbujas:
            self.cazaburbujas.siguiente_paso()


if __name__ == "__main__":
    Main().iniciar()
