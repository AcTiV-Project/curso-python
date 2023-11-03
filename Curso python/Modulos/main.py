"""
Modulos: Son funcionalidades del lenguajes que ya estan hechas y listas para utilizar

Link para ver la documentacion de modulos. https://docs.python.org/3/py-modindex.html
"""

#Importando modulo propio


import mimodulo #Importando mi modulo
from mimodulo import hola #Para importar solo una funcion de mi modulo
from mimodulo import * #Para importar todas las funciones de mi modulo

print(mimodulo.hola("Angie"))

#print(hola("Alejandra"))


#MODULO DE FECHA

import datetime

print(datetime.date.today()) 


#MODULO DE MATEMATICAS

import math

print("Raiz cuadrada de 10. ", math.sqrt(10))
print("Valor pi. ", float(math.pi))
print("Redondear. ", math.floor(8.42510))


#MODULO RANDOM
import random 
print("Numero aleatorio de tipo entero de 10 a 25:  ", random.randint(10, 25) )