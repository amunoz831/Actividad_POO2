class CuentaBancaria:
    PORCENTAJE_CUOTA_MANEJO = 0.02

    def __init__(self, numero_cuenta, propietarios, balance):
        self.numero_cuenta = numero_cuenta
        self.propietarios = propietarios
        self.balance = balance
    
    def depositar(self, cantidad):
        if cantidad > 0:
            self.balance += cantidad
            print(f"Se depositaron {cantidad} en la cuenta.")
        else:
            print("La cantidad a depositar debe ser mayor que cero.")
    
    def retirar(self, cantidad):
        if 0 < cantidad <= self.balance:
            self.balance -= cantidad
            print(f"Se retiraron {cantidad} de la cuenta.")
        else:
            print("No hay suficiente saldo para el retiro.")
    
    def aplicar_cuota_manejo(self):
        cuota = self.balance * CuentaBancaria.PORCENTAJE_CUOTA_MANEJO
        self.balance -= cuota
        print(f"Se aplicó una cuota de manejo de {cuota} a la cuenta.")
    
    def mostrar_detalles(self):
        print("Detalles de la cuenta:")
        print(f"Número de cuenta: {self.numero_cuenta}")
        print(f"Propietarios: {', '.join(self.propietarios)}")
        print(f"Balance: {self.balance}")

propietarios_cuenta = ["Camilo Gomez", "Serafina Sanchez"]
cuenta1 = CuentaBancaria("3128027383", propietarios_cuenta, 7520.0)

print(f"Balance inicial: {cuenta1.balance}")
cuenta1.depositar(5372.0)
print(f"Nuevo balance: {cuenta1.balance}")
cuenta1.retirar(738.2)
print(f"Nuevo balance: {cuenta1.balance}")
cuenta1.aplicar_cuota_manejo()
print(f"Nuevo balance después de la cuota: {cuenta1.balance}")
cuenta1.mostrar_detalles()