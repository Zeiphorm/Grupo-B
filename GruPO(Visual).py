#Un campo para ingresar nombre de producto, un campo para cargar producto, y cargar stock, boton agregar producto y boton elmininar producto, tabla de productos registrados.

import tkinter as tk
from tkinter import ttk

ventana= tk.Tk()
ventana.title("Negocio de mi tio")
ventana.geometry('800x800')
ventana.configure(bg="#970202")

encabezado=tk.Frame(ventana,height=105)
encabezado.pack(fill="x")
encabezado.pack_propagate(False)
encabezado.config(bg="black")

tk.Label(
    encabezado,
    text="Supermercado Peru",
    font=("Consolas",25,"bold"),
    bg="black",         
    fg="white"                       
).pack(anchor="w",padx=220,pady=(28,0),fill="both")

marco_titulo = tk.Frame(ventana, bg="#fffefe", height=20)
marco_titulo.pack(fill="x", side="top")

estilo=ttk.Style()
estilo.theme_use("clam")


lista = tk.Label(ventana,text ="",font=("Consolas",10,"bold"), bg="#970202",fg="white")
lista.pack()
tk.Label(ventana,text="Ingrese el nombre del producto",font=("Consolas",10,"bold"), bg="#970202",fg="white").pack(anchor="w",padx=30,pady=(28,0))
tk.Label(ventana, text="Nombre:",font=("Consolas",10,"bold"), bg="#970202",fg="white").pack()
entrada_nombre = tk.Entry(ventana)
entrada_nombre.pack()
tk.Label(ventana,text="Escriba para cargar el producto",font=("Consolas",10,"bold"), bg="#970202",fg="white").pack(anchor="w",padx=30,pady=(28,0))
tk.Label(ventana,font=("Consolas",10,"bold"), bg="#970202",fg="white").pack()
entrada_cargar = tk.Entry(ventana)
entrada_cargar.pack()
tk.Label(ventana,text="Escriba para cargar el stock",font=("Consolas",10,"bold"), bg="#970202",fg="white").pack(anchor="w",padx=30,pady=(28,0))
tk.Label(ventana, text="Stock:",font=("Consolas",10,"bold"), bg="#970202",fg="white").pack()
entrada_stock = tk.Entry(ventana)
entrada_stock.pack()


boton1 = tk.Button(ventana,text="Agregar Producto",font=("Consolas",10,"bold"), bg="#000000",fg="white")
boton1.pack()
boton2 = tk.Button(ventana,text="Eliminar producto",font=("Consolas",10,"bold"), bg="#000000",fg="white")
boton2.pack()

ventana.mainloop()