from random import randint

from configuracion import CANVAS_ANCHURA, CANVAS_ALTURA

TORPEDO_RADIO = 10
MAX_TORPEDO_VELOCIDAD = 20
TORPEDO_COLOR = 'red'
TORPEDO_PROBABILIDAD = 10
MARGEN = TORPEDO_RADIO
TORPEDO_X_INICIAL = CANVAS_ANCHURA + MARGEN


class Torpedo:
    def __init__(self, canvas):
        print('creando torpedo')
        self.canvas = canvas
        self.x = TORPEDO_X_INICIAL
        self.y = randint(0, CANVAS_ALTURA)
        self.radio = TORPEDO_RADIO
        self.circulo = canvas.create_oval(self.x - self.radio, self.y - self.radio,
                                          self.x + self.radio, self.y + self.radio,
                                          fill=TORPEDO_COLOR)
        self.velocidad = randint(15, MAX_TORPEDO_VELOCIDAD)
        self.activo = True

    def mover(self):
        if not self.activo:
            if randint(1, TORPEDO_PROBABILIDAD) == 1:
                # Regenarar torpedo
                self.x = TORPEDO_X_INICIAL
                self.y = randint(0, CANVAS_ALTURA)
                self.activo = True
            else:
                return
        self.x -= self.velocidad
        self.canvas.moveto(self.circulo, self.x, self.y)
        if self.x < 0 - TORPEDO_RADIO * 2:
            # El torpedo se desactiva cuando se sale completamente de la pantalla
            self.desactivar()

    def desactivar(self):
        print('desactivando torpedo')
        self.activo = False

    def detonar(self):
        self.desactivar()
