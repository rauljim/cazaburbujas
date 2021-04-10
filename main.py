import time
from tkinter import Tk, Canvas

from configuracion import TITULO, CANVAS_ANCHURA, CANVAS_ALTURA, FONDO
from menu import Menu


def iniciar(ventana, canvas):
    menu = Menu(ventana, canvas)
    canvas.bind_all("<Key>", menu.reaccionar_a_tecla_pulsada)
    while menu.activo:
        time.sleep(0.1)
        menu.siguiente_paso()
        ventana.update()


ventana = Tk()
ventana.title(TITULO)
canvas = Canvas(ventana, width=CANVAS_ANCHURA, heigh=CANVAS_ALTURA, bg=FONDO)
canvas.pack()
menu = Menu(ventana, canvas)
ventana.update()
iniciar(ventana, canvas)

