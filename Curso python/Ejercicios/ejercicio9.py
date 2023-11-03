"""
hacer un script que pida un numero indefinidamente hasta que se ingrese el numero 111
"""

contador = 1

while contador < 100:
    numero = int(input("Ingresa un numero:  "))

    if numero == 111:
        break
    else:
        print(f"Has introducido el {numero}")