from random import randint

from configuracion import CANVAS_ANCHURA, CANVAS_ALTURA

TORPEDO_RADIO = 10
MAX_TORPEDO_VELOCIDAD = 26
TORPEDO_COLOR = 'red'
TORPEDO_PROBABILIDAD = 10
MARGEN = TORPEDO_RADIO
TORPEDO_X_INICIAL = CANVAS_ANCHURA + MARGEN


class Torpedo:
    def __init__(self, canvas, nivel):
        print('creando torpedo')
        self.canvas = canvas
        self.x = TORPEDO_X_INICIAL
        self.y = randint(0, CANVAS_ALTURA)
        self.radio = TORPEDO_RADIO
        self.circulo = canvas.create_oval(self.x - self.radio, self.y - self.radio,
                                          self.x + self.radio, self.y + self.radio,
                                          fill=TORPEDO_COLOR)
        if nivel == 1:
            velocidad_maxima = MAX_TORPEDO_VELOCIDAD / 2
            self.escudo_probabilidad = TORPEDO_PROBABILIDAD * 3
            self.velocidad = randint(7, velocidad_maxima)
        elif nivel == 2:
            velocidad_maxima = MAX_TORPEDO_VELOCIDAD
            self.escudo_probabilidad = TORPEDO_PROBABILIDAD * 2
            self.velocidad = randint(20, velocidad_maxima)
        elif nivel == 3:
            velocidad_maxima = MAX_TORPEDO_VELOCIDAD * 2
            self.velocidad = randint(35, velocidad_maxima)
        self.activo = True
        self.pausa = False

    def pausar(self):
        self.pausa = True

    def reanudar(self):
        self.pausa = False

    def mover(self):
        if self.pausa:
            return
        if not self.activo:
            if randint(1, TORPEDO_PROBABILIDAD) == 1:
                # Regenarar torpedo
                self.x = TORPEDO_X_INICIAL
                self.y = randint(0, CANVAS_ALTURA)
                self.activo = True
                self.circulo = self.canvas.create_oval(self.x - self.radio, self.y - self.radio,
                                                       self.x + self.radio, self.y + self.radio,
                                                       fill=TORPEDO_COLOR)
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
        self.canvas.delete(self.circulo)

    def detonar(self):
        self.desactivar()
