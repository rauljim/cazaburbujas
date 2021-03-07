from configuracion import CANVAS_ANCHURA, CANVAS_ALTURA, CENTRO_X, CENTRO_Y

SUBMARINO_RADIO = 15
SUBMARINO_COLOR = 'red'
SUBMARINO_DISTANCIA_PASO = 10
SUBMARINO_AJUSTE_TRIANGULO = 5


class Submarino:
    def __init__(self, canvas):
        self.canvas = canvas
        self.triangulo = canvas.create_polygon(5, 5, 5, 25, 30, 15, fill=SUBMARINO_COLOR)
        self.circulo = canvas.create_oval(0, 0, 30, 30, outline=SUBMARINO_COLOR)
        self.x = CENTRO_X
        self.y = CENTRO_Y
        self.radio = SUBMARINO_RADIO
        self.canvas.moveto(self.triangulo, self.x + SUBMARINO_AJUSTE_TRIANGULO, self.y + SUBMARINO_AJUSTE_TRIANGULO)
        self.canvas.moveto(self.circulo, self.x, self.y)

    def mover_en_canvas(self, movimiento_en_x, movimiento_en_y):
        x_modificada = self.x + movimiento_en_x
        y_modificada = self.y + movimiento_en_y
        if 0 <= x_modificada <= CANVAS_ANCHURA - SUBMARINO_RADIO * 2:
            self.x = x_modificada
        if 0 <= y_modificada <= CANVAS_ALTURA - SUBMARINO_RADIO * 2:
            self.y = y_modificada

        self.canvas.moveto(self.triangulo, self.x + SUBMARINO_AJUSTE_TRIANGULO, self.y + SUBMARINO_AJUSTE_TRIANGULO)
        self.canvas.moveto(self.circulo, self.x, self.y)
