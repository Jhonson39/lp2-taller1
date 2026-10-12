# Guía rápida — Taller 1

## Abrir en VS Code
1. Descomprime el ZIP.
2. Abre VS Code y elige **Archivo > Abrir carpeta**.
3. Selecciona `taller1_tienda_virtual_flask`.
4. Abre **Terminal > Nueva terminal**.

## Preparar el proyecto (Ubuntu o WSL2)
Ejecuta estos comandos uno por uno desde la carpeta del proyecto:

```bash
python3 --version
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Iniciar la tienda
Con el entorno virtual activado:

```bash
python3 run.py
```

Abre `http://127.0.0.1:5000` en el navegador. Para detenerlo, vuelve a la terminal y presiona `Ctrl+C`.

## Pruebas solicitadas
1. La página principal debe mostrar los 10 productos.
2. Pulsa **Ver detalle** para abrir la ficha de un producto.
3. Comprueba que se muestren nombre, marca, SKU y precio.
4. Visita `http://127.0.0.1:5000/producto/NO-EXISTE` para comprobar el error 404.

## Archivos principales
- `run.py`: inicia el servidor.
- `app/__init__.py`: crea la aplicación Flask.
- `app/routes.py`: rutas y lectura del JSON.
- `app/data/productos.json`: catálogo sin base de datos.
- `app/templates/`: páginas HTML.
- `app/static/css/style.css`: diseño.
- `requirements.txt`: dependencia Flask.

Nota: debes ejecutar el proyecto en tu computador para confirmar que funciona con tu instalación de Python.
