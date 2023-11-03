"""
Hacer un programa que muestre los numeros inpares
entre dos numeros que decida el usuario
"""

num1 = int(input("Ingresa el primer numero: "))
num2 = int(input("Ingresa el segundo numero: "))

if num1 < num2:
    for x in range(num1, (num2 + 1)):
        if x%2 == 0:
            print(f"{x} es PAR")
        else:
            print(f"{x} es IMPAR")

else:
    print("El numero 1 debe ser mayor al numero 2...")