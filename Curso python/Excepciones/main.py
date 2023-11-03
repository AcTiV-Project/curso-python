#Captura de errores

try:
    numero = int(input("Ingresa un numero:  "))

    print(f"el numero es {numero}")
except:
    print("No se permiten letras, textos y caracteres especiales.")


#Multiple excepsiones

try:
    numero = int(input("Numero para elevar al cuadrado: "))
    print("el numero es: " + str(numero*numero))

except TypeError:
    print("Debes convertir tus numero a enteros en el codigo")

except ValueError:
    print("Introduce un numero correcto")

except Exception as e:
    print("Ha ocurrido un error: ", type(e).__name__)
