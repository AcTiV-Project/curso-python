"""
sacar el porcentaje de un numero que introduzca el usuario
"""

numero = int(input("Ingresa un numero: "))

porcentaje = int(input(f"Ingresa el porcentaje a sacar de {numero}: "))

resultado = (numero * (porcentaje/100))

print(f"el {porcentaje}% de {numero} es: {resultado}")