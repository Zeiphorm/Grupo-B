#C.R.U.D tabla empleados, ID, nombre, años trabajado, asistencias, DNI, asistencias justificadas? bonificaciones?
import sqlite3
conexion=sqlite3.connect("Tabla_empleados.db")
cursor=conexion.cursor()

cursor.execute(""" CREATE TABLE IF NOT EXISTS empleados(
id INTEGER PRIMARY KEY AUTOINCREMENT,
nombre TEXT NOT NULL,
tiempo_servido INTEGER,
dni INTEGER,
asistencias_mensuales INTEGER
)
""")
conexion.commit()

class Empleado:
    def __init__(self,nombre,tiempo_servido,dni,asistencias_mensuales):
        self.nombre   = nombre
        self.tiempo_servido = tiempo_servido
        self.dni = dni
        self.asistencias_mensuales = asistencias_mensuales
    def mostrar_datos(self):
        return f"El empleado es {self.nombre} de DNI {self.dni}. Trabajo {self.tiempo_servido} años, este mes asistio {self.asistencias_mensuales} dias"

def mostrar_lista():
    cursor.execute("SELECT * FROM empleados")
    empleados= cursor.fetchall()
    if not empleados:
        print("No hay empleados")
        return
    texto = "--- empleadoss ---\n"
    for empleado in empleados:
        # empleado = (id, nombre, tiempo_servido, dni, asistencias_mensuales)
        texto += f"ID: {empleado[0]} "+f" Nombre: {empleado[1]} " +f" DNI: {empleado[2]} " +f" Años de trabajo: {empleado[3]} " + f" Dias presente este mes: {empleado[4]} "
        print(texto)

def agregar_nuevo_empleado(nombre,tiempo_servido,dni,asistencias_mensuales):
    # Valido que no esten vacios
    if nombre == "" or tiempo_servido == "" or dni == "" or asistencias_mensuales == "":
        print("Complete todos los campos")
        return
    tiempo_servido = int(tiempo_servido)
    dni = int(dni)
    asistencias_mensuales = int(asistencias_mensuales)
    empleado = Empleado(nombre,tiempo_servido,dni,asistencias_mensuales)
    cursor.execute("INSERT INTO empleados(nombre,tiempo_servido,dni,asistencias_mensuales) VALUES (?,?,?,?)",(empleado.nombre,empleado.tiempo_servido,empleado.dni,empleado.asistencias_mensuales))
    conexion.commit()
    print(f"Empleado agregado: {empleado.mostrar_datos()}")

def modificar_empleado(nombre,dni):
    if nombre == "" or dni == "":
        print("Complete todos los campos")
        return
    cursor.execute("SELECT * FROM empleados WHERE nombre = ? AND dni = ?",(nombre,dni,))
    empleado = cursor.fetchall()

    if not empleado:
        print("No hay registros de ese empleado")
        return
    #ahora tomo los datos de todo lo que escribi
    while True:
        print("Seleccione los datos a modificar (seleccione el dato usando un numero) ",mostrar_lista())
        print("1. Nombre\n2. Tiempo servido\n3. DNI\n4. Asistencias\n0. Salir")
        select= input("")
        if select == "1":
            nuevo_nombre = input("Nuevo dato: ")
            cursor.execute(
                "UPDATE empleados SET nombre = ? WHERE nombre = ? AND dni = ?",
                (nuevo_nombre, nombre, dni),
            )
            conexion.commit()
            nombre = (
            )
            print("Empleado modificado correctamente")
        elif select == "2":
            nuevo_tiempo_servido = int(input("Nuevo dato: "))
            cursor.execute(
                "UPDATE empleados SET tiempo_servido = ? WHERE nombre = ? AND dni = ?",
                (nuevo_tiempo_servido, nombre, dni),
            )
            conexion.commit()
            print("Empleado modificado correctamente")
        elif select == "3":
            nuevo_dni = int(input("Nuevo dato: "))
            cursor.execute(
                "UPDATE empleados SET dni = ? WHERE nombre = ? AND dni = ?",
                (nuevo_dni, nombre, dni),
            )
            conexion.commit()
            dni = nuevo_dni
            print("Empleado modificado correctamente")
        elif select == "4":
            nuevas_asistencias_mensuales = int(input("Nuevo dato: "))
            cursor.execute(
                "UPDATE empleados SET asistencias_mensuales = ? WHERE nombre = ? AND dni = ?",
                (nuevas_asistencias_mensuales, nombre, dni),
            )
            conexion.commit()
            print("Empleado modificado correctamente")
        else:
            print("Error, intente devuelta")

def eliminar_empleado(nombre,dni):
    if nombre == "" or dni == "":
        print("Campo vacio. Escriba un nombre y DNI de empleado")
        return
    nombre = nombre
    dni = dni
    cursor.execute("SELECT * FROM empleados WHERE nombre = ?, dni = ?",(nombre,dni))
    empleado = cursor.fetchmany()

    if not empleado:
        print("No hay registro para ese empleado")
        return
    cursor.execute("DELETE FROM empleados WHERE nombre = ?, dni = ?",(nombre,dni))
    conexion.commit()
    print("Empleado eliminado correctamente")

#Prueba interna- Puede eliminarse luego
while True:
    print("MENU")
    print("1. Mostrar lista")
    print("2. Agregar")
    print("3. Modificar")
    print("4. Eliminar")
    print("0. Salir")
    op=input("Seleccione opcion\n")
    if op=="0":
        conexion.close()
        break
    elif op=="1":
        mostrar_lista()
    elif op=="2":
        print("Ingrese los datos de su empleado")
        nombre=input("Nombre del empleado\n")
        dni=int(input("DNI\n"))
        tiempo_servido=int(input("Tiempo trabajado (en años)\n"))
        asistencias_mensuales=int(input("Numero de dias asistidos este mes\n"))
        agregar_nuevo_empleado(nombre,dni,tiempo_servido,asistencias_mensuales)
    elif op=="3":
        print("Ingrese los datos de su empleado")
        nombre=input("Nombre del empleado\n")
        dni=input("DNI del empleado\n")
        modificar_empleado(nombre,dni)
    elif op=="4":
        print("Ingrese los datos de su empleado")
        nombre=input("Nombre del empleado\n")
        dni=input("DNI del empleado\n")
        eliminar_empleado(nombre,dni)
    else:
        print("opcion invalida")