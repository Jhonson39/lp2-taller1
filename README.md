# Taller 1 - Tienda Virtual con Flask

## Descripción del proyecto

Este proyecto consiste en desarrollar una tienda virtual utilizando Flask. La aplicación permite mostrar un catálogo de productos, consultar sus detalles y navegar por las diferentes páginas.

Los productos se almacenan en un archivo JSON, por lo que no es necesario utilizar una base de datos.

## Objetivo

Crear una aplicación web con Python y Flask que permita visualizar productos de una tienda virtual mediante páginas HTML dinámicas.

## Tecnologías utilizadas

- **Python:** lenguaje de programación.
- **Flask:** framework para desarrollar la aplicación web.
- **HTML:** estructura de las páginas.
- **CSS:** diseño y estilos de la tienda.
- **Jinja2:** permite mostrar información dinámica en las plantillas.
- **JSON:** archivo utilizado para almacenar los productos.

## Estructura del proyecto

```text
taller1/
├── app/
│   ├── __init__.py
│   ├── routes.py
│   ├── data/
│   │   └── productos.json
│   ├── static/
│   │   ├── css/
│   │   └── images/
│   └── templates/
│       ├── base.html
│       ├── index.html
│       └── detalle.html
├── requirements.txt
├── run.py
└── README.md
```

## Funcionalidades

- Mostrar el catálogo de productos en la página principal.
- Consultar la información de cada producto.
- Buscar productos mediante su SKU en la URL.
- Mostrar una página de error 404 cuando un producto no existe.
- Cargar los productos desde un archivo JSON.
- Utilizar plantillas HTML dinámicas con Jinja2.

## Instalación y ejecución

### 1. Crear el entorno virtual

```bash
python3 -m venv venv
```

### 2. Activar el entorno virtual

En Ubuntu o WSL2:

```bash
source venv/bin/activate
```

### 3. Instalar las dependencias

```bash
pip install -r requirements.txt
```

### 4. Ejecutar la aplicación

```bash
python3 run.py
```

### 5. Abrir la tienda

Ingresar desde el navegador a:

http://127.0.0.1:5000

## Rutas principales

| Ruta | Descripción |
|---|---|
| `/` | Muestra el catálogo de productos. |
| `/producto/<sku>` | Muestra los detalles de un producto específico. |

## Almacenamiento de los productos

Los productos se encuentran en el archivo `app/data/productos.json`. Este archivo contiene la información necesaria para mostrar cada producto en la tienda.

## Autor

Estudiante de programación.

## Conclusión

Con este taller se ponen en práctica los conocimientos básicos de Python, Flask, HTML, CSS y plantillas Jinja2 para construir una aplicación web sencilla. También se aprende a organizar un proyecto y a manejar información almacenada en archivos JSON.
