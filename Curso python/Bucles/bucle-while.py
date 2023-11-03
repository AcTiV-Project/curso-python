"""
While: es una estructura de control que repite la ejecucion de una intruccion tantas 
veces como sea necesario hasta que deje de cumplirse la condicion.
"""

contador = 1

while contador <= 100:
    print(f"Estoy en el numero: {contador}")

    contador = contador + 1
