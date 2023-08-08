import Punto

class Circulo:
    def __init__(self, centro, radio):
        self.centro = centro
        self.radio = radio

    def calcular_area(self):
        return 3.14159 * self.radio ** 2

    def calcular_perimetro(self):
        return 2 * 3.14159 * self.radio

    def contiene_punto(self, punto):
        distancia_al_centro = ((punto.x - self.centro.x) ** 2 + (punto.y - self.centro.y) ** 2) ** 0.5
        return distancia_al_centro <= self.radio

centro_circulo = Punto(7, 2)
circulo1 = Circulo(centro_circulo, 5)

print(f"Área del círculo: {circulo1.calcular_area()}")
print(f"Perímetro del círculo: {circulo1.calcular_perimetro()}")

punto_interior = Punto(3, 4)
if circulo1.contiene_punto(punto_interior):
    print("El punto está dentro del círculo.")
else:
    print("El punto no está dentro del círculo.")