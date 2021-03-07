from time import time


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
        if tiempo_restante < 0:
            self.canvas.itemconfig(self.texto_puntos, text="HAS PERDIDO")
            return
        self.canvas.itemconfig(self.texto_tiempo, text=str(int(tiempo_restante)))
        self.canvas.itemconfig(self.texto_puntos, text=str(self.puntos))

    def tiempo_agotado(self):
        return time() > self.tiempo_fin
