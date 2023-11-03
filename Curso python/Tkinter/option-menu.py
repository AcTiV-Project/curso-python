from tkinter import *

ventana = Tk()
ventana.geometry("700x600")
ventana.title("Option Menu")

def seleccionar():
    seleccionado.config(text=opcion.get())

opcion = StringVar()
opcion.set("Opcion 1")

Label(ventana, text="Selecciona una opcion").grid(row=0, column=0, columnspan=2)
select = OptionMenu(ventana, opcion, "Opcion 1", "Opcion 2", "Opcion 3")
select.grid(row=1, column=0)

Button(ventana, text="Ver", command=seleccionar).grid(row=2, column=0)

seleccionado = Label(ventana)
seleccionado.grid(row=3, column=0)

ventana.mainloop()