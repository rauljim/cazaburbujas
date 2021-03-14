from random import randint

from configuracion import CANVAS_ANCHURA, CANVAS_ALTURA

ESCUDO_RADIO = 10
MAX_ESCUDO_VELOCIDAD = 10
ESCUDO_COLOR = 'green'
ESCUDO_PROBABILIDAD = 15
MARGEN = ESCUDO_RADIO
ESCUDO_Y_INICIAL = CANVAS_ALTURA - MARGEN


class Escudo:
    def __init__(self, canvas):
        print('creando escudo')
        self.canvas = canvas
        self.x = randint(0, CANVAS_ALTURA)
        self.y = ESCUDO_Y_INICIAL
        self.radio = ESCUDO_RADIO
        self.circulo = canvas.create_oval(self.x - self.radio, self.y - self.radio,
                                          self.x + self.radio, self.y + self.radio,
                                          fill=ESCUDO_COLOR)
        self.velocidad = randint(10, MAX_ESCUDO_VELOCIDAD)
        self.activo = True

    def mover(self):
        if not self.activo:
            if randint(1, ESCUDO_PROBABILIDAD) == 1:
                # Regenarar escudo
                self.x = randint(0, CANVAS_ALTURA)
                self.y = ESCUDO_Y_INICIAL
                self.activo = True
            else:
                return
        self.y -= self.velocidad
        self.canvas.moveto(self.circulo, self.x, self.y)
        if self.y < 0 - ESCUDO_RADIO * 2:
            # El escudo se desactiva cuando se sale completamente de la pantalla
            self.desactivar()

    def desactivar(self):
        print('desactivando escudo')
        self.activo = False

    def activar(self):
        self.desactivar()
