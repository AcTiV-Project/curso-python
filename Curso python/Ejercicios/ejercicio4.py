"""
pedir 2 numero basico al usuario y hacer todas las operaciones basica de una calculadora
"""

num1 = int(input("Digita un numero: "))
num2 = int(input("Digita otro numero: "))

suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division = num1 / num2

print(f"El resultado de la suma es: {suma}")
print(f"El resultado de la resta es: {resta}")
print(f"El resultado de la multiplicacion es: {multiplicacion}")
print(f"El resultado de la division es: {division}")