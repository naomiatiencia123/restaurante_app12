from modelos.producto import Producto
from modelos.usuario import Usuario
from modelos.venta import Venta
from servicios.archivo_servicio import cargar_datos, guardar_datos


class Restaurante:

    def __init__(self):
        self.productos = []
        self.usuarios = []
        self.ventas = []

        # Índices para realizar búsquedas rápidas
        self.indice_productos = {}
        self.indice_usuarios = {}
        self.indice_ventas_usuario = {}

    def reconstruir_indices(self):
        # Índice de productos por código
        self.indice_productos = {
            producto.codigo: producto
            for producto in self.productos
        }

        # Índice de usuarios por identificación
        self.indice_usuarios = {
            usuario.identificacion: usuario
            for usuario in self.usuarios
        }

        # Índice de ventas por usuario
        self.indice_ventas_usuario = {}

        for venta in self.ventas:
            if venta.usuario_id not in self.indice_ventas_usuario:
                self.indice_ventas_usuario[venta.usuario_id] = []

            self.indice_ventas_usuario[venta.usuario_id].append(venta)

    def cargar_datos(self):
        productos_data = cargar_datos("datos/productos.json")
        usuarios_data = cargar_datos("datos/usuarios.json")
        ventas_data = cargar_datos("datos/ventas.json")

        self.productos = [
            Producto(
                producto["codigo"],
                producto["nombre"],
                producto["precio"],
                producto["stock"]
            )
            for producto in productos_data
        ]

        self.usuarios = [
            Usuario(
                usuario["identificacion"],
                usuario["nombre"]
            )
            for usuario in usuarios_data
        ]

        self.ventas = [
            Venta(
                venta["usuario_id"],
                venta["codigo_producto"],
                venta["cantidad"]
            )
            for venta in ventas_data
        ]

        # Reconstruir los índices después de cargar los datos
        self.reconstruir_indices()

    def guardar_datos(self):
        productos_data = [
            {
                "codigo": producto.codigo,
                "nombre": producto.nombre,
                "precio": producto.precio,
                "stock": producto.stock
            }
            for producto in self.productos
        ]

        usuarios_data = [
            {
                "identificacion": usuario.identificacion,
                "nombre": usuario.nombre
            }
            for usuario in self.usuarios
        ]

        ventas_data = [
            {
                "usuario_id": venta.usuario_id,
                "codigo_producto": venta.codigo_producto,
                "cantidad": venta.cantidad
            }
            for venta in self.ventas
        ]

        guardar_datos("datos/productos.json", productos_data)
        guardar_datos("datos/usuarios.json", usuarios_data)
        guardar_datos("datos/ventas.json", ventas_data)

    # Buscar producto rápidamente por código
    def buscar_producto(self, codigo):
        return self.indice_productos.get(codigo)

    # Buscar usuario rápidamente por identificación
    def buscar_usuario(self, identificacion):
        return self.indice_usuarios.get(identificacion)

    # Buscar ventas rápidamente por usuario
    def ventas_por_usuario(self, usuario_id):
        return self.indice_ventas_usuario.get(usuario_id, [])

    # Registrar una venta y actualizar el stock
    def realizar_venta(self, usuario_id, codigo_producto, cantidad):
        usuario = self.indice_usuarios.get(usuario_id)

        if usuario is None:
            return False, "Usuario no encontrado."

        producto = self.indice_productos.get(codigo_producto)

        if producto is None:
            return False, "Producto no encontrado."

        if cantidad <= 0:
            return False, "La cantidad debe ser mayor que cero."

        if producto.stock < cantidad:
            return False, "Stock insuficiente."

        # Actualizar stock
        producto.stock -= cantidad

        # Crear la venta
        venta = Venta(usuario_id, codigo_producto, cantidad)
        self.ventas.append(venta)

        # Actualizar el índice de ventas por usuario
        if usuario_id not in self.indice_ventas_usuario:
            self.indice_ventas_usuario[usuario_id] = []

        self.indice_ventas_usuario[usuario_id].append(venta)

        return True, "Venta realizada correctamente."