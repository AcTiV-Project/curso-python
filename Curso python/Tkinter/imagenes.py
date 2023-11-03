from tkinter import *
from PIL import Image, ImageTk

ventana = Tk()
ventana.geometry("500x500")

imagen = Image.open('./Tkinter/imagenes/software.jpg')
render = ImageTk.PhotoImage(imagen)

Label(ventana, image=render).pack(anchor=E)



ventana.mainloop()