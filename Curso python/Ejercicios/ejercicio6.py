"""
Mostrar todas las tablas de multiplicar del 1 al 10
mostrando el titulo de la tabla
"""

for cabecera in range(1, 11):
    print("##########################")

    print(f"##### Tabla del {cabecera} #####")

    print("##########################")

    for numero in range(1, 11):
        print(f"{numero} X {cabecera} = {numero * cabecera}")

