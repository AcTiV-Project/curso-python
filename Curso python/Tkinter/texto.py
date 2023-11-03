from tkinter import *

ventana = Tk()
ventana.geometry("600x600")

texto = Label(ventana, text="Curso de python")
texto.config(
    fg="white", #color de la letra
    bg="black", #color de fondo
    padx=40, #padding horizontal por dentro
    pady=40, #padding vertical por dentro
    font=("Consolas", 30)
)
texto.pack()

texto = Label(ventana, text="Master en python")
texto.config(
    #para dar estilos al elementos se hace dentro del config
)
texto.pack(anchor=E) #para mover el elemento se hace dentor del pack

texto = Label(ventana, text="Yoyitin")
texto.config(
    height=5, #altura de 5 lineas a mi elemento
    bg="red",
    cursor="spider" #tipo de cursor en el elemento
)


texto.pack()


ventana.mainloop()