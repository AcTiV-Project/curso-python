"""
Ejercicio con tkinter (Calculadora)
"""

from tkinter import *
from tkinter import messagebox 

def sumar():
    try:
        resultado.set(float(numero1.get()) + float(numero2.get()))
        mostrarResultado()
    except:
        messagebox.showerror("Error", "Introduce valores correctos...")

def restar():
    try:
        resultado.set(float(numero1.get()) - float(numero2.get()))
        mostrarResultado()
    except:
        messagebox.showerror("Error", "Introduce valores correctos...")


def multiplicar():
    try:
        resultado.set(float(numero1.get()) * float(numero2.get()))
        mostrarResultado()
    except:
        messagebox.showerror("Error", "Introduce valores correctos...")

def dividir():
    try:
        resultado.set(float(numero1.get()) / float(numero2.get()))
        mostrarResultado()
    except:
        messagebox.showerror("Error", "Introduce valores correctos...")

def mostrarResultado():
    messagebox.showinfo("Resultado", f"El resultado es: {resultado.get()}")
    numero1.set("")
    numero2.set("")






ventana = Tk()
ventana.geometry("400x400")
ventana.title("Calculadora")

numero1 = StringVar()
numero2 = StringVar()
resultado = StringVar()

marco = Frame(ventana)

marco.config(
    bd=5,
    relief=SOLID,
    padx=5,
    pady=5
)

marco.pack()

Label(marco, text="Primer Numero").pack()
Entry(marco, textvariable=numero1).pack()

Label(marco, text="Segundo Numero").pack()
Entry(marco, textvariable=numero2).pack()

Label(marco, text="").pack()

Button(marco, text="Sumar", command=sumar).pack(side=LEFT)    
Button(marco, text="Restar", command=restar).pack(side=LEFT) 
Button(marco, text="Multiplicar", command=multiplicar).pack(side=LEFT) 
Button(marco, text="Dividir", command=dividir).pack(side=LEFT) 









ventana.mainloop()