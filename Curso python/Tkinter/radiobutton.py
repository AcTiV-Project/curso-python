from tkinter import *

ventana = Tk()
ventana.geometry("700x600")
ventana.title("RadioButton")

#Radiobutton
def marcar():
    marcado.config(text=opcion.get())

opcion = StringVar()
opcion.set(None)

Label(ventana, text="Cual es tu genero").grid(row=3, column=0)

Radiobutton(
    ventana,
    text="Masculino",
    value="Masculino",
    variable=opcion,
    command=marcar
).grid(row=4, column=0)

Radiobutton(
    ventana,
    text="Femenino",
    value="Femenino",
    variable=opcion,
    command=marcar
).grid(row=5, column=0)

marcado = Label(ventana)
marcado.grid(row=6, column=0)



ventana.mainloop()