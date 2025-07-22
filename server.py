# Juan Diego Medina 21/07/25
from flask import Flask, render_template

app = Flask(__name__)

# Ruta base
@app.route("/juego")
def juego():
    return render_template("index.html", cantidad=3, colorcito="red")

# Ruta con cantidad
@app.route("/juego/<int:x>")
def juego_con_cantidad(x):
    return render_template("index.html", cantidad=x, colorcito="red")

# Ruta con cantidad y color
@app.route("/juego/<int:x>/<color>")
def juego_con_cantidad_y_color(x, color):
    return render_template("index.html", cantidad=x, colorcito=color)

if __name__ == "__main__":
    app.run(debug=True)
