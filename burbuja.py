from random import randint

from configuracion import CANVAS_ANCHURA, CANVAS_ALTURA

MIN_BURBUJA_RADIO = 10
MAX_BURBUJA_RADIO = 30
MAX_BURBUJA_VELOCIDAD = 10
BURBUJA_COLOR = 'white'
BURBUJA_PROBABILIDAD = 30
MARGEN = MAX_BURBUJA_RADIO
BURBUJA_X_INICIAL = CANVAS_ANCHURA + MARGEN


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

    def explotar(self):
        self.desactivar()
