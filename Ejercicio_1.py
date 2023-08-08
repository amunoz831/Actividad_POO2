class Vehiculo:
    def __init__(self, velocidad_maxima, kilometraje):
        self.velocidad_maxima = velocidad_maxima
        self.kilometraje = kilometraje

vehiculo1 = Vehiculo(200, 15000)
print(f"Velocidad máxima: {vehiculo1.velocidad_maxima}")
print(f"Kilometraje: {vehiculo1.kilometraje}")