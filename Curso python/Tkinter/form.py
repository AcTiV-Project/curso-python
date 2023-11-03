from tkinter import *

ventana = Tk()
ventana.title("Formulario A c T 1 V")
ventana.geometry("800x500")

encabezado = Label(ventana, text="A c T 1 V")
encabezado.config(
    fg="orange",
    bg="black",
    font=("Open Sans", 18),
    padx=10,
    pady=10
)
"""
encabezado.pack(
    side=LEFT,
    anchor=NW,
    fill=X,  #Instruccion para que se expanda el elemento en el eje x al 100%
    expand=YES #instruccion para habilitar el expandimiento
)
"""
encabezado.grid(row=0, column=0, columnspan=2, sticky=W)


#Label de nombre
label = Label(ventana, text="Nombre")
label.grid(row=1, column=0, padx=5, pady=5)

#Campo nombre
campo_texto = Entry(ventana)
campo_texto.grid(row=1, column=1, sticky=W, padx=5, pady=5)
campo_texto.config(
    justify=CENTER #Instruccion para especificar por donde saldra el texto al empezar a escribir dentro de la caja de texto
)


""""""""

#Label de apellido
label = Label(ventana, text="Apellido")
label.grid(row=2, column=0, padx=5, pady=5)

#Campo apellido
campo_texto = Entry(ventana)
campo_texto.grid(row=2, column=1, sticky=W, padx=5, pady=5)
campo_texto.config(
    justify=RIGHT, #Instruccion para especificar por donde saldra el texto al empezar a escribir dentro de la caja de texto
    state="normal" #Instruccion para habilitar un caja de texto ("disabled" para desabilitarlo)
)

""""""""

label = Label(ventana, text="Descripcion")
label.grid(row=3, column=0, padx=5, pady=5, sticky=N)

campo_grande = Text(ventana)
campo_grande.grid(row=3, column=1, sticky=W, padx=5, pady=5)

campo_grande.config(
    width=40,
    height=7
)

Label(ventana).grid(row=4, column=1) #linea separadora para separar la caja grande del boton

boton = Button(ventana, text="Enviar")
boton.grid(row=5, column=1, sticky=W)
boton.config(
    padx=5,
    pady=3,
    bg="black",
    fg="white"
)


ventana.mainloop()