import sqlite3

conexion = sqlite3.connect("restaurante.db")
cursor = conexion.cursor()


class Menu:
    def __init__(self):
        self.menu = {}

    def agregar_producto(self, clave, nombre, precio):
        self.menu[clave] = {
            'nombre': nombre,
            'precio': precio
        }

        cursor.execute("INSERT INTO Menu VALUES (?, ?, ?, ?, ?)", (clave, nombre, precio))
        conexion.commit()

    def eliminar_producto(self, clave):
        if clave in self.menu:
            del self.menu[clave]

    def actualizar_producto(self, clave, nombre=None, precio=None):
        if clave in self.menu:
            if nombre:
                self.menu[clave]['nombre'] = nombre
            if precio:
                self.menu[clave]['precio'] = precio

# docstring
"""
Módulo y Clase de Menú

Esta clase permite gestionar la información del menú de productos.

Funciones:
- agregar_producto(clave, nombre, precio)
- eliminar_producto(clave)
- actualizar_producto(clave, nombre, precio)
"""

#Aqui insertamos el codigo de nuestra base de datos
cursor.execute('''
CREATE TABLE IF NOT EXISTS Menu (
    clave TEXT PRIMARY KEY,
    nombre TEXT,
    precio REAL
)
''')
conexion.commit()