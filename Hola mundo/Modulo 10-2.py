class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print(f"{self.nombre} el mahulla ")

gato = Animal("Gato")
gato.hablar()  # Gato hace un sonido
