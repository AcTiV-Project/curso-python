#funciones predefinidas

print(type("hola"))

#comprobar el tipo de variable

nombre = "Jorge"

nombre = isinstance(nombre, float)

if nombre:
    print("la variable es float")
else:
    print("la variable no es float")


if not isinstance(nombre, float):
    print("la variable no es numero con decimales")


print("LIMPIAR ESPACIOS")
s = "        hola       "

print(s.strip())



print("eliminar variables")
year = 2023

print(year)
del year

print("CANTIDAD DE CARACTERES EN UNA VARIABLES")
a = "hola"
print(len(a))


print("ENCONTRAR CARACTERES EN UNA VARIABLE")
d = "la vida es bella"

print(d.find("vida"))




print("REMPLAZAR PALABRAS EN UN STRING")

frase = "A"
nueva_frase = frase.replace("A", "B")
print(nueva_frase)




print("MAYUSCULAS y minusculas")

o = "Jorge"
print(o.lower())
print(o.upper())
