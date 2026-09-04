from servicios.restaurante import Restaurante


def mostrar_productos(restaurante):
    print("\n--- PRODUCTOS ---")

    for producto in restaurante.productos:
        print(producto)


def mostrar_usuarios(restaurante):
    print("\n--- USUARIOS ---")

    for usuario in restaurante.usuarios:
        print(usuario)


def buscar_producto(restaurante):
    codigo = input("\nIngrese el código del producto: ")

    producto = restaurante.buscar_producto(codigo)

    if producto:
        print("\nProducto encontrado:")
        print(producto)
    else:
        print("\nProducto no encontrado.")


def buscar_usuario(restaurante):
    identificacion = input("\nIngrese la identificación del usuario: ")

    usuario = restaurante.buscar_usuario(identificacion)

    if usuario:
        print("\nUsuario encontrado:")
        print(usuario)
    else:
        print("\nUsuario no encontrado.")


def consultar_ventas(restaurante):
    identificacion = input("\nIngrese la identificación del usuario: ")

    ventas = restaurante.ventas_por_usuario(identificacion)

    if ventas:
        print("\nVentas del usuario:")

        for venta in ventas:
            print(venta)
    else:
        print("\nNo se encontraron ventas para este usuario.")


def registrar_venta(restaurante):
    identificacion = input("\nIngrese la identificación del usuario: ")
    codigo = input("Ingrese el código del producto: ")

    try:
        cantidad = int(input("Ingrese la cantidad: "))
    except ValueError:
        print("\nLa cantidad debe ser un número entero.")
        return

    exito, mensaje = restaurante.realizar_venta(
        identificacion,
        codigo,
        cantidad
    )

    print(f"\n{mensaje}")

    if exito:
        producto = restaurante.buscar_producto(codigo)
        print(f"Stock actualizado: {producto.stock}")


def main():
    restaurante = Restaurante()

    restaurante.cargar_datos()

    while True:
        print("\n==============================")
        print("       RESTAURANTE APP")
        print("==============================")
        print("1. Mostrar productos")
        print("2. Mostrar usuarios")
        print("3. Buscar producto")
        print("4. Buscar usuario")
        print("5. Consultar ventas por usuario")
        print("6. Registrar venta")
        print("7. Guardar datos")
        print("8. Salir")

        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            mostrar_productos(restaurante)

        elif opcion == "2":
            mostrar_usuarios(restaurante)

        elif opcion == "3":
            buscar_producto(restaurante)

        elif opcion == "4":
            buscar_usuario(restaurante)

        elif opcion == "5":
            consultar_ventas(restaurante)

        elif opcion == "6":
            registrar_venta(restaurante)

        elif opcion == "7":
            restaurante.guardar_datos()
            print("\nDatos guardados correctamente.")

        elif opcion == "8":
            restaurante.guardar_datos()
            print("\nDatos guardados. ¡Hasta luego!")
            break

        else:
            print("\nOpción no válida.")


if __name__ == "__main__":
    main()