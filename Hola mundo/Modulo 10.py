# Definimos la clase
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

# Creamos un objeto
persona1 = Persona("Laura", 25)

print(persona1.nombre)  # Laura
print(persona1.edad)    # 25
