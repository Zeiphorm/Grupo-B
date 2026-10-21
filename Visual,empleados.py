#como tabla con todo botones, y su funcion (Crud)
#nombres de empleados, años trabajando, dni, y asistencias mensuales. bonificaciones, y asistencias justificadas y ambas estan relacionadas.

import tkinter as tk
from tkinter import ttk


def agregar_empleado():
    nombre = entrada_nombre.get().strip()
    puesto = entrada_cargar.get().strip()
    stock_id = entrada_stock.get().strip()
    
    if nombre and puesto and stock_id:

        registro = f"Nombre: {nombre} | Puesto: {puesto} | DNI: {stock_id}"
        lista_empleados.insert(tk.END, registro)
        

        entrada_nombre.delete(0, tk.END)
        entrada_cargar.delete(0, tk.END)
        entrada_stock.delete(0, tk.END)


def eliminar_empleado():
    try:

        indice_seleccionado = lista_empleados.curselection()[0]
        lista_empleados.delete(indice_seleccionado)
    except IndexError:
        pass



ventana = tk.Tk()
ventana.title("Empleados data")
ventana.geometry("800x800")
ventana.configure(bg="#970202")


encabezado = tk.Frame(ventana, height=105)
encabezado.pack(fill="x")
encabezado.pack_propagate(False)
encabezado.config(bg="black")

tk.Label(
    encabezado,
    text="Empleados de Rockstar",
    font=("Consolas", 25, "bold"),
    bg="black",
    fg="white",
).pack(anchor="center", pady=(28, 0))

marco_titulo = tk.Frame(ventana, bg="#fffefe", height=20)
marco_titulo.pack(fill="x", side="top")

estilo = ttk.Style()
estilo.theme_use("clam")


marco_lista = tk.Frame(ventana, bg="#970202")
marco_lista.pack(pady=20, fill="both", expand=True, padx=50)


scrollbar = tk.Scrollbar(marco_lista, orient="vertical")
scrollbar.pack(side="right", fill="y")


lista_empleados = tk.Listbox(
    marco_lista, 
    font=("Consolas", 11), 
    bg="#1a1a1a", 
    fg="white", 
    selectbackground="#fffefe", 
    selectforeground="black",
    yscrollcommand=scrollbar.set
)
lista_empleados.pack(side="left", fill="both", expand=True)
scrollbar.config(command=lista_empleados.yview)



tk.Label(
    ventana, text="Nombre del Empleado:", font=("Consolas", 11, "bold"), bg="#970202", fg="white"
).pack(pady=(10, 0))
entrada_nombre = tk.Entry(ventana, font=("Consolas", 11), width=40)
entrada_nombre.pack(pady=5)

tk.Label(
    ventana, text="Puesto:", font=("Consolas", 11, "bold"), bg="#970202", fg="white"
).pack(pady=(10, 0))
entrada_cargar = tk.Entry(ventana, font=("Consolas", 11), width=40)
entrada_cargar.pack(pady=5)

tk.Label(
    ventana, text="DNI:", font=("Consolas", 11, "bold"), bg="#970202", fg="white"
).pack(pady=(10, 0))
entrada_stock = tk.Entry(ventana, font=("Consolas", 11), width=40)
entrada_stock.pack(pady=5)



boton1 = tk.Button(
    ventana,
    text="Contratar Empleado",
    font=("Consolas", 11, "bold"),
    bg="#000000",
    fg="white",
    command=agregar_empleado, 
    padx=10,
    pady=5
)
boton1.pack(pady=10)

boton2 = tk.Button(
    ventana,
    text="Despedir empleado",
    font=("Consolas", 11, "bold"),
    bg="#000000",
    fg="white",
    command=eliminar_empleado, 
    padx=10,
    pady=5
)
boton2.pack(pady=5)

ventana.mainloop()
