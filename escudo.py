from random import randint

from configuracion import CANVAS_ALTURA

ESCUDO_RADIO = 10
MAX_ESCUDO_VELOCIDAD = 18
ESCUDO_COLOR = 'green'
ESCUDO_PROBABILIDAD = 1
MARGEN = ESCUDO_RADIO
ESCUDO_Y_INICIAL = CANVAS_ALTURA - MARGEN


class Escudo:
    def __init__(self, canvas, nivel):
        print('creando escudo')
        self.canvas = canvas
        self.x = randint(0, CANVAS_ALTURA)
        self.y = ESCUDO_Y_INICIAL
        self.radio = ESCUDO_RADIO
        self.circulo = canvas.create_oval(self.x - self.radio, self.y - self.radio,
                                          self.x + self.radio, self.y + self.radio,
                                          fill=ESCUDO_COLOR)
        if nivel == 1:
            velocidad_maxima = MAX_ESCUDO_VELOCIDAD / 2
            self.escudo_probabilidad = ESCUDO_PROBABILIDAD
            self.velocidad = randint(7, velocidad_maxima)
        elif nivel == 2:
            velocidad_maxima = MAX_ESCUDO_VELOCIDAD
            self.escudo_probabilidad = ESCUDO_PROBABILIDAD * 2
            self.velocidad = randint(14, velocidad_maxima)
        elif nivel == 3:
            velocidad_maxima = MAX_ESCUDO_VELOCIDAD * 2
            self.escudo_probabilidad = ESCUDO_PROBABILIDAD * 6
            self.velocidad = randint(25, velocidad_maxima)
        self.activo = True

    def mover(self):
        if not self.activo:
            if randint(1, self.escudo_probabilidad) == 1:
                # Regenarar escudo
                self.x = randint(0, CANVAS_ALTURA)
                self.y = ESCUDO_Y_INICIAL
                self.circulo = self.canvas.create_oval(self.x - self.radio, self.y - self.radio,
                                                       self.x + self.radio, self.y + self.radio,
                                                       fill=ESCUDO_COLOR)
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
        self.canvas.delete(self.circulo)

    def activar(self):
        self.desactivar()
