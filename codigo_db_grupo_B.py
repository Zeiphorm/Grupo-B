import sqlite3
import tkinter as tk
from tkinter import tk


conexion=sqlite3.connect("Base_negocio.db")
cursor=conexion.cursor()

cursor.execute(""" CREATE TABLE IF NOT EXISTS productos(
id INTEGER PRIMARY KEY AUTOINCREMENT,
nombre_producto TEXT NOT NULL,
stock_disponible INTEGER,
precio INTEGER
)
""")
conexion.commit()

class Producto:
    def __init__(self,nombre_producto,stock_disponible,precio):
        self.nombre_producto   = nombre_producto
        self.stock_disponible = stock_disponible
        self.precio     = precio
    def mostrar_datos(self):
        return f"El producto es {self.nombre_producto}, Quedan {self.stock_disponible} copias del producto, cuesta ${self.precio} pesos"

def mostrar_lista():
    cursor.execute("SELECT * FROM productos")
    productos= cursor.fetchall()
    if not productos:
        print("No hay productos")
        return
    texto = "--- Productos ---\n"
    for producto in productos:
        # producto = (id, nombre_producto, stock_disponible, precio)
        texto += f"ID: {producto[0]} "+f"Nombre: {producto[1]} " +f"Stock disponible: {producto[2]} " + f"Precio: {producto[3]} "
        print(texto)

def agregar_nuevo_producto(nombre_producto,stock_disponible,precio):
    # Valido que no esten vacios
    if nombre_producto == "" or stock_disponible == "" or precio == "":
        print("Complete todos los campos")
        return
    stock_disponible = int(stock_disponible)
    precio = int(precio)
    producto = Producto(nombre_producto,stock_disponible,precio)
    cursor.execute("INSERT INTO productos(nombre_producto,stock_disponible,precio) VALUES (?,?,?)",(producto.nombre_producto,producto.stock_disponible,producto.precio))
    conexion.commit()
    print(f"Producto agregado: {producto.mostrar_datos()}")

def eliminar_producto(nombre_producto):
    if nombre_producto =="":
        print("Campo vacio. Escriba un nombre de producto")
        return
    nombre_producto = nombre_producto
    cursor.execute("SELECT * FROM productos WHERE nombre_producto = ?",(nombre_producto,))
    producto = cursor.fetchone()

    if not producto:
        print("No hay registro para ese producto")
        return
    cursor.execute("DELETE FROM productos WHERE nombre_producto = ?",(nombre_producto,))
    conexion.commit()
    print("Producto eliminado correctamente")

#Prueba interna- Puede eliminarse luego

   

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