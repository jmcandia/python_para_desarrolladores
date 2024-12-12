class Producto:
    """
    Clase que representa un producto en el inventario
    """

    def __init__(self, nombre, cantidad, precio, id=None):
        """
        Constructor de la clase Producto

        @param nombre (str): Nombre del producto
        @param cantidad (int): Cantidad de unidades del producto
        """
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        """
        Método para representar el objeto como un string
        """
        return f"[{self.id}] {self.nombre} - Cantidad: {self.cantidad}, Precio: ${self.precio:.2f}"
