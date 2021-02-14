from tkinter import Tk, Canvas
from random import randint
from time import sleep, time

ALTURA = 500
ANCHURA = 800
TITULO = "Cazaburbujas"
FONDO = 'darkblue'
BARCO_RADIO = 15
BARCO_COLOR = 'red'
CENTRO_X = ANCHURA / 2
CENTRO_Y = ALTURA / 2
BARCO_DISTANCIA_PASO = 10

MIN_BURBUJA_RADIO = 10
MAX_BURBUJA_RADIO = 30
MAX_BURBUJA_VELOCIDAD = 10
BURBUJA_COLOR = 'white'
BURBUJA_PROBABILIDAD = 60

MARGEN = MAX_BURBUJA_RADIO

BURBUJA_X_INICIAL = ANCHURA + MARGEN

class Barco:
    def __init__(self, canvas):
        self.canvas = canvas
        self.triangulo = canvas.create_polygon(5, 5, 5, 25, 30, 15, fill=BARCO_COLOR)
        self.circulo = canvas.create_oval(0, 0, 30, 30, outline=BURBUJA_COLOR)

    def mover_en_canvas(self, x, y):
        self.canvas.move(self.triangulo, x, y)
        self.canvas.move(self.circulo, x, y)


class Burbuja:
    def __init__(self, canvas, id):
        self.canvas = canvas
        self.id = id
        x = BURBUJA_X_INICIAL
        y = randint(0, ALTURA)
        self.radio = randint(MIN_BURBUJA_RADIO, MAX_BURBUJA_RADIO)
        self.circulo = canvas.create_oval(x - self.radio, y - self.radio, x + self.radio, y + self.radio, outline=BURBUJA_COLOR)
        self.velocidad = randint(1, MAX_BURBUJA_VELOCIDAD)
        self.activa = True

    def mover(self):
        if not self.activa:
            return
        self.canvas.move(self.circulo, -self.velocidad, 0)
        x, y = self.coordenadas()
        if x < 0:
            self.borrar()

    def coordenadas(self):
        pos = self.canvas.coords(self.circulo)
        x_min, x_max, y_min, y_max = pos
        x = (x_min + x_max) / 2
        y = (y_min + y_max) / 2
        return x, y

    def borrar(self):
        print('desactivando', self.id)
        self.activa = False
        self.canvas.delete(self.circulo)

class Cazaburbujas:
    def __init__(self, canvas):
        self.barco = Barco(canvas)
        self.barco.mover_en_canvas(CENTRO_X, CENTRO_Y)
        self.burbujas = list()
        self.num_burbujas = 0

    def crear_burbuja(self):
        nueva_burbuja = Burbuja(canvas, self.num_burbujas)
        self.num_burbujas += 1
        self.burbujas.append(nueva_burbuja)

    def mover_burbujas(self):
        for burbuja in self.burbujas:
            burbuja.mover()

    def limpiar_burbujas(self):
        if len(self.burbujas) and not self.burbujas[0].activa:
            print('borrando', self.burbujas[0].id)
            del self.burbujas[0]

    def evento_callback(self, evento):
        if evento.keysym == 'Up':
            self.barco.mover_en_canvas(0, -BARCO_DISTANCIA_PASO)
        elif evento.keysym == 'Down':
            self.barco.mover_en_canvas(0, BARCO_DISTANCIA_PASO)
        elif evento.keysym == 'Left':
            self.barco.mover_en_canvas(-BARCO_DISTANCIA_PASO, 0)
        elif evento.keysym == 'Right':
            self.barco.mover_en_canvas(BARCO_DISTANCIA_PASO, 0)

    def siguiente_paso(self):
        if randint(1, BURBUJA_PROBABILIDAD) == 1:
            self.crear_burbuja()
        self.mover_burbujas()
        self.limpiar_burbujas()

ventana = Tk()
ventana.title(TITULO)
canvas = Canvas(ventana, width=ANCHURA, heigh=ALTURA, bg=FONDO)
canvas.pack()

cazaburbujas = Cazaburbujas(canvas)
canvas.bind_all("<Key>", cazaburbujas.evento_callback)

while True:
    cazaburbujas.siguiente_paso()
    ventana.update()
    sleep(0.1)
