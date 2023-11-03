#POO (clases)


class Carro:
    #Atributos o Propiedades (Variables)

    color = "Negro"
    marca = "Kia"
    modelo = "Soluto"
    velocidad = 220

#Metodos, son acciones que realiza el objeto (Carro) (Funciones)

def acelerar(self):
    self.velocidad +=1

def frenar(self):
    self.velocidad -=1


def getvelocidad(self):
    return self.velocidad

#Fin de la clase


#Crear objeto / Instanciar clase

carro = Carro()

print(carro.velocidad)

