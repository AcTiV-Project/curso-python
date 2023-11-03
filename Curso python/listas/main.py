"""
Listas: colecciones de datos con un unico nombre
"""

peliculas = ['Batman', 'Spiderman', 'jumanji']

print(peliculas) #Imprimiendo todos los datos de la lista


#Indices de las listas

print(peliculas[1]) #Imporimiendo el segundo valor de la lista
print(peliculas[0:1])
peliculas[1] = "Maze Runner" #Cambiando el valor de un array



peliculas.append("Harry poter") #Agregar contenido a una lista


for peliculas in peliculas: #Recorriendo una lista
    print(peliculas)


#Listas multidimensionales

contacto = [
    [
        'Antonio',
        'antonio@gamil.com'
    ],

    [
        'Luis',
        'luis@gmail.com'
    ],

    [
        'jorge',
        'jorge@gmail.com'
    ]
]

print(contacto[0][1]) #imprimiendo el email de la primera lista


#funciones y metodos para listas

personas = ['jorge', 'angie', 'lisa']
numeros = [1, 2,4,5,3]

