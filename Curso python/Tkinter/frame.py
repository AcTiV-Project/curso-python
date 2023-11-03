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

texto = Label(marco, text="Texto dentro del marco").pack() #texto dentro del frame

texto.config(
    bg="blue",
    fg="white",
    font=("Arial", 20),
    anchor="CENTER"
)

texto.pack()

ventama.mainloop()