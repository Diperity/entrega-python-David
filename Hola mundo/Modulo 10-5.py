class Perro:
    def hablar(self):
        print("Guau!")

class Gato:
    def hablar(self):
        print("Miau!")

def hacer_hablar(animal):
    animal.hablar()

hacer_hablar(Perro())  # Guau!
hacer_hablar(Gato())   # Miau!
