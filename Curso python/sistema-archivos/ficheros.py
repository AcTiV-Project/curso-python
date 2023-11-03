from io import open
import pathlib
import shutil #modulo para copiar archivos y renombrarlos
import os


#Abrir un archivo
archivo = open("fichero-texto.txt", "a+")

ruta = str(pathlib.Path().absolute()) + "/fichero-texto.txt"
archivo = open(ruta, "a+")



#ESCRIBIR DENTRO DE UN ARCHIVO
archivo.write("*****Soy un texto desde Python*****\n")




#CERRAR UN ARCHIVO
archivo.close()



#LEER UN ARCHIVO
archivo = open("fichero-texto.txt", "r")
contenido = archivo.read()

print(contenido)


#Copiar archivo

ruta_original = str(pathlib.Path().absolute()) + "/fichero-texto.txt"
ruta_nueva = str(pathlib.Path().absolute()) + "/fichero-copiado.txt"
ruta_alternativa = str(pathlib.Path().absolute()) + "..Paquetes/fichero-copiado.txt"

shutil.copyfile(ruta_original, ruta_nueva)

#Mover
ruta_original = str(pathlib.Path().absolute()) + "/fichero-texto.txt"
ruta_nueva = str(pathlib.Path().absolute()) + "/fichero-copiado-Nuevo.txt"

shutil.move(ruta_original, ruta_nueva)


#Eliminar archivo
ruta_nueva = str(pathlib.Path().absolute()) + "/fichero-copiado-Nuevo.txt"
os.remove(ruta_nueva)



#Comprobar si existe un archivo
import os.path

ruta_comprobar = os.path.abspath("./") + "/fichero-texto1.txt"
print(ruta_comprobar)

if os.path.isfile(ruta_comprobar):
    print("el archivo existe")
else:
    print("No existe el archivo")



