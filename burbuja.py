from random import randint

from configuracion import CANVAS_ANCHURA, CANVAS_ALTURA

MIN_BURBUJA_RADIO = 10
MAX_BURBUJA_RADIO = 30
MAX_BURBUJA_VELOCIDAD = 30
BURBUJA_COLOR = 'white'
BURBUJA_PROBABILIDAD = 20
MARGEN = MAX_BURBUJA_RADIO
BURBUJA_X_INICIAL = CANVAS_ANCHURA + MARGEN


class Burbuja:
    def __init__(self, canvas, id, nivel):
        print('creando', id)
        self.canvas = canvas
        self.id = id
        self.x = BURBUJA_X_INICIAL
        self.y = randint(0, CANVAS_ALTURA)
        self.radio = randint(MIN_BURBUJA_RADIO, MAX_BURBUJA_RADIO)
        self.circulo = canvas.create_oval(self.x - self.radio, self.y - self.radio,
                                          self.x + self.radio, self.y + self.radio,
                                          outline=BURBUJA_COLOR)
        if nivel == 1:
            velocidad_maxima = MAX_BURBUJA_VELOCIDAD / 2
        elif nivel == 2:
            velocidad_maxima = MAX_BURBUJA_VELOCIDAD
        elif nivel == 3:
            velocidad_maxima = MAX_BURBUJA_VELOCIDAD * 2
        self.velocidad = randint(10, velocidad_maxima)
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


