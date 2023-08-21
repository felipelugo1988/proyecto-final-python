import sqlite3

conexion = sqlite3.connect("restaurante.db")
cursor = conexion.cursor()



class Clientes:
    def __init__(self):
        self.clientes = {}

    def agregar_cliente(self, clave, nombre, direccion, correo, telefono):
        self.clientes[clave] = {
            'nombre': nombre,
            'direccion': direccion,
            'correo_electronico': correo,
            'telefono': telefono
        }

        cursor.execute("INSERT INTO Clientes VALUES (?, ?, ?, ?, ?)", (clave, nombre, direccion, correo, telefono))
        conexion.commit()

    def eliminar_cliente(self, clave):
        if clave in self.clientes:
            del self.clientes[clave]

    def actualizar_cliente(self, clave, nombre=None, direccion=None, correo=None, telefono=None):
        if clave in self.clientes:
            if nombre:
                self.clientes[clave]['nombre'] = nombre
            if direccion:
                self.clientes[clave]['direccion'] = direccion
            if correo:
                self.clientes[clave]['correo_electronico'] = correo
            if telefono:
                self.clientes[clave]['telefono'] = telefono

# docstring
"""
Módulo y Clase de Clientes

Esta clase permite gestionar la información de los clientes.

Funciones:
- agregar_cliente(clave, nombre, direccion, correo, telefono)
- eliminar_cliente(clave)
- actualizar_cliente(clave, nombre, direccion, correo, telefono)
"""


#Aqui insertamos el codigo de nuestra base de datos
cursor.execute('''
CREATE TABLE IF NOT EXISTS Clientes (
    clave TEXT PRIMARY KEY,
    nombre TEXT,
    direccion TEXT,
    correo_electronico TEXT,
    telefono TEXT
)
''')
conexion.commit()