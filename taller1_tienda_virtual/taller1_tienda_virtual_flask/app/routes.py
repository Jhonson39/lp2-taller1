import json
from pathlib import Path
from flask import Blueprint, abort, render_template

main = Blueprint("main", __name__)
RUTA_PRODUCTOS = Path(__file__).parent / "data" / "productos.json"

def cargar_productos():
    with open(RUTA_PRODUCTOS, "r", encoding="utf-8") as archivo:
        return json.load(archivo)

def buscar_producto_por_sku(sku):
    productos = cargar_productos()
    for producto in productos:
        if producto["sku"] == sku:
            return producto
    return None

@main.route("/")
def index():
    productos = cargar_productos()
    return render_template("index.html", productos=productos)

@main.route("/producto/<sku>")
def detalle(sku):
    producto = buscar_producto_por_sku(sku)
    if producto is None:
        abort(404)
    return render_template("detalle.html", producto=producto)
