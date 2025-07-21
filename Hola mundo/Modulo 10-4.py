class Vehiculo:
    def __init__(self, marca):
        self.marca = marca

    def arrancar(self):
        print(f"{self.marca} encendiendo...")

class Moto(Vehiculo):  # Hereda de Vehiculo
    def hacer_caballito(self):
        print(f"{self.marca} realizando derrape")

yamaha = Moto("Yamaha")
yamaha.arrancar()        # Yamaha encendiendo...
yamaha.hacer_caballito() # Yamaha realizando derrape
