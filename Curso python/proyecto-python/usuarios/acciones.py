import usuarios.usuario as modelo

class Acciones:

    def registro(self):
        print("\nOk, registrate en el sistema: ")

        nombre = input("Cual es tu nombre?:  ")
        apellido = input("Cual es tu apellido?:  ")
        email = input("Cual es tu email?:  ")
        password = input("Cual es tu contraseña?:  ")

        usuario = modelo.Usuario(nombre, apellido, email, password)
        registro = usuario.registrar()

        if registro[0] >=1:
            print(f"perfecto {registro[1].nombre} te has registrado con el email {registro[1].email}")
        else:
            print("No te has registrado")


    def login(self):
        print("\n Ok, identificate en el sistema: ")

        email = input("Cual es tu email?:  ")
        password = input("Cual es tu contraseña?:  ")