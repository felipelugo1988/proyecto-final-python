import sqlite3

conexion = sqlite3.connect("restaurante.db")
cursor = conexion.cursor()


class Pedido:
    def __init__(self):
        self.pedidos = {}
        self.contador_pedido = 1

    def crear_pedido(self, cliente, producto, precio):
        self.pedidos[self.contador_pedido] = {
            'cliente': cliente,
            'producto': producto,
            'precio': precio
        }
        self.contador_pedido += 1

        cursor.execute("INSERT INTO Pedido (cliente, producto, precio) VALUES (?, ?, ?)", (cliente, producto, precio))
        conexion.commit()

        #Agregamos el codigo para simular la impresion de un ticket en un archivo    
        with open("ticket.txt", "a") as ticket_file:
            ticket_file.write(f"Cliente: {cliente}\nProducto: {producto}\nPrecio: ${precio:.2f}\n\n")

    def cancelar_pedido(self, numero_pedido):
        if numero_pedido in self.pedidos:
            del self.pedidos[numero_pedido]
# docstring
"""
Módulo y Clase de Pedido

Esta clase permite gestionar la información de los pedidos realizados.

Funciones:
- crear_pedido(cliente, producto, precio)
- cancelar_pedido(numero_pedido)
"""

#Aqui insertamos el codigo de nuestra base de datos
cursor.execute('''
CREATE TABLE IF NOT EXISTS Pedido (
    pedido INTEGER PRIMARY KEY,
    cliente TEXT,
    producto TEXT,
    precio REAL,
    FOREIGN KEY (cliente) REFERENCES clientes(clave),
    FOREIGN KEY (producto) REFERENCES Menu(clave) 
)
''')
conexion.commit()