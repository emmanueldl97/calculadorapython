from tkinter import *
from tkinter import messagebox
ventana=Tk()
ventana.geometry("400x500")
ventana.config(bg="black")

#====================FUNCIONES==========
def opcionno():
    messagebox.showinfo("opción no disponible","Esta opción aún no se encuentra disponible")




miframe=Frame(ventana, width=400, height=600)
miframe.config(bg="gray")
miframe.pack()

#==============barra de menus=================
barra=Menu(ventana)
ventana.config(menu=barra)

opciones=Menu(barra, tearoff=0)
barra.add_cascade(label="Opciones", menu=opciones)
opciones.add_cascade(label="guardar", command=opcionno)
opciones.add_cascade(label="herramientas", command=opcionno)
opciones.add_cascade(label="configuracion", command=opcionno)
opciones.add_separator()
opciones.add_cascade(label="salir", command=quit)

ayuda=Menu(barra, tearoff=0)
barra.add_cascade(label="Ayuda", menu=ayuda)
ayuda.add_cascade(label="Ayuda", command=opcionno)

#=======================PANTALLA=================
pantalla=Label(miframe, width=40, height=3, bg="black")
pantalla.grid(row=0, columnspan=4)



#=================================BOTONES===================
uno=Button(miframe, text="1", width=10, height=10)
uno.grid(row=1, column=0, padx=10, pady=10)
dos=Button(miframe, text="2", width=10, height=10)
dos.grid(row=1, column=1, padx=10, pady=10)
tres=Button(miframe, text="3", width=10, height=10)
tres.grid(row=1, column=2, padx=10, pady=10)

cuatro=Button(miframe, text="4", width=10, height=10)
cuatro.grid(row=2, column=0, padx=10, pady=10)
cinco=Button(miframe, text="5", width=10, height=10)
cinco.grid(row=2, column=1, padx=10, pady=10)
seis=Button(miframe, text="6", width=10, height=10)
seis.grid(row=2, column=2, padx=10, pady=10)

siete=Button(miframe, text="7", width=10, height=10)
siete.grid(row=3, column=0, padx=10, pady=10)
ocho=Button(miframe, text="8", width=10, height=10)
ocho.grid(row=3, column=1, padx=10, pady=10)
nueve=Button(miframe, text="9", width=10, height=10)
nueve.grid(row=3, column=2, padx=10, pady=10)

menos=Button(miframe, text="-", width=10, height=10)
menos.grid(row=1, column=3, padx=10, pady=10)
por=Button(miframe, text="x", width=10, height=10)
por.grid(row=2, column=3, padx=10, pady=10)
mas=Button(miframe, text="+", width=10, height=10)
mas.grid(row=3, column=3, padx=10, pady=10)
igual=Button(miframe, text="=", width=40, height=5)
igual.grid(row=4, column=0, columnspan=4, padx=10, pady=10)





ventana.mainloop()