#Un campo para ingresar nombre de producto, un campo para cargar producto, y cargar stock, boton agregar producto y boton elmininar producto, tabla de productos registrados.

import tkinter as tk
from tkinter import ttk

ventana= tk.Tk()
ventana.title("Negocio de mi tio")
ventana.geometry('800x800')
ventana.configure(bg="#EE0707")

encabezado=tk.Frame(ventana,height=105)
encabezado.pack(fill="x")
encabezado.pack_propagate(False)


tk.Label(
    encabezado,
    text="Supermercado Peru",
    font=("Segoe UI",25,"bold"),

).pack(anchor="w",padx=30,pady=(17,0))


estilo=ttk.Style()
estilo.theme_use("clam")


resultado = tk.Label(ventana,text ="")
resultado.pack()
tk.Label(ventana,text="Ingrese el nombre del producto").pack()
tk.Label(ventana, text="Nombre:").pack()
entrada_nombre = tk.Entry(ventana)
entrada_nombre.pack()
tk.Label(ventana,text="Escriba para cargar el producto").pack()
tk.Label(ventana).pack()
entrada_cargar = tk.Entry(ventana)
entrada_cargar.pack()
tk.Label(ventana,text="Escriba para cargar el stock").pack()
tk.Label(ventana, text="stock:").pack()
entrada_stock = tk.Entry(ventana)
entrada_stock.pack()


boton1 = tk.Button(ventana,text="Agregar Producto")
boton1.pack()
boton2 = tk.Button(ventana,text="Eliminar producto")
boton2.pack()

ventana.mainloop()