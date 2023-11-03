#Condicionales

#Operadores de comparacion

"""
== igual
!= diferente de
> mayor que
< menor que
>= mayor o igual
<= menor o igual
"""

print("#####EJEMPLO 1#####")

color = input("Cual es tu color: ")

if color == "Rojo":
    print("El color es rojo")
else:
    print("El color no es rojo")


print("\n#####EJEMPLO 2#####")

#if anidados

nombre = "Jorge"
ciudad = "Panama"
continente = "latinoamerica"
edad = 24
mayoria_edad = 18

if edad >= mayoria_edad:
    print(f"{nombre} es mayor de edad")

    if continente != "latinoamerica":
        print(f"{nombre} no es de latinoamerica")
    else:
        print(f"es de latinoamerica y de {ciudad}")
else:
    print(f"{nombre} No es mayor de edad")


#elif
print("\n#####EJEMPLO 3#####")

dia = int(input("Cual es el dia de la semana: "))

if dia == 1:
    print("es lunes")
elif dia == 2:
    print("es martes")
elif dia == 3:
    print("es miercoles")
elif dia == 4:
    print("es jueves")
elif dia == 5:
    print("es viernes")
else:
    print("es fin de semana...")


print("\n#####EJEMPLO 4#####")

"""
Operadores logicos

and : y
or : o
! : negacion
not : no

"""

edad_minima = 18
edad_maxima = 65
edad_oficial = int(input("cual es tu edad: "))

if edad_oficial >= edad_minima and edad_oficial <= edad_maxima:
    print("estas en edad de trabajar")
else:
    print("No estas en edad de trabajar")


print("\n#####EJEMPLO 5#####")

pais = input("Cual es el pais: ")

if pais == "Panama" or pais == "Colombia" or pais == "Mexico":
    print("Es un pais de habla hispana")
else:
    print("No es un pais de habla hispana")



print("\n#####EJEMPLO 6#####")

pais = "Autralia"

if not (pais == "Panama" or pais == "Colombia" or pais == "Mexico"):
    print(" No es un pais de habla hispana")
else:
    print("Si es un pais de habla hispana")


print("\n#####EJEMPLO 7#####")

pais = "Autralia"

if pais != "Panama" and pais != "Colombia" and pais != "Mexico":
    print(" No es un pais de habla hispana")
else:
    print("Si es un pais de habla hispana")