from math import sqrt
from random import randint

from burbuja import Burbuja, BURBUJA_PROBABILIDAD
from escudo import Escudo
from marcador import Marcador
from submarino import Submarino, SUBMARINO_DISTANCIA_PASO
from torpedo import Torpedo


def colision(objeto1, objeto2):
    distancia = sqrt((objeto2.x - objeto1.x) ** 2 + (objeto2.y - objeto1.y) ** 2)
    return distancia < objeto1.radio + objeto2.radio


class Cazaburbujas:
    def __init__(self, ventana, canvas, nivel):
        self.pausa = False
        self.ventana = ventana
        self.canvas = canvas
        self.nivel = nivel
        self.marcador = Marcador(canvas, nivel)
        self.submarino = Submarino(canvas)
        self.burbujas = list()
        self.partida_activa = True
        self.num_burbujas = 0
        self.torpedo = Torpedo(canvas, nivel)
        self.escudo = Escudo(canvas, nivel)

    def crear_burbuja(self):
        nueva_burbuja = Burbuja(self.canvas, self.num_burbujas, self.nivel)
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
        if self.marcador.has_perdido() and evento.keysym == 'space':
            self.borrar_pantalla()
            return True
        if self.marcador.has_perdido():
            return
        if evento.keysym == 'F1':
            self.borrar_pantalla()
            return True
        elif evento.keysym == 'F9' and self.pausa:
            self.reanudar()
        elif evento.keysym == 'F9':
            self.pausar()
        elif evento.keysym == 'Up':
            self.submarino.mover_en_canvas(0, -SUBMARINO_DISTANCIA_PASO)
        elif evento.keysym == 'Down':
            self.submarino.mover_en_canvas(0, SUBMARINO_DISTANCIA_PASO)
        elif evento.keysym == 'Left':
            self.submarino.mover_en_canvas(-SUBMARINO_DISTANCIA_PASO, 0)
        elif evento.keysym == 'Right':
            self.submarino.mover_en_canvas(SUBMARINO_DISTANCIA_PASO, 0)

    def siguiente_paso(self):
        self.marcador.actualizar()
        if self.marcador.has_perdido() or self.pausa:
            return
        if randint(1, BURBUJA_PROBABILIDAD) == 1:
            self.crear_burbuja()
        self.mover_burbujas()
        self.limpiar_burbujas()
        colisiones = self.detectar_colisiones()
        self.marcador.puntos += colisiones
        self.marcador.tiempo_fin += 5 * colisiones
        num_escudos = self.detectar_escudo_activo()
        self.marcador.escudos += num_escudos
        self.torpedo.mover()
        impacto_detectado = self.detectar_impacto_con_torpedo()
        self.escudo.mover()

        if impacto_detectado:
            print("Submarino tocado")
            self.torpedo.detonar()
            self.marcador.escudos -= 2

        if self.marcador.escudos < 0:
            self.marcador.registrar_impacto_con_torpedo()

    def detectar_escudo_activo(self):
        num_escudos = 0
        if self.escudo.activo and colision(self.submarino, self.escudo):
            self.escudo.activar()
            print("Escudo activado")
            num_escudos += 1
        return num_escudos

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

    def reiniciar_partida(self):
        self.partida_activa = False
        self.borrar_pantalla()

    def borrar_pantalla(self):
        for burbuja in self.burbujas:
            burbuja.desactivar()
        self.escudo.desactivar()
        self.marcador.borrar_pantalla()
        self.submarino.borrar()
        self.torpedo.desactivar()
        self.ventana.update()

    def pausar(self):
        for burbuja in self.burbujas:
            burbuja.pausar()
        self.torpedo.pausar()
        self.escudo.pausar()
        self.submarino.pausar()
        self.marcador.pausar()
        self.pausa = True

    def reanudar(self):
        for burbuja in self.burbujas:
            burbuja.reanudar()
        self.torpedo.reanudar()
        self.escudo.reanudar()
        self.submarino.reanudar()
        self.marcador.reanudar()
        self.pausa = False

