def registrar_operacion(func):
    """
    Decorador para registrar las operaciones realizadas en la base de datos.
    """
    def envoltura(*args, **kwargs):
        print(f"\nEjecutando operación: {func.__name__}")
        resultado = func(*args, **kwargs)
        print("Operación completada.\n")
        return resultado
    return envoltura
