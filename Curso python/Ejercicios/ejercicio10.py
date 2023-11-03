"""
pedir la nota de 15 alumno y debe decir
cuantos han aprobado y reprobado
"""

contador = 0
aprobados = 0
suspendidos = 0

numero_alumno = int(input("Cuantos alumnos tienes: "))

while contador <= numero_alumno:

    nota = int(input(f"que nota vas a colocar al \" alumno{contador}\ ?"))

    if nota >=5:
        aprobados +=1
    else:
        suspendidos +=1

    contador += 1

    print(f"Alumnos aprobados: {aprobados}")
    print(f"Alumnos suspendidos: {suspendidos}")