import os

#Crear carpeta
if not os.path.isdir("./mi_carpeta"):
    os.mkdir("./miCarpeta")
else:
    print("ya existe la carpeta")

"""
Eliminar un archivo
os.rmdir("./miCarpeta")
"""
