from tkinter import *

ventana = Tk()
ventana.geometry("300x400")


def getDato():
    resultado.set(dato.get())

    if len(resultado.get()) >= 1:
        texto_recogido.config(
            bg="orange",
            fg="black"
        )

dato = StringVar()
resultado = StringVar()

Label(ventana, text="Ingresa un dato").pack(anchor=NW, padx=10, pady=10)
Entry(ventana, textvariable=dato).pack(anchor=NW, padx=10, pady=10)

Label(ventana, text="datorecogido").pack(anchor=NW, padx=10, pady=10)



texto_recogido = Label(ventana, textvariable=resultado)

texto_recogido.pack(anchor=NW, padx=10, pady=10)

Button(ventana, text="Enviar", command=getDato).pack(anchor=NW, padx=10, pady=10)


ventana.mainloop()