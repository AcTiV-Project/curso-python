from tkinter import *

#POSICIONAMIENTOS CON SIDE

ventana = Tk()
ventana.geometry("600x600")

text = Label(ventana, text="A c T i V")
text.config(
    bg="black",
    fg="white",
    font=("consolas", 30)
)

text.pack(
    side=BOTTOM,
    fill=X, #para expandir un elemento horizontalmente
    expand=YES #instruccion para habilitar el expandimiento
)

ventana.mainloop()