from tkinter import Tk, Canvas
from random import randint
from time import sleep
from math import sqrt

from burbuja import Burbuja, BURBUJA_PROBABILIDAD
from configuracion import CANVAS_ANCHURA, CANVAS_ALTURA, TITULO, FONDO
from marcador import Marcador
from submarino import Submarino, SUBMARINO_DISTANCIA_PASO
from torpedo import Torpedo
from escudo import Escudo


def colision(objeto1, objeto2):
    distancia = sqrt((objeto2.x - objeto1.x) ** 2 + (objeto2.y - objeto1.y) ** 2)
    return distancia < objeto1.radio + objeto2.radio


class Cazaburbujas:
    def __init__(self, canvas):
        self.marcador = Marcador(canvas)
        self.submarino = Submarino(canvas)
        self.burbujas = list()
        self.num_burbujas = 0
        self.torpedo = Torpedo(canvas)
        self.escudo = Escudo(canvas)

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
        if self.marcador.has_perdido():
            return
        if evento.keysym == 'Up':
            self.submarino.mover_en_canvas(0, -SUBMARINO_DISTANCIA_PASO)
        elif evento.keysym == 'Down':
            self.submarino.mover_en_canvas(0, SUBMARINO_DISTANCIA_PASO)
        elif evento.keysym == 'Left':
            self.submarino.mover_en_canvas(-SUBMARINO_DISTANCIA_PASO, 0)
        elif evento.keysym == 'Right':
            self.submarino.mover_en_canvas(SUBMARINO_DISTANCIA_PASO, 0)

    def siguiente_paso(self):
        self.marcador.actualizar()
        if self.marcador.has_perdido():
            return
        if randint(1, BURBUJA_PROBABILIDAD) == 1:
            self.crear_burbuja()
        self.mover_burbujas()
        self.limpiar_burbujas()
        colisiones = self.detectar_colisiones()
        self.marcador.puntos += colisiones
        self.marcador.tiempo_fin += 10 * colisiones
        self.torpedo.mover()
        impacto_detectado = self.detectar_impacto_con_torpedo()
        self.escudo.mover()
        escudo_activado = self.detectar_escudo_activo()
        if impacto_detectado:
            print("Submarino tocado")
            self.torpedo.detonar()
            self.marcador.registrar_impacto_con_torpedo()
            self.escudo.activar()
        
    def detectar_escudo_activo(self):
        num_vidas = 0
        if self.escudo.activo and colision(self.submarino, self.escudo):
            self.escudo.activar()
            
            print("Escudo activado")
            num_vidas += 1
        return num_vidas
            
        
    def detectar_impacto_con_torpedo(self):

        return self.torpedo.activo and colision(self.submarino, self.torpedo)

    def detectar_colisiones(self):
        colisiones = 0
        for burbuja in self.burbujas:
            if burbuja.activa and colision(self.submarino, burbuja):
                burbuja.explotar()

                print("Burbuja explotada")
                colisiones += 1
        return colisiones


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
