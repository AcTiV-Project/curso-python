"""
mostrar todos los numero entre dos que diga el usuario
"""

num1 = int(input("Digite un numero: "))
num2 = int(input("Digite otro numero: "))

if num1 < num2:
    for contador in range(num1, num2):
        print(contador)
else:
    print("el numero 1 debe ser mayor al numero 2...")