def dividir(a, b):
    if b == 0:
        raise ValueError("No se puede dividir entre cero")
    return a / b

def pedir_entero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número entero.")

try:
    x = pedir_entero("Ingrese el numerador: ")
    y = pedir_entero("Ingrese el denominador: ")
    resultado = dividir(x, y)
except ValueError as ve:
    print("Error:", ve)
except Exception as e:
    print("Ocurrió un error inesperado:", e)
else:
    print("Resultado:", resultado)
finally:
    print("Fin del programa.")
