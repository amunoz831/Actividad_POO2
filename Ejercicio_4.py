import math

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Rectangulo:
    def __init__(self, esquina_sup_izq, esquina_inf_der):
        self.esquina_sup_izq = esquina_sup_izq
        self.esquina_inf_der = esquina_inf_der

    def calcular_perimetro(self):
        base = abs(self.esquina_inf_der.x - self.esquina_sup_izq.x)
        altura = abs(self.esquina_inf_der.y - self.esquina_sup_izq.y)
        return 2 * (base + altura)

    def calcular_area(self):
        base = abs(self.esquina_inf_der.x - self.esquina_sup_izq.x)
        altura = abs(self.esquina_inf_der.y - self.esquina_sup_izq.y)
        return base * altura
    
    def es_cuadrado(self):
        base = abs(self.esquina_inf_der.x - self.esquina_sup_izq.x)
        altura = abs(self.esquina_inf_der.y - self.esquina_sup_izq.y)
        return base == altura

punto_superior_izquierdo = Punto(-3, 7)
punto_inferior_derecho = Punto(4, -4)

rectangulo1 = Rectangulo(punto_superior_izquierdo, punto_inferior_derecho)

print(f"Perímetro del rectángulo: {rectangulo1.calcular_perimetro()}")
print(f"Área del rectángulo: {rectangulo1.calcular_area()}")

if rectangulo1.es_cuadrado():
    print("El rectángulo es un cuadrado.")
else:
    print("El rectángulo no es un cuadrado.")