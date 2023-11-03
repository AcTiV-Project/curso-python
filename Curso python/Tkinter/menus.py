from tkinter import * 

ventana = Tk()
ventana.geometry("700x700")
ventana.title("Menus")

mi_menu = Menu(ventana)
ventana.config(menu=mi_menu)

#Submenu
archivo = Menu(mi_menu, tearoff=0)

archivo.add_cascade(label="Nuevo Archivo")
archivo.add_cascade(label="Nuevo Ventana")

archivo.add_separator()  #Agregando un separador

archivo.add_cascade(label="Abrir Carpeta")
archivo.add_cascade(label="Abrir Ventana")
archivo.add_separator()  #Agregando un separador

archivo.add_command(label="Salir", command=ventana.quit)
#Submenu


mi_menu.add_cascade(label="Archivo", menu=archivo)  #Utilizar el metodo add_cascade en el boton donde crearemos el submenu




mi_menu.add_command(label="Editar")
mi_menu.add_command(label="Seleccion")



ventana.mainloop()