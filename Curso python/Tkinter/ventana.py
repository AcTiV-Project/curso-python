from tkinter import * #Importar modulo

ventana = Tk() #creando la raiz

ventana.geometry("750x550") #tamaño de la ventana
ventana.title("Interfaz grafica de yoyitin") #Titulo a la ventana
ventana.iconbitmap("./Tkinter/imagenes/tk.ico") #Icono a la ventana
ventana.resizable(0, 0) #Bloquear el redimensionamiento de la ventana



ventana.mainloop() #arrancar y mostrar la ventana