from tkinter import * 
from tkinter import messagebox as messagebox

ventana = Tk()
ventana.geometry("400x300")

def sacarAlerta():
    messagebox.showinfo("A c T 1 V", "esta es una alerta de informacion")       #alerta de tipo informacion
    #messagebox.showerror("A c T 1 V", "esta es una alerta de informacion")      #alerta de tipo error
    #messagebox.showwarning("A c T 1 V", "esta es una alerta de informacion")    #alerta de tipo cuidado

Button(ventana, text="Enviar alerta", command=sacarAlerta).pack()



def salir():
    resultado = messagebox.askquestion("Salir", "¿Deseas continuar en el programa?") #alerta de tipo pregunta al usuario

    if resultado != "yes":
        ventana.destroy()  #el metodo destroy se utiliza para detener la ejecucion de un programa

Button(ventana, text="Salir", command=salir).pack()

ventana.mainloop()