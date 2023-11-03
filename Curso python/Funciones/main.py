"""
Conjunto de instrucciones agrupadas bajo un mismo nombre que puede
reutilizarse invocando tantas veces como sea necesario.
"""

#Definiendo una funcion

"""
print("##### EJEMPLO 1 #####")

def muestraNombre():

    print("Jorge")
    print("Anna")
    print("Angie")
    print("Fabiola")
    print("Andrea")
    print("\n")

#Ejecutando la funcion
muestraNombre()


print("##### EJEMPLO 2 #####")

#Ejemplo con parametros

def mostrarNombre(nombre):
    print(f"Tu nombre es: {nombre}")

nombre = input("Cual es tu nombre: ")

mostrarNombre(nombre)



print("##### EJEMPLO 3 #####")

def tabla(numero):
    print(f"Tabla de multiplicar del numero: {numero}")


    for contador in range(11):
        operacion = numero*contador
        print(f"{numero} X {contador} = {operacion}")

    print("\n")

tabla(5)


print("##### EJEMPLO 4 #####")
#parametros opcionales

def getEmpleado(nombre, dni = None):
    print("EMPLEADO")
    print(f"Nombre: {nombre}")

getEmpleado("Jorge Bernuil")



print("##### EJEMPLO 5 #####")
#return o devolver datos

def saludame(nombre):
    saludo = f"hola, saludos {nombre}"

    return saludo

print(saludame("Jorge Bernuil"))



print("##### EJEMPLO 7 #####")
#funciones dentro de otra

def getNombre(nombre):
    texto = f"El Nombre es: {nombre}"
    return texto

def getApellido(apellido):
    texto = f"los apellido son: {apellido}"
    return texto

def devuelveTodo(nombre, apellido):
    texto = getNombre(nombre) + "\n" + getApellido(apellido)
    return texto

print(devuelveTodo("Jorge", "Bernuil"))

"""


print("##### EJEMPLO 8 #####")
#funciones lambda

dime_el_año = lambda year: f"El año es: {year}"

print(dime_el_año(2017))
