from tkinter import *

ventama = Tk()
ventama.title("Frame en python")
ventama.geometry("400x450")

marco = Frame(ventama, width=200, height=200)

marco.config(
    bg="red",
    bd="2",
    relief=SOLID
)

marco.pack(
    side=BOTTOM,
    anchor=N
)
marco.pack_propagate(False) #intruccion para evitar que mi frame se contraiga al meter un elemento

texto = Label(marco, text="A c T 1 V")

texto.config(
    bg="red",
    fg="black",
    font=("Arial", 20),          #Ejemplo de como centrar texto con el metodo config
    #width=10,
    #height=10,
    #anchor="center"
)

texto.pack(anchor="center", fill=Y, expand=YES)  #Ejemplo utilizando el metodo pack




ventama.mainloop()