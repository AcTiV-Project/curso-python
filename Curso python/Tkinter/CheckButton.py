from tkinter import *

ventana = Tk()
ventana.geometry("500x400")

#Botones check
def mostrarprofesion():
    texto = ""

    if web.get():
        texto += "desarrollo web"

    if movil.get():
        if web.get():
            texto += " y desarrollo web"
        else:
            texto += "desarrollo movil"

    mostrar.config(
        text=texto, 
        bg="green",
        fg="white"
    )

web = IntVar()
movil = IntVar()

#Checkbutton
Label(ventana, text="¿A que te dedicas actualmente?").grid(row=0, column=0, columnspan=2)


Checkbutton(
    ventana, text="Desarrollo Web",
    variable=web,
    onvalue=1,
    offvalue=0,
    command=mostrarprofesion
).grid(row=1, column=0, columnspan=2)


Checkbutton(
    ventana, text="Desarrollo movil",
    variable=movil,
    onvalue=1,
    offvalue=0,
    command=mostrarprofesion
).grid(row=2, column=0, columnspan=2)

mostrar = Label(ventana)
mostrar.grid(row=3, column=0)





ventana.mainloop()
