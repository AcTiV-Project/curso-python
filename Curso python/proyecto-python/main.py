print("""
ACCIONES DISPONIBLES
    -registro
    -login
""")

from usuarios import acciones

hazel = acciones.Acciones()

accion = input("Que deseas hacer?: ")

if accion == "registro":
    hazel.registro()

elif accion == "login":
    hazel.login()
  