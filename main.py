from tkinter import Tk, Canvas
from random import randint
from time import sleep, time

CANVAS_ANCHURA = 800
CANVAS_ALTURA = 500
TITULO = "Cazaburbujas"
FONDO = 'darkblue'
SUBMARINO_RADIO = 15
SUBMARINO_COLOR = 'red'
CENTRO_X = CANVAS_ANCHURA / 2
CENTRO_Y = CANVAS_ALTURA / 2
SUBMARINO_DISTANCIA_PASO = 10
SUBMARINO_AJUSTE_TRIANGULO = 5

MIN_BURBUJA_RADIO = 10
MAX_BURBUJA_RADIO = 30
MAX_BURBUJA_VELOCIDAD = 10
BURBUJA_COLOR = 'white'
BURBUJA_PROBABILIDAD = 30

MARGEN = MAX_BURBUJA_RADIO

BURBUJA_X_INICIAL = CANVAS_ANCHURA + MARGEN


class Submarino:
    def __init__(self, canvas):
        self.canvas = canvas
        self.triangulo = canvas.create_polygon(5, 5, 5, 25, 30, 15, fill=SUBMARINO_COLOR)
        self.circulo = canvas.create_oval(0, 0, 30, 30, outline=BURBUJA_COLOR)
        self.x = CENTRO_X
        self.y = CENTRO_Y
        self.canvas.moveto(self.triangulo, self.x + SUBMARINO_AJUSTE_TRIANGULO, self.y + SUBMARINO_AJUSTE_TRIANGULO)
        self.canvas.moveto(self.circulo, self.x, self.y)

    def mover_en_canvas(self, movimiento_en_x, movimiento_en_y):
        x_modificada = self.x + movimiento_en_x
        y_modificada = self.y + movimiento_en_y
        if x_modificada >= 0 and x_modificada <= CANVAS_ANCHURA - SUBMARINO_RADIO * 2:
            self.x = x_modificada
        if y_modificada >= 0 and y_modificada <= CANVAS_ALTURA - SUBMARINO_RADIO * 2:
            self.y = y_modificada

        self.canvas.moveto(self.triangulo, self.x + SUBMARINO_AJUSTE_TRIANGULO, self.y + SUBMARINO_AJUSTE_TRIANGULO)
        self.canvas.moveto(self.circulo, self.x, self.y)


class Burbuja:
    def __init__(self, canvas, id):
        print('creando', id)
        self.canvas = canvas
        self.id = id
        self.x = BURBUJA_X_INICIAL
        self.y = randint(0, CANVAS_ALTURA)
        self.radio = randint(MIN_BURBUJA_RADIO, MAX_BURBUJA_RADIO)
        self.circulo = canvas.create_oval(self.x - self.radio, self.y - self.radio,
                                          self.x + self.radio, self.y + self.radio,
                                          outline=BURBUJA_COLOR)
        self.velocidad = randint(1, MAX_BURBUJA_VELOCIDAD)
        self.activa = True

    def mover(self):
        if not self.activa:
            return
        self.x -= self.velocidad
        self.canvas.moveto(self.circulo, self.x, self.y)
        if self.x < 0 - MAX_BURBUJA_RADIO * 2:
            # Burbujas se desactivan cuando se salen completamente de la pantalla
            self.desactivar()

    def desactivar(self):
        print('desactivando', self.id)
        self.activa = False
        self.canvas.delete(self.circulo)

class Marcador:
    def __init__(self, canvas):
        self.canvas = canvas
        self.puntos = 0
        self.tiempo_fin = time() + 30
        canvas.create_text(50, 30, text="TIEMPO", fill="white")
        canvas.create_text(150, 30, text="PUNTOS", fill="white")
        self.texto_tiempo = canvas.create_text(50, 50, fill="white")
        self.texto_puntos = canvas.create_text(150, 50, fill="white")
        self.actualizar()

    def actualizar(self):
        tiempo_restante = self.tiempo_fin - time()
        self.canvas.itemconfig(self.texto_tiempo, text=str(int(tiempo_restante)))
        self.canvas.itemconfig(self.texto_puntos, text=str(self.puntos))


class Cazaburbujas:
    def __init__(self, canvas):
        self.marcador = Marcador(canvas)
        self.barco = Submarino(canvas)
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

    def reaccionar_a_tecla_pulsada(self, evento):
        if evento.keysym == 'Up':
            self.barco.mover_en_canvas(0, -SUBMARINO_DISTANCIA_PASO)
        elif evento.keysym == 'Down':
            self.barco.mover_en_canvas(0, SUBMARINO_DISTANCIA_PASO)
        elif evento.keysym == 'Left':
            self.barco.mover_en_canvas(-SUBMARINO_DISTANCIA_PASO, 0)
        elif evento.keysym == 'Right':
            self.barco.mover_en_canvas(SUBMARINO_DISTANCIA_PASO, 0)

    def siguiente_paso(self):
        if randint(1, BURBUJA_PROBABILIDAD) == 1:
            self.crear_burbuja()
        self.mover_burbujas()
        self.limpiar_burbujas()
        self.marcador.actualizar()

ventana = Tk()
ventana.title(TITULO)
canvas = Canvas(ventana, width=CANVAS_ANCHURA, heigh=CANVAS_ALTURA, bg=FONDO)
canvas.pack()

cazaburbujas = Cazaburbujas(canvas)
canvas.bind_all("<Key>", cazaburbujas.reaccionar_a_tecla_pulsada)

while True:
    cazaburbujas.siguiente_paso()
    ventana.update()
    sleep(0.1)
