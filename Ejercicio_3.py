class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def mostrar(self):
        print(f"Coordenadas: ({self.x}, {self.y})")

    def mover(self, nuevo_x, nuevo_y):
        self.x = nuevo_x
        self.y = nuevo_y

    def calcular_distancia(self, otro_punto):
        return ((self.x - otro_punto.x)**2 + (self.y - otro_punto.y)**2)**0.5

punto1 = Punto(32, 9)
punto1.mostrar()

punto2 = Punto(7, -11)
punto2.mover(19, -1)
distancia = punto1.calcular_distancia(punto2)
print(f"Distancia entre los puntos: {distancia}")