Restaurante App - Semana 12

JAMIE NAOMI ATIENCIA VASQUEZ

Descripción

Este proyecto consiste en un sistema básico para administrar un restaurante utilizando Python y Programación Orientada a Objetos.

El sistema permite administrar productos, usuarios y ventas, además de guardar y cargar la información mediante archivos JSON.

En esta semana se incorporaron estructuras de datos como dict para realizar búsquedas más rápidas mediante índices.

Funcionalidades

El sistema permite:

Mostrar todos los productos registrados.
Mostrar todos los usuarios registrados.
Buscar un producto mediante su código.
Buscar un usuario mediante su identificación.
Consultar las ventas asociadas a un usuario.
Guardar los datos en archivos JSON.
Cargar los datos desde archivos JSON.
Realizar búsquedas rápidas utilizando índices construidos con dict.
Estructura del proyecto
restaurante_app12/
│
├── datos/
│   ├── productos.json
│   ├── usuarios.json
│   └── ventas.json
│
├── modelos/
│   ├── producto.py
│   ├── usuario.py
│   └── venta.py
│
├── servicios/
│   ├── archivo_servicio.py
│   └── restaurante.py
│
├── main.py
└── README.md

Ejecución

Para ejecutar el programa, abrir una terminal en la carpeta principal del proyecto y utilizar:

python main.py


Luego se mostrará un menú con las diferentes opciones disponibles.

Estructuras de datos

Para mejorar la velocidad de las búsquedas se utilizan diccionarios (dict) como índices:

indice_productos: permite buscar productos mediante su código.
indice_usuarios: permite buscar usuarios mediante su identificación.
indice_ventas_usuario: permite consultar rápidamente las ventas asociadas a un usuario.

Los índices se reconstruyen después de cargar los datos desde los archivos JSON.

Datos de prueba

El proyecto incluye datos de prueba para:

4 productos.
3 usuarios.
4 ventas.

También se realizaron pruebas de búsquedas existentes y no existentes para comprobar el correcto funcionamiento del sistema.