import sqlite3


class BaseDeDatos:
    """
    Clase que administra la base de datos.
    """

    def __init__(self, db_name="inventario.db"):
        """
        Constructor de la clase AdministradorDB.
        """
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def ejecutar_consulta(self, consulta: str, parametros: tuple = ()):
        """
        Ejecuta una consulta en la base de datos.

        @param consulta (str): consulta a ejecutar.
        @param parametros (tuple): Parámetros a pasar a la consulta.
        """
        self.cursor.execute(consulta, parametros)
        self.conn.commit()

    def obtener_resultados(self, consulta, parametros=()):
        """
        Devuelve todos los registros de la base de datos.

        @param consulta (str): Consulta a ejecutar.
        @param parametros (tuple): Parámetros a pasar a la consulta.
        @return (list): Lista de registros.
        """
        self.cursor.execute(consulta, parametros)
        return self.cursor.fetchall()

    def cerrar_conexion(self):
        """
        Cierra la conexión con la base de datos.
        """
        self.conn.close()
        print("Conexión cerrada.")
