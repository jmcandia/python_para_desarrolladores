import asyncio
import sqlite3
from functools import reduce

from utils.decorators import registrar_operacion

from .base_de_datos import BaseDeDatos
from .producto import Producto


class Inventario:
    """
    Clase que representa el inventario de productos.
    """

    def __init__(self, bdd):
        """
        Constructor de la clase Inventario.

        @param db (BaseDeDatos): Instancia de la clase BaseDeDatos.
        """
        # Conexión y creación de tabla
        self.bdd = bdd
        self._crear_tabla()

    def _crear_tabla(self):
        """
        Crea la tabla 'productos' en la base de datos.
        """
        self.bdd.ejecutar_consulta('''
            CREATE TABLE IF NOT EXISTS productos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                cantidad INTEGER NOT NULL,
                precio REAL NOT NULL
            )
        ''')

    @registrar_operacion
    def añadir_producto(self, producto):
        """
        Añade un producto al inventario.

        @param producto (Producto): Instancia de la clase Producto a añadir al inventario.
        """
        self.bdd.ejecutar_consulta(
            "INSERT INTO productos (nombre, cantidad, precio) VALUES (?, ?, ?)",
            (producto.nombre, producto.cantidad, producto.precio)
        )
        print(f"Producto '{producto.nombre}' añadido al inventario.")

    def actualizar_producto(self, producto):
        """
        Actualiza un producto en el inventario.

        @param producto (Producto): Instancia de la clase Producto a actualizar.
        """
        self.bdd.ejecutar_consulta(
            "UPDATE productos SET nombre = ?, cantidad = ?, precio = ? WHERE id = ?",
            (producto.nombre, producto.cantidad, producto.precio, producto.id)
        )
        print(f"Producto '{producto.nombre}' actualizado.")

    @registrar_operacion
    def mostrar_inventario(self):
        """
        Muestra todos los productos del inventario.
        """
        productos_db = self.bdd.obtener_resultados("SELECT * FROM productos")
        return [Producto(producto[1], producto[2], producto[3], producto[0]) for producto in (productos_db or [])]

    @registrar_operacion
    def buscar_producto_por_nombre(self, nombre):
        """
        Busca productos por nombre.

        @param nombre (str): Nombre del producto a buscar.
        @return (list): Lista de instancias de la clase Producto que coinciden con el nombre.
        """
        productos_db = self.bdd.obtener_resultados("SELECT * FROM productos WHERE nombre LIKE ?",
                                                   (f"%{nombre}%",))
        # Si no se encontraron productos, retornar una lista vacía
        if not productos_db:
            return []
        # Crear instancias de la clase Producto con los productos encontrados
        productos_encontrados = [
            Producto(producto[1], producto[2], producto[3], producto[0]) for producto in productos_db]
        return productos_encontrados or []

    @registrar_operacion
    def buscar_producto_por_id(self, id):
        """
        Busca un producto por ID.

        @param id (int): ID del producto a buscar.
        @return (Producto): Instancia de la clase Producto que coincide con el ID.
        """
        productos_db = self.bdd.obtener_resultados(
            "SELECT * FROM productos WHERE id = ?", (id,))
        if not productos_db:
            return None
        producto = Producto(nombre=productos_db[0][1],
                            cantidad=productos_db[0][2],
                            precio=productos_db[0][3],
                            id=productos_db[0][0])
        return producto

    @registrar_operacion
    async def calcular_valor_total(self):
        """
        Calcula el valor total del inventario de forma asíncrona.

        @return (float): Valor total del inventario.
        """
        print("Calculando el valor total del inventario...")
        await asyncio.sleep(1)
        productos_db = self.bdd.obtener_resultados(
            "SELECT nombre, cantidad, precio FROM productos")
        total = reduce(lambda acc, p: acc + p[1] * p[2], productos_db, 0)
        return total
