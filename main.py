import asyncio

from models.base_de_datos import BaseDeDatos
from models.inventario import Inventario
from models.producto import Producto


# Función principal
async def main():
    """
    Función principal del programa
    """
    bdd = BaseDeDatos()
    inventario = Inventario(bdd)

    while True:
        print("\n--- Menú Principal ---")
        print("1. Añadir producto")
        print("2. Mostrar inventario")
        print("3. Buscar producto por ID")
        print("4. Buscar producto por nombre")
        print("5. Calcular valor total del inventario")
        print("6. Salir")

        opcion = input("Seleccione una opción (1-6): ")

        if opcion == "1":
            nombre = input("Ingrese el nombre del producto: ")
            cantidad = int(input("Ingrese la cantidad: "))
            precio = float(input("Ingrese el precio: "))
            producto = Producto(nombre, cantidad, precio)
            inventario.añadir_producto(producto)

        elif opcion == "2":
            productos = inventario.mostrar_inventario()
            if not productos:
                print("Inventario vacío.")

            for producto in productos:
                print(producto)

        elif opcion == "3":
            id = int(input("Ingrese el ID del producto a buscar: "))
            producto = inventario.buscar_producto_por_id(id)
            if not producto:
                print("Producto no encontrado.")
                continue
            print(producto)

        elif opcion == "4":
            nombre = input("Ingrese el nombre del producto a buscar: ")
            productos = inventario.buscar_producto_por_nombre(nombre)
            if not productos:
                print("Producto(s) no encontrado(s).")
                continue

            for producto in productos:
                print(producto)

        elif opcion == "5":
            total = await inventario.calcular_valor_total()
            print(f"El valor total del inventario es: ${total:.2f}")

        elif opcion == "6":
            print("¡Gracias por usar el sistema de inventario!")
            bdd.cerrar_conexion()
            break

        else:
            print("Opción no válida. Intente de nuevo.")

# Ejecutar la función principal
if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nPrograma terminado por el usuario.")
        exit(0)
