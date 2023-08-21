from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

# Conexión a la base de datos
conexion = sqlite3.connect("restaurante.db")
conexion.row_factory = sqlite3.Row
cursor = conexion.cursor()

@app.route("/")
def index():
    return "¡Bienvenido a Happy Burger!"

@app.route("/consulta_pedido", methods=["GET", "POST"])
def consulta_pedido():
    if request.method == "POST":
        numero_pedido = request.form["numero_pedido"]
        cursor.execute("SELECT * FROM Pedido WHERE pedido = ?", (numero_pedido,))
        pedido = cursor.fetchone()

        return render_template("pedido.html", pedido=pedido)

    return render_template("consulta_pedido.html")

if __name__ == "__main__":
    app.run(debug=True)
