class Venta:
    def __init__(self, usuario_id, codigo_producto, cantidad):
        self.usuario_id = usuario_id
        self.codigo_producto = codigo_producto
        self.cantidad = cantidad

    def __str__(self):
        return f"Usuario: {self.usuario_id} - Producto: {self.codigo_producto} - Cantidad: {self.cantidad}"