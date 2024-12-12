# Python para Desarrolladores Experimentados: Una Guía Integral

## Tabla de Contenidos

- [Python para Desarrolladores Experimentados: Una Guía Integral](#python-para-desarrolladores-experimentados-una-guía-integral)
  - [Tabla de Contenidos](#tabla-de-contenidos)
  - [Introducción](#introducción)
    - [¿Por qué Python?](#por-qué-python)
    - [Comparación con Otros Lenguajes](#comparación-con-otros-lenguajes)
    - [Filosofía Pythonic: El Zen de Python](#filosofía-pythonic-el-zen-de-python)
    - [Buenas Prácticas de Programación](#buenas-prácticas-de-programación)
  - [Módulo 1: Fundamentos de Python](#módulo-1-fundamentos-de-python)
    - [Sintaxis Básica](#sintaxis-básica)
    - [Tipos de Datos](#tipos-de-datos)
    - [Tipos de Datos Compuestos](#tipos-de-datos-compuestos)
    - [Operadores y Expresiones](#operadores-y-expresiones)
      - [Operadores Aritméticos](#operadores-aritméticos)
      - [Operadores de Comparación](#operadores-de-comparación)
      - [Operadores Lógicos](#operadores-lógicos)
      - [Operadores de Asignación](#operadores-de-asignación)
      - [Operadores de Identidad](#operadores-de-identidad)
      - [Operadores de Pertenencia](#operadores-de-pertenencia)
    - [Estructuras de Control](#estructuras-de-control)
      - [Condicionales (`if`, `elif`, `else`)](#condicionales-if-elif-else)
      - [Bucles (`for`, `while`)](#bucles-for-while)
      - [Interrupciones (`break`, `continue`)](#interrupciones-break-continue)
      - [For/Else y While/Else](#forelse-y-whileelse)
      - [Comprensiones de Listas y Generadores](#comprensiones-de-listas-y-generadores)
    - [Entrada y Salida](#entrada-y-salida)
      - [Entrada Estándar](#entrada-estándar)
      - [Salida Estándar](#salida-estándar)
      - [Archivos](#archivos)
    - [Bibliotecas y Módulos](#bibliotecas-y-módulos)
      - [Biblioteca Estándar](#biblioteca-estándar)
      - [Bibliotecas Externas](#bibliotecas-externas)
    - [Funciones y Módulos](#funciones-y-módulos)
      - [Funciones](#funciones)
      - [Módulos](#módulos)
      - [Alcance de las Variables](#alcance-de-las-variables)
    - [Excepciones y Manejo de Errores](#excepciones-y-manejo-de-errores)
  - [Módulo 2: Programación Avanzada en Python](#módulo-2-programación-avanzada-en-python)
    - [Programación Orientada a Objetos](#programación-orientada-a-objetos)
      - [Clases y Objetos](#clases-y-objetos)
      - [Herencia y Polimorfismo](#herencia-y-polimorfismo)
    - [Programación Funcional](#programación-funcional)
      - [Funciones de Orden Superior](#funciones-de-orden-superior)
      - [Funciones Lambda](#funciones-lambda)
      - [Comprensiones de Conjuntos y Diccionarios](#comprensiones-de-conjuntos-y-diccionarios)
      - [Decoradores](#decoradores)
    - [Programación Asíncrona](#programación-asíncrona)
      - [Hilos (`threading`)](#hilos-threading)
      - [Procesos (`multiprocessing`)](#procesos-multiprocessing)
      - [Corrutinas (`asyncio`)](#corrutinas-asyncio)
    - [Programación Orientada a Eventos](#programación-orientada-a-eventos)
      - [`tkinter`](#tkinter)
      - [`asyncio`](#asyncio)
      - [`PyQt`](#pyqt)
  - [Módulo 3: Acceso a Bases de Datos con Python](#módulo-3-acceso-a-bases-de-datos-con-python)
    - [Bases de Datos Relacionales](#bases-de-datos-relacionales)
      - [`sqlite3`](#sqlite3)
      - [`MySQLdb`](#mysqldb)
      - [`psycopg2`](#psycopg2)
      - [`SQLAlchemy`](#sqlalchemy)
    - [Bases de Datos No Relacionales](#bases-de-datos-no-relacionales)
      - [`pymongo`](#pymongo)
      - [`redis-py`](#redis-py)
      - [`google-cloud-bigquery`](#google-cloud-bigquery)

## Introducción

Python es un lenguaje de programación de alto nivel, interpretado y de propósito general. Fue creado por Guido van Rossum en 1991 y actualmente es mantenido por la Python Software Foundation. Python es conocido por su sintaxis clara y legible, y su versatilidad, ya que permite desarrollar aplicaciones de todo tipo, desde scripts sencillos hasta aplicaciones web complejas.

Para desarrolladores experimentados que provienen de otros lenguajes, esta guía ofrece una perspectiva técnica y pragmática de Python, destacando sus características únicas y filosofía de diseño.

### ¿Por qué Python?

Python surge como un lenguaje diseñado para resolver problemas de manera elegante y eficiente. A diferencia de otros lenguajes que priorizan la verbosidad o el rendimiento puro, Python se centra en la legibilidad y la productividad del desarrollador.

Dentro de las razones por las que Python es un lenguaje popular y ampliamente utilizado se encuentran:

- **Legibilidad:** El código Python se lee casi como texto plano en inglés.
- **Simplicidad:** Python fomenta la simplicidad y la claridad en el diseño del código.
- **Versatilidad** Ideal para:
  - Desarrollo web
  - Ciencia de datos
  - Inteligencia artificial
  - Automatización
  - Scripting

### Comparación con Otros Lenguajes

| **Característica**           | **Python**                                 | **C/C++**                           | **C#**                                | **Java**                                 | **PHP**                            |
|------------------------------|--------------------------------------------|-------------------------------------|---------------------------------------|------------------------------------------|------------------------------------|
| **Tipado**                   | Dinámico y fuerte                          | Estático y fuerte                   | Estático y fuerte                     | Estático y fuerte                        | Dinámico y débil                   |
| **Declaración de variables** | Implícita (`x = 5`)                        | Explícita (`int x = 5;`)            | Explícita (`int x = 5;`)              | Explícita (`int x = 5;`)                 | Implícita (`$x = 5;`)              |
| **Gestión de memoria**       | Automática (recolección de basura)         | Manual (C) / Automática (C++)       | Automática (GC - Garbage Collector)   | Automática (GC - Garbage Collector)      | Automática                         |
| **Sintaxis**                 | Simple, basada en indentación              | Compleja, con llaves `{}`           | Verbosa, con llaves `{}`              | Verbosa, con llaves `{}`                 | Mixta, basada en `{}` y pragmática |
| **Paradigma**                | Multiparadigma: procedural, OOP, funcional | Procedural, OOP (en C++)            | OOP (Orientado a Objetos)             | OOP                                      | Procedural, OOP                    |
| **Manejo de excepciones**    | `try` / `except`                           | `try` / `catch`                     | `try` / `catch`                       | `try` / `catch`                          | `try` / `catch`                    |
| **Ejecución**                | Interpretado (JIT con PyPy)                | Compilado                           | Compilado a IL (Intermediate Language)| Compilado a bytecode (JVM)               | Interpretado (Zend Engine)         |
| **Velocidad**                | Moderada (más lenta que C/C++)             | Muy alta                            | Alta                                  | Alta                                     | Moderada                           |
| **Portabilidad**             | Muy alta                                   | Media (depende del compilador)      | Alta (con .NET Core)                  | Alta (JVM)                               | Alta                               |
| **Soporte de librerías**     | Extenso (estándar y terceros: PyPI)        | Extenso (pero limitado en C)        | Extenso (paquetes .NET)               | Extenso (bibliotecas estándar y externas)| Extenso (muchas extensiones)       |
| **Aplicaciones comunes**     | Web, Data Science, IA, Scripts, Backend    | Sistemas, drivers, aplicaciones     | Aplicaciones empresariales, juegos    | Aplicaciones empresariales, Android      | Desarrollo web                     |
| **Curva de aprendizaje**     | Baja (sintaxis simple y amigable)          | Alta (especialmente en C)           | Media                                 | Media                                    | Baja                               |

```python
# Ejemplo de código Python
def greet(name):
    print(f'Hello, {name}!')

greet('Alice')
```

```csharp
// Ejemplo de código C#
using System;

class Program
{
    static void Main()
    {
        Greet("Alice");
    }

    static void Greet(string name)
    {
        Console.WriteLine($"Hello, {name}!");
    }
}
```

```java
// Ejemplo de código Java
public class Main {
    public static void main(String[] args) {
        greet("Alice");
    }

    static void greet(String name) {
        System.out.println("Hello, " + name + "!");
    }
}
```

```cpp
// Ejemplo de código C++
#include <iostream>
#include <string>

void greet(const std::string& name) {
    std::cout << "Hello, " << name << "!" << std::endl;
}

int main() {
    greet("Alice");
    return 0;
}
```

```php
<?php
// Ejemplo de código PHP
function greet($name) {
    echo "Hello, $name!";
}

greet('Alice');
?>
```

### Filosofía Pythonic: El Zen de Python

Python tiene una filosofía de diseño que se refleja en el [Zen de Python](https://peps.python.org/pep-0020/), un conjunto de principios que guían el desarrollo del lenguaje. Algunos de los principios más importantes son:

1. **Hermoso es mejor que feo**

    Python fomenta el uso de una sintaxis clara y legible, que sea fácil de entender y mantener. La belleza del código es importante, ya que facilita la colaboración y el mantenimiento del software.

    ```python
    # No Pythonic
    def f(x): return x**2

    # Pythonic
    def square(x):
        return x**2
    ```

2. **Explícito es mejor que implícito**

    Python favorece la claridad y la transparencia en el código, evitando la ambigüedad y la confusión. Es importante que el código sea explícito en lugar de depender de suposiciones o inferencias.

    ```python
    # No Pythonic
    def process(x):
        return x if x else []

    # Pythonic
    def process(x=None):
        return x or []
    ```

   En el ejemplo anterior, la función `process` devuelve una lista vacía si el argumento `x` es `None` o `False`. En la primera versión, se utiliza una declaración `if` para comprobar si `x` es verdadero, lo cual es menos claro y más propenso a errores. Lo más Pythonic es utilizar el operador `or` para devolver `x` si es verdadero, o una lista vacía si es falso.

   ```python
    # No Pythonic
    def process(*args):
        x, y = args
        return dict(**locals())
    
    # Pythonic
    def process(x, y):
        return {'x': x, 'y': y}
   ```

   En este otro ejemplo, la función `process` recibe dos argumentos y devuelve un diccionario con los nombres y valores de los argumentos. En la primera versión, se utilizan argumentos variables y la función `locals()` para obtener los nombres y valores de las variables definidas dentro del scope de la función, lo cual es menos claro y más propenso a errores. Lo más Pythonic es definir explícitamente los argumentos de la función y devolver un diccionario con los nombres y valores de los argumentos.

3. **Simple es mejor que complejo**

    Python fomenta la simplicidad en el diseño y la implementación del código. Es preferible utilizar soluciones simples y directas en lugar de complicar innecesariamente el código.

    ```python
    # No Pythonic
    def is_even(number):
        if number % 2 == 0:
            return True
        else:
            return False

    # Pythonic
    def is_even(number):
        return number % 2 == 0
    ```

    En este ejemplo, la función `is_even` verifica si un número es par. En la primera versión, se utiliza una declaración `if` para comprobar si el número es par y devolver `True` o `False` en consecuencia. En la segunda versión, se utiliza una expresión booleana para devolver directamente el resultado de la comparación, lo cual es más simple y claro.

4. **Complejo es mejor que complicado**

    Aunque Python fomenta la simplicidad, también reconoce que hay problemas que son inherentemente complejos y requieren soluciones complejas. Es importante distinguir entre la complejidad necesaria para resolver un problema y la complicación innecesaria que dificulta la comprensión y el mantenimiento del código.

    ```python
    # No Pythonic
    def fibonacci(n):
        if n <= 0:
            return []
        elif n == 1:
            return [0]
        elif n == 2:
            return [0, 1]
        else:
            fib = [0, 1]
            for i in range(2, n):
                fib.append(fib[i-1] + fib[i-2])
            return fib

    # Pythonic
    def fibonacci(n):
        fib = [0, 1]
        while len(fib) < n:
            fib.append(fib[-1] + fib[-2])
        return fib[:n]
    ```

    En este ejemplo, la función `fibonacci` genera una secuencia de Fibonacci de longitud `n`. En la primera versión, se utilizan múltiples declaraciones `if` para manejar los casos base y un bucle `for` para generar la secuencia. En la segunda versión, se utiliza un bucle `while` para generar la secuencia de Fibonacci de forma más eficiente y concisa.

5. **Plano es mejor que anidado**

    Python fomenta la estructuración plana del código, evitando la anidación excesiva de bloques de código. Es preferible utilizar una estructura de control lineal en lugar de anidar múltiples bloques de código.

    ```python
    # No Pythonic
    def process_data(data):
        if data:
            for item in data:
                if item:
                    for key, value in item.items():
                        if key:
                            print(key, value)

    # Pythonic
    def process_data(data):
        for item in data or []:
            for key, value in item.items() or []:
                if key:
                    print(key, value)
    ```

    En este ejemplo, la función `process_data` procesa una lista de diccionarios y muestra las claves y valores de cada diccionario. En la primera versión, se utilizan múltiples declaraciones `if` y bucles `for` anidados, lo cual dificulta la comprensión del código. En la segunda versión, se utiliza una estructura de control lineal y el operador `or` para simplificar el código y hacerlo más legible.

6. **Legibilidad cuenta**

    Python valora la legibilidad del código como un aspecto fundamental del diseño de software. Es importante que el código sea claro, conciso y fácil de entender para facilitar la colaboración y el mantenimiento del software.

    ```python
    # No Pythonic
    def calculate_total(items):
        total = 0
        for item in items:
            total += item['price'] * item['quantity']
        return total

    # Pythonic
    def calculate_total(items):
        return sum(item['price'] * item['quantity'] for item in items)
    ```

    En este ejemplo, la función `calculate_total` calcula el total de una lista de elementos, donde cada elemento tiene un precio y una cantidad. En la primera versión, se utiliza un bucle `for` para iterar sobre los elementos y calcular el total. En la segunda versión, se utiliza una expresión generadora y la función `sum` para calcular el total de forma más concisa y legible.

7. **Los casos especiales no son lo suficientemente especiales como para romper las reglas**

    Este principio sugiere que las excepciones a las reglas generales no deben ser tan comunes o complejas como para justificar la violación de las reglas generales. Es importante seguir las convenciones y buenas prácticas de programación en la mayoría de los casos, y solo desviarse de ellas cuando sea absolutamente necesario.

    ```python
    # No Pythonic
    def validate_user(username, age, is_admin=False):
        # Caso especial con reglas múltiples e inconsistentes
        if is_admin:
            # Admins tienen reglas diferentes
            if len(username) < 3:
                return False
            if age < 18:
                # Pero espera, ¡este admin es menor de edad!
                # Rompemos nuestra propia regla con una excepción especial
                if username == 'support_system':
                    return True
                return False
        else:
            # Usuarios regulares tienen reglas diferentes
            if len(username) < 5:
                return False
            if age < 18:
                return False
        
        return True

    # Ejemplos de uso
    print(validate_user("john", 17))                          # Falso
    print(validate_user("john", 17, is_admin=True))           # Comportamiento inesperado
    print(validate_user("support_system", 16, is_admin=True)) # Caso especial
    ```

    En este ejemplo, la función `validate_user` verifica si un usuario cumple con ciertas reglas en función de su nombre de usuario, edad y si es un administrador. Sin embargo, la función tiene reglas inconsistentes y casos especiales que complican su lógica y la hacen propensa a errores. Es preferible seguir reglas consistentes y claras en la mayoría de los casos, y manejar los casos especiales de forma explícita y coherente.

    ```python
    # Pythonic
    class UserValidationError(ValueError):
        """Excepción personalizada para errores de validación de usuario"""
        pass

    class UserValidator:
        """
        Validador de usuarios con reglas claras y consistentes

        Args:
            username (str): Nombre de usuario
            age (int): Edad del usuario
            roles (list, optional): Roles especiales del usuario
        
        Raises:
            UserValidationError: Si el usuario no cumple con las reglas de validación

        Returns:
            bool: Verdadero si el usuario cumple con las reglas de validación
        """
        @staticmethod
        def validate_user(username, age, roles=None):
            # Largo de nombre de usuario consistente
            if len(username) < 4:
                raise UserValidationError('El nombre de usuario debe tener al menos 4 caracteres')

            # Edad mínima consistente
            if age < 18:
                # Verificar roles especiales
                allowed_underage_roles = ['support_system', 'junior_account']
                if not roles or not any(role in allowed_underage_roles for role in roles):
                    raise UserValidationError('El usuario debe ser mayor de edad')

            return True
    
    # Ejemplos de uso
    def register_user(username, age, roles=None):
        try:
            UserValidator.validate_user(username, age, roles)
            print(f'Usuario {username} registrado con éxito')
        except UserValidationError as e:
            print(f'Error al registrar usuario: {e}')
    
    register_user("john", 17)                               # Falla
    register_user("support_system", 16, ['support_system']) # Pasa
    register_user("admin_user", 25, ['admin'])              # Pasa
    register_user("support", 25, ['support_system'])        # Pasa
    ```

    En cambio, en esta versión, se define una clase `UserValidator` que encapsula la lógica de validación de usuarios con reglas claras y consistentes. Se utiliza una excepción personalizada `UserValidationError` para manejar los errores de validación de usuarios de forma explícita y coherente. La clase `UserValidator` proporciona un método estático `validate_user` que verifica si un usuario cumple con las reglas de validación y lanza una excepción si no es así. Esto permite manejar los casos especiales de forma más clara y coherente, evitando la complejidad y la confusión de la versión anterior.

8. **Los errores nunca deberían pasar en silencio**

    Python fomenta la detección y el manejo de errores de forma explícita, evitando que los errores pasen desapercibidos o se ignoren. Es importante capturar y manejar los errores de manera adecuada para garantizar la robustez y la fiabilidad del software.

    ```python
    # No Pythonic
    try:
        result = 10 / 0
    except ZeroDivisionError:
        pass

    # Pythonic
    try:
        result = 10 / 0
    except ZeroDivisionError as e:
        print(f'Error: {e}')
    ```

    En este ejemplo, se intenta dividir un número por cero, lo cual genera una excepción `ZeroDivisionError`. En la primera versión, se utiliza una declaración `try` y `except` para capturar la excepción y no hacer nada al respecto. En la segunda versión, se utiliza una declaración `try`, `except` y `as` para capturar la excepción y mostrar un mensaje de error informativo.

9. **Aunque la practicidad le gana a la pureza**

    Este principio sugiere que es preferible priorizar la practicidad y la utilidad sobre la pureza y la perfección. Es importante encontrar un equilibrio entre la elegancia del diseño y la eficacia de la implementación.

    ```python
    # No Pythonic
    def process_data(data):
        if not data:
            return []
        return [item for item in data if item]

    # Pythonic
    def process_data(data):
        return [item for item in data if item]
    ```

    En este ejemplo, la función `process_data` filtra una lista de elementos para eliminar los elementos vacíos. En la primera versión, se utiliza una declaración `if` para verificar si la lista de datos está vacía y devolver una lista vacía en ese caso. En la segunda versión, se utiliza una expresión de lista para filtrar los elementos de la lista directamente, lo cual es más conciso y Pythonic.

### Buenas Prácticas de Programación

1. Convenciones de Nombres

    - **Variables:** Utilizar nombres descriptivos y significativos para las variables, evitando nombres genéricos o abreviaturas confusas.
    - **Funciones:** Utilizar verbos para los nombres de las funciones que describan claramente su propósito y acción.
    - **Clases:** Utilizar sustantivos para los nombres de las clases que representen entidades o conceptos del dominio del problema.
    - **Constantes:** Utilizar mayúsculas y guiones bajos para los nombres de las constantes, separando palabras con guiones bajos.
    - **Módulos:** Utilizar nombres cortos y descriptivos para los módulos, evitando nombres genéricos o ambiguos.

    ```python
    # Variables
    total_price = calculate_total_price(items)

    # Funciones
    def calculate_total_price(items):
        return sum(item['price'] * item['quantity'] for item in items)

    # Clases
    class User:
        def __init__(self, username, email):
            self.username = username
            self.email = email

    # Constantes
    MAX_RETRIES = 3

    # Módulos
    import utils
    ```

2. Comentarios y Documentación

    - **Comentarios:** Utilizar comentarios para explicar el propósito y la lógica del código, evitando comentarios redundantes o innecesarios.
    - **Docstrings:** Utilizar docstrings para documentar las funciones, clases y módulos, describiendo su propósito, parámetros, valores de retorno y comportamiento.

    ```python
    # Comentarios
    # Calcular el total de la lista de elementos
    total_price = calculate_total_price(items)

    # Docstrings
    def calculate_total_price(items):
        """
        Calcula el precio total de una lista de elementos.

        Args:
            items (list): Lista de elementos con precio y cantidad

        Returns:
            float: Precio total de los elementos
        """
        return sum(item['price'] * item['quantity'] for item in items)
    ```

3. Modularidad y Reutilización

    - **Modularidad:** Dividir el código en módulos y funciones pequeñas y cohesivas, que realicen tareas específicas y sean fáciles de entender y mantener.
    - **Reutilización:** Reutilizar el código existente mediante la creación de funciones y clases genéricas y reutilizables, evitando la duplicación de código.

    ```python
    # Modularidad
    import utils

    items = utils.load_items('data.csv')
    total_price = utils.calculate_total_price(items)
    utils.save_total_price(total_price, 'total.txt')

    # Reutilización
    def calculate_total_price(items):
        return sum(item['price'] * item['quantity'] for item in items)

    def save_total_price(total_price, filename):
        with open(filename, 'w') as file:
            file.write(f'Total Price: {total_price}')
    ```

4. Entornos virtuales

    Los entornos virtuales permiten aislar las dependencias de los proyectos y evitar conflictos entre versiones de paquetes. Es recomendable utilizar entornos virtuales para gestionar las dependencias de los proyectos de forma independiente.

    Para crear un entorno virtual, necestamos instalar el paquete virtualenv de Python. Para ello,ejecutamos el siguiente comando:

    ```bash
    pip install virtualenv
    ```

    Luego, podemos crear un entorno virtual con el siguiente comando:

    ```bash
    virtualenv <nombre_entorno>
    ```

    Si estás trabajando en Windows y recibes el siguiente mensaje de error al ejecutar el comando anterior:

    ```cmd
    "virtualenv" no se reconoce como un comando interno o externo,
    programa o archivo por lotes ejecutable.
    ```

    O bien, si recibes el siguiente mensaje de error:

    ```cmd
    virtualenv: The term 'virtualenv' is not recognized as a name of a cmdlet, function, script
    file, or executable program.
    Check the spelling of the name, or if a path was included, verify that the path is correct
    and try again.
    ```

    Entonces debes ejecutar el siguiente comando:

    ```bash
    python -m virtualenv <nombre_entorno>
    ```

    > **Nota:** Recuerda reemplazar `<nombre_entorno>` por el nombre que desees darle a tu entorno virtual. Los nombres más comunes son `venv`, `env` y `myenv`, aunque puedes elegir el que prefieras. Solo asegúrate de que sea un nombre descriptivo y fácil de recordar, y evita espacios y caracteres especiales.

    Para activar el entorno virtual, debes estar en la carpeta raíz del proyecto. El comando para activar el entorno virtual es diferente en Windows y en sistemas Unix (Linux y macOS).

    - En Windows:

    ```cmd
    <nombre_entorno>\Scripts\activate
    ```

    - En Linux/macOS:

    ```bash
    source <nombre_entorno>/bin/activate
    ```

    Para desactivar el entorno virtual, puedes ejecutar el siguiente comando en cualquier sistema operativo:

    ```bash
    deactivate
    ```

5. Gestión de Dependencias

    Para gestionar las dependencias de un proyecto de Python, es recomendable utilizar `pip` y un archivo `requirements.txt` que especifique las dependencias y sus versiones. Esto facilita la instalación de las dependencias en otros entornos y garantiza la reproducibilidad del entorno de desarrollo.

    Para la instalación de las dependencias, se puede utilizar el siguiente comando:

    ```bash
    pip install <dependencia1> <dependencia2> ...
    ```

    > **Nota:** Recuerda reemplazar `<dependencia1>`, `<dependencia2>`, etc., por los nombres de las dependencias que deseas instalar. Puedes especificar las versiones de las dependencias utilizando el formato `nombre==versión`.

    Para generar un archivo `requirements.txt` con las dependencias del proyecto, se puede utilizar el siguiente comando:

    ```bash
    pip freeze > requirements.txt
    ```

    > **Nota:** El comando `pip freeze` muestra una lista de las dependencias instaladas en el entorno virtual, junto con sus versiones. Al redirigir la salida a un archivo `requirements.txt`, se crea un archivo con las dependencias y sus versiones específicas, por ejemplo.
    >
    > ```plaintext
    > # requirements.txt
    > requests==2.26.0
    > pandas==1.3.3
    > numpy==1.21.2
    > ```

    Para instalar las dependencias de un proyecto a partir de un archivo `requirements.txt`, se puede utilizar el siguiente comando:

    ```bash
    pip install -r requirements.txt
    ```

## Módulo 1: Fundamentos de Python

### Sintaxis Básica

La sintaxis de Python se caracteriza por su simplicidad y legibilidad. Algunos aspectos básicos de la sintaxis de Python incluyen:

- **Indentación:** Python utiliza la indentación para definir bloques de código en lugar de llaves o palabras clave como `begin` y `end`. La indentación es fundamental para la estructura del código y debe ser consistente en todo el programa.

    ```python
    # Ejemplo de indentación en Python
    if x > 0:
        print('Número positivo')
    else:
        print('Número no positivo')
    ```

- **Comentarios:** Los comentarios en Python comienzan con el símbolo `#` y se extienden hasta el final de la línea. Los comentarios son útiles para documentar el código y explicar su funcionamiento.

    ```python
    # Ejemplo de comentario en Python
    # Esta función suma dos números y devuelve el resultado
    def sumar(a, b):
        return a + b
    ```

    Los comentarios multilínea se pueden crear utilizando triples comillas simples (`'''`) o triples comillas dobles (`"""`).

    ```python
    # Ejemplo de comentario multilínea en Python
    """
    Esta función calcula el producto de dos números
    y devuelve el resultado
    """
    def multiplicar(a, b):
        return a * b
    ```

### Tipos de Datos

Python es un lenguaje de programación dinámico y fuertemente tipado, lo que significa que las variables tienen un tipo de datos asociado y no es necesario declarar explícitamente el tipo de una variable. Los tipos de datos básicos en Python incluyen:

- **Enteros (`int`):** Números enteros sin punto decimal, por ejemplo, `42`.
- **Flotantes (`float`):** Números con punto decimal, por ejemplo, `3.14`.
- **Booleanos (`bool`):** Valores de verdad (`True` o `False`).
- **Cadenas de texto (`str`):** Secuencias de caracteres, por ejemplo, `'Hola, mundo!'`. Las cadenas de texto se pueden definir con comillas simples (`'`) o dobles (`"`). También se pueden utilizar triples comillas simples (`'''`) o dobles (`"""`) para cadenas multilínea.
- **Listas (`list`):** Secuencias ordenadas de elementos, por ejemplo, `[1, 2, 3]`.
- **Tuplas (`tuple`):** Secuencias ordenadas e inmutables de elementos, por ejemplo, `(1, 2, 3)`.
- **Conjuntos (`set`):** Colecciones no ordenadas de elementos únicos, por ejemplo, `{1, 2, 3}`.
- **Diccionarios (`dict`):** Colecciones de pares clave-valor, por ejemplo, `{'nombre': 'Alice', 'edad': 30}`.
- **Ninguno (`NoneType`):** Valor especial que representa la ausencia de un valor, por ejemplo, `None`.

```python
# Ejemplo de tipos de datos en Python
entero = 42
flotante = 3.14
booleano = True
cadena = 'Hola, mundo!'
cadena_multilinea = '''
Línea 1
Línea 2
Línea 3
'''
lista = [1, 2, 3]
tupla = (1, 2, 3)
conjunto = {1, 2, 3}
diccionario = {'nombre': 'Alice', 'edad': 30}
nulo = None
```

Como ya se mencionó, los tipos de datos en Python son dinámicos, lo que significa que una variable puede cambiar de tipo durante la ejecución del programa. Por ejemplo, una variable que almacena un entero puede cambiar a un flotante si se le asigna un valor con punto decimal.

```python
# Ejemplo de cambio de tipo de datos en Python
valor = 42
print(type(valor))  # <class 'int'>
valor = 3.14
print(type(valor))  # <class 'float'>
```

Los tipos de datos en Python también son fuertemente tipados, lo que significa que las operaciones entre tipos incompatibles generan un error. Por ejemplo, no se puede sumar un entero con una cadena de texto sin convertir explícitamente uno de los valores.

```python
# Ejemplo de error de tipo en Python
numero = 42
texto = '42'
resultado = numero + texto  # TypeError: unsupported operand type(s) for +: 'int' and 'str'
```

Para convertir un valor de un tipo a otro, se pueden utilizar funciones integradas como `int()`, `float()`, `str()`, `list()`, `tuple()`, `set()`, `dict()`, entre otras.

```python
# Ejemplo de conversión de tipo de datos en Python
numero = 42
texto = '42'
resultado = numero + int(texto) # Ahora es posible sumar el entero con el entero convertido desde la cadena
```

Hay que tener en cuenta algunas características especiales de los tipos de datos en Python, como la indexación y el slicing en cadenas, listas y tuplas, y los métodos y operaciones específicos de los conjuntos y diccionarios.

```python
# Ejemplo de indexación y slicing en Python
cadena = 'Hola, mundo!'
print(cadena[0])    # 'H'
print(cadena[2:6])  # 'la, '
print(cadena[::-1]) # '!odnum ,aloH'

# Ejemplo de métodos y operaciones en Python
lista = [1, 2, 3]
lista.append(4)     # Agregar un elemento al final de la lista
lista.insert(1, 5)  # Insertar un elemento en una posición específica
lista.pop()         # Eliminar y devolver el último elemento de la lista
conjunto = {1, 2, 3}
conjunto.add(4)     # Agregar un elemento al conjunto
conjunto.remove(2)  # Eliminar un elemento del conjunto
diccionario = {'nombre': 'Alice', 'edad': 30}
diccionario['apellido'] = 'Smith'  # Agregar un par clave-valor al diccionario
diccionario.pop('edad')           # Eliminar y devolver un valor del diccionario
```

Para las cadenas de texto, Python proporciona una amplia variedad de métodos y operaciones para manipular y formatear cadenas, como `upper()`, `lower()`, `strip()`, `split()`, `join()`, `format()`. También se pueden utilizar secuencias de escape y caracteres especiales en las cadenas, como `\n` para nueva línea, `\t` para tabulación, `\\` para barra invertida, `\'` para comilla simple, `\"` para comilla doble.

```python
# Ejemplo de métodos y operaciones de cadenas en Python
cadena = '¡Hola, mundo!'
print(cadena.upper())        # '¡HOLA, MUNDO!'
print(cadena.split(', '))    # ['¡Hola', 'mundo!']
print(' '.join(['¡Hola', 'mundo!']))  # '¡Hola mundo!'
print('¡Hola, {}!'.format('mundo'))   # '¡Hola, mundo!'
print('¡Hola, {nombre}!'.format(nombre='mundo'))  # '¡Hola, mundo!'
print('¡Hola, mundo!\n¡Adiós, mundo!')  # Salto de línea
```

Python también presenta una alternativa a la función `format()`, y es el uso de f-strings, que permiten incrustar expresiones y variables directamente en las cadenas de texto. Las f-strings se crean anteponiendo una `f` o `F` al inicio de la cadena y utilizando llaves `{}` para incrustar expresiones y variables.

```python
# Ejemplo de f-strings en Python
nombre = 'Alice'
edad = 30
print(f'¡Hola, {nombre}! Tienes {edad} años.')  # '¡Hola, Alice! Tienes 30 años.'
```

Esto también funciona con cadenas multilínea y expresiones más complejas.

```python
# Ejemplo de f-strings con cadenas multilínea y expresiones en Python
nombre = 'Alice'
edad = 30
mensaje = f'''
¡Hola, {nombre}!\n
Tienes {edad} años.\n
El doble de tu edad es {edad * 2}.
'''
print(mensaje)
```

### Tipos de Datos Compuestos

Además de los tipos de datos básicos, Python también proporciona tipos de datos compuestos y estructuras de datos avanzadas, como:

- **Rangos (`range`):** Secuencias inmutables de números enteros, por ejemplo, `range(5)` representa los números del `0` al `4`.
- **Bytes y bytearray:** Secuencias de bytes y arreglos de bytes mutables, respectivamente.
- **Fechas y horas (`datetime`):** Representaciones de fechas y horas, por ejemplo, `datetime.datetime.now()`.
- **Archivos (`file`):** Manipulación de archivos y operaciones de entrada/salida.
- **Funciones (`function`):** Definiciones de funciones y objetos de función.
- **Clases (`class`):** Definiciones de clases y objetos de clase.

```python
# Ejemplo de tipos de datos compuestos en Python
rango = range(5)
bytes = b'hello'
fecha_actual = datetime.datetime.now()
archivo = open('datos.txt', 'r')
```

En Python, los tipos de datos compuestos y estructuras de datos avanzadas se utilizan para representar y manipular datos de forma más compleja y especializada. Estas estructuras proporcionan funcionalidades adicionales y métodos específicos para trabajar con los datos de manera eficiente y efectiva.

### Operadores y Expresiones

Los operadores en Python son símbolos especiales que realizan operaciones sobre valores y variables. Los operadores se clasifican en diferentes categorías, como operadores aritméticos, operadores de comparación, operadores lógicos, operadores de asignación, operadores de identidad, operadores de pertenencia, entre otros.

#### Operadores Aritméticos

Los operadores aritméticos se utilizan para realizar operaciones matemáticas básicas, como suma, resta, multiplicación, división, módulo y potenciación.

| Operador | Descripción       | Ejemplo          | Resultado |
|----------|-------------------|------------------|-----------|
| `+`      | Suma              | `2 + 3`          | `5`       |
| `-`      | Resta             | `5 - 2`          | `3`       |
| `*`      | Multiplicación    | `2 * 3`          | `6`       |
| `/`      | División          | `6 / 3`          | `2.0`     |
| `//`     | División entera   | `7 // 3`         | `2`       |
| `%`      | Módulo            | `7 % 3`          | `1`       |
| `**`     | Potenciación      | `2 ** 3`         | `8`       |

#### Operadores de Comparación

Los operadores de comparación se utilizan para comparar valores y variables, y devuelven un valor booleano (`True` o `False`) que indica si la comparación es verdadera o falsa.

| Operador | Descripción       | Ejemplo          | Resultado |
|----------|-------------------|------------------|-----------|
| `==`     | Igual a           | `2 == 3`         | `False`   |
| `!=`     | Diferente de      | `2 != 3`         | `True`    |
| `>`      | Mayor que         | `3 > 2`          | `True     |
| `<`      | Menor que         | `2 < 3`          | `True`    |
| `>=`     | Mayor o igual que | `3 >= 3`         | `True     |
| `<=`     | Menor o igual que | `2 <= 3`         | `True`    |

#### Operadores Lógicos

Los operadores lógicos se utilizan para combinar expresiones booleanas y realizar operaciones lógicas, como conjunción, disyunción y negación.

| Operador | Descripción       | Ejemplo          | Resultado |
|----------|-------------------|------------------|-----------|
| `and`    | Conjunción        | `True and False` | `False`   |
| `or`     | Disyunción        | `True or False`  | `True`    |
| `not`    | Negación          | `not True`       | `False`   |

#### Operadores de Asignación

Los operadores de asignación se utilizan para asignar valores a variables y actualizar el valor de una variable.

| Operador | Descripción                  | Ejemplo          | Equivalente  |
|----------|------------------------------|------------------|--------------|
| `=`      | Asignación                   | `x = 5`          |              |
| `+=`     | Suma y asignación            | `x += 3`         | `x = x + 3`  |
| `-=`     | Resta y asignación           | `x -= 2`         | `x = x - 2`  |
| `*=`     | Multiplicación y asignación  | `x *= 2`         | `x = x * 2`  |
| `/=`     | División y asignación        | `x /= 2`         | `x = x / 2`  |
| `//=`    | División entera y asignación | `x //= 2`        | `x = x // 2` |
| `%=`     | Módulo y asignación          | `x %= 2`         | `x = x % 2`  |
| `**=`    | Potenciación y asignación    | `x **= 2`        | `x = x ** 2` |

#### Operadores de Identidad

Los operadores de identidad se utilizan para comparar la identidad de objetos, es decir, si dos variables se refieren al mismo objeto en memoria.

| Operador | Descripción       | Ejemplo          | Resultado               |
|----------|-------------------|------------------|-------------------------|
| `is`     | Identidad         | `x is y`         | `True` si `x` es `y`    |
| `is not` | No identidad      | `x is not y`     | `True` si `x` no es `y` |

#### Operadores de Pertenencia

Los operadores de pertenencia se utilizan para verificar si un valor está presente en una secuencia, como una lista, tupla, conjunto o diccionario.

| Operador | Descripción    | Ejemplo          | Resultado                        |
|----------|----------------|------------------|----------------------------------|
| `in`     | Pertenencia    | `x in lista`     | `True` si `x` está en `lista`    |
| `not in` | No pertenencia | `x not in lista` | `True` si `x` no está en `lista` |

### Estructuras de Control

Las estructuras de control en Python se utilizan para controlar el flujo de ejecución del programa y tomar decisiones basadas en condiciones específicas. Algunas de las estructuras de control más comunes en Python son:

#### Condicionales (`if`, `elif`, `else`)

La estructura condicional `if` se utiliza para ejecutar un bloque de código si una condición es verdadera. Se pueden utilizar múltiples bloques `elif` (else if) para comprobar condiciones adicionales, y un bloque `else` para ejecutar un código si ninguna de las condiciones anteriores es verdadera.

```python
# Ejemplo de estructura condicional en Python
x = 42

if x > 0:
    print('Número positivo')
elif x < 0:
    print('Número negativo')
else:
    print('Número cero')
```

#### Bucles (`for`, `while`)

Los bucles `for` se utilizan para iterar sobre una secuencia de elementos, como una lista, tupla, conjunto o rango. Los bucles `while` se utilizan para ejecutar un bloque de código mientras una condición sea verdadera.

```python
# Ejemplo de bucle for en Python
for i in range(5):
    print(i)

# Ejemplo de bucle while en Python
i = 0
while i < 5:
    print(i)
    i += 1
```

#### Interrupciones (`break`, `continue`)

Las instrucciones `break` y `continue` se utilizan para controlar el flujo de ejecución dentro de un bucle. La instrucción `break` se utiliza para salir del bucle por completo, mientras que la instrucción `continue` se utiliza para saltar a la siguiente iteración del bucle.

```python
# Ejemplo de instrucción break en Python
for i in range(10):
    if i == 5:
        break
    print(i)

# Ejemplo de instrucción continue en Python
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)
```

#### For/Else y While/Else

Python permite utilizar la cláusula `else` en combinación con los bucles `for` y `while`. El bloque de código en la cláusula `else` se ejecuta si el bucle se completa sin interrupciones.

```python
# Ejemplo de bucle for/else en Python
for i in range(5):
    print(i)
else:
    print('Bucle completado')

# Ejemplo de bucle while/else en Python
i = 0
while i < 5:
    print(i)
    i += 1
else:
    print('Bucle completado')
```

Si el bucle se interrumpe con una instrucción `break`, el bloque de código en la cláusula `else` no se ejecuta.

```python
# Ejemplo de bucle for/else interrumpido en Python
for i in range(5):
    if i == 3:
        break
    print(i)
else:
    print('Bucle completado')
```

#### Comprensiones de Listas y Generadores

Las comprensiones de listas son una forma concisa y expresiva de crear listas en Python utilizando una sintaxis similar a la notación de conjuntos en matemáticas.

```python
# Ejemplo de comprensión de lista en Python
cuadrados = [x**2 for x in range(5)]
print(cuadrados)  # [0, 1, 4, 9, 16]
```

Las comprensiones de listas pueden incluir condiciones para filtrar los elementos de la lista.

```python
# Ejemplo de comprensión de lista con condición en Python
pares = [x for x in range(10) if x % 2 == 0]
print(pares)  # [0, 2, 4, 6, 8]
```

Las comprensiones de generadores son similares a las comprensiones de listas, pero generan un objeto generador en lugar de una lista. Los generadores son más eficientes en términos de memoria y se utilizan para generar secuencias de elementos de forma perezosa.

```python
# Ejemplo de comprensión de generador en Python
generador = (x**2 for x in range(5))
print(next(generador))  # 0
print(next(generador))  # 1
print(next(generador))  # 4
print(next(generador))  # 9
print(next(generador))  # 16
print(next(generador))  # Lanza la excepción StopIteration
```

Para iterar sobre un generador, se puede utilizar un bucle `for` o la función `next()` para obtener el siguiente elemento del generador.

```python
# Ejemplo de iteración sobre un generador en Python
generador = (x**2 for x in range(5))
for valor in generador:
    print(valor)

# Equivalente a:
generador = (x**2 for x in range(5))
while True:
    try:
        valor = next(generador)
        print(valor)
    except StopIteration:
        break
```

Una forma común de utilizar los generadores es en combinación con funciones como `sum()`, `max()`, `min()`, `list()`, `set()`, `dict()`, entre otras.

```python
# Ejemplo de uso de generadores en Python
generador = (x**2 for x in range(5))
print(sum(generador))  # 30
```

### Entrada y Salida

#### Entrada Estándar

La entrada estándar en Python se refiere a la lectura de datos desde la consola o la terminal. La función `input()` se utiliza para leer una línea de entrada desde la consola y devolverla como una cadena.

```python
# Ejemplo de entrada estándar en Python
nombre = input('Ingrese su nombre: ')
print(f'Hola, {nombre}!')
```

En este ejemplo, la función `input()` se utiliza para solicitar al usuario que ingrese su nombre, y el nombre ingresado se imprime en la consola utilizando la función `print()`.

#### Salida Estándar

La salida estándar en Python se refiere a la escritura de datos en la consola o la terminal. La función `print()` se utiliza para imprimir datos en la consola y puede aceptar múltiples argumentos separados por comas.

```python
# Ejemplo de salida estándar en Python
nombre = 'Alice'
edad = 30
print('Nombre:', nombre, 'Edad:', edad)
```

En este ejemplo, la función `print()` se utiliza para imprimir el nombre y la edad en la consola, separados por comas. Los argumentos de la función `print()` se convierten en cadenas y se concatenan con un espacio en blanco.

#### Archivos

La lectura y escritura de archivos en Python se realiza utilizando la función `open()`, que devuelve un objeto de archivo que se puede utilizar para leer o escribir datos en un archivo.

```python
# Ejemplo de lectura y escritura de archivos en Python
with open('archivo.txt', 'w') as archivo:
    archivo.write('Hola, mundo!')

with open('archivo.txt', 'r') as archivo:
    contenido = archivo.read()

print(contenido)  # 'Hola, mundo!'
```

En este ejemplo, se crea un archivo de texto llamado `archivo.txt` en modo de escritura (`'w'`) y se escribe el texto `'Hola, mundo!'` en el archivo. Luego, se abre el archivo en modo de lectura (`'r'`) y se lee el contenido del archivo en una variable `contenido`.

Python proporciona varios modos de apertura de archivos, como `'r'` para lectura, `'w'` para escritura, `'a'` para agregar, `'b'` para modo binario, `'t'` para modo de texto, entre otros.

### Bibliotecas y Módulos

Python es un lenguaje de programación que cuenta con una amplia variedad de bibliotecas y módulos que proporcionan funcionalidades adicionales y permiten extender las capacidades del lenguaje. Algunas de las bibliotecas y módulos más populares en Python son:

#### Biblioteca Estándar

La biblioteca estándar de Python es un conjunto de módulos y paquetes que se distribuyen con el intérprete de Python y proporcionan funcionalidades esenciales para tareas comunes de programación, como entrada y salida, manipulación de archivos, manejo de excepciones, acceso a la red, procesamiento de datos, entre otros. Algunos de los módulos más utilizados de la biblioteca estándar de Python son:

- `os`: Funciones para interactuar con el sistema operativo.
- `sys`: Funciones y variables relacionadas con el intérprete de Python.
- `math`: Funciones matemáticas y constantes.
- `random`: Generación de números aleatorios.
- `datetime`: Manipulación de fechas y horas.
- `json`: Codificación y decodificación de datos en formato JSON.
- `re`: Expresiones regulares.
- `urllib`: Acceso a recursos en la web.
- `sqlite3`: Interfaz para trabajar con bases de datos SQLite.
- `csv`: Lectura y escritura de archivos CSV.
- `collections`: Tipos de datos especializados como `namedtuple`, `deque`, `Counter`, `defaultdict`.
- `itertools`: Funciones para crear y manipular iteradores.
- `functools`: Funciones de orden superior y herramientas de programación funcional.
- `multiprocessing`: Soporte para la programación concurrente y paralela.
- `threading`: Soporte para la programación concurrente con hilos.
- `socket`: Interfaz para la programación de red.
- `http`: Protocolos y servicios web.
- `unittest`: Marco de pruebas unitarias.
- `logging`: Registro y seguimiento de eventos.
- `argparse`: Análisis de argumentos de línea de comandos.
- `os.path`: Funciones para manipular rutas de archivos y directorios.
- `subprocess`: Creación de procesos secundarios y comunicación con ellos.
- `pickle`: Serialización y deserialización de objetos Python.
- `shutil`: Operaciones de alto nivel en archivos y directorios.
- `tempfile`: Creación de archivos y directorios temporales.
- `timeit`: Medición del tiempo de ejecución de código.
- `profile`: Perfilado de código.
- `cProfile`: Perfilado de código con información detallada.
- `trace`: Seguimiento de la ejecución de código.

La biblioteca estándar de Python es una de las características más poderosas y útiles del lenguaje y proporciona una amplia gama de funcionalidades para tareas comunes de programación.

#### Bibliotecas Externas

Además de la biblioteca estándar, Python cuenta con una amplia variedad de bibliotecas externas que proporcionan funcionalidades especializadas para tareas específicas, como análisis de datos, aprendizaje automático, visualización, desarrollo web, automatización, entre otros. Algunas de las bibliotecas externas más populares en Python son:

- `NumPy`: Biblioteca para computación numérica y manipulación de arreglos.
- `Pandas`: Biblioteca para análisis de datos y manipulación de datos tabulares.
- `Matplotlib`: Biblioteca para visualización de datos en gráficos y figuras.
- `Seaborn`: Biblioteca para visualización de datos estadísticos.
- `Scikit-learn`: Biblioteca para aprendizaje automático y minería de datos.
- `TensorFlow`: Biblioteca para aprendizaje profundo y redes neuronales.
- `PyTorch`: Biblioteca para aprendizaje profundo y redes neuronales.
- `Django`: Marco de desarrollo web de alto nivel.
- `Flask`: Marco de desarrollo web ligero y flexible.
- `Requests`: Biblioteca para realizar solicitudes HTTP.
- `Beautiful Soup`: Biblioteca para extraer datos de páginas web.
- `Selenium`: Biblioteca para automatizar navegadores web.
- `OpenCV`: Biblioteca para visión por computadora y procesamiento de imágenes.
- `Pygame`: Biblioteca para desarrollo de juegos.
- `PyQt`: Enlace de Python para la biblioteca Qt.
- `Twisted`: Marco para programación de red.
- `Scrapy`: Marco para extracción de datos web.
- `NLTK`: Kit de herramientas de lenguaje natural.
- `Spacy`: Biblioteca para procesamiento avanzado de lenguaje natural.
- `FastAPI`: Marco para la creación de API web de alto rendimiento.
- `Pytest`: Marco de pruebas para pruebas unitarias y de integración.
- `Sphinx`: Generador de documentación para proyectos de Python.

Estas son solo algunas de las bibliotecas externas más populares en Python, y existen muchas otras bibliotecas especializadas que proporcionan funcionalidades adicionales y permiten extender las capacidades del lenguaje.

### Funciones y Módulos

#### Funciones

Las funciones en Python son bloques de código reutilizables que realizan una tarea específica y pueden aceptar argumentos y devolver un valor. Las funciones se definen utilizando la palabra clave `def`, seguida del nombre de la función y los parámetros entre paréntesis.

```python
# Ejemplo de función en Python
def saludar(nombre):
    return f'Hola, {nombre}!'
```

Los parámetros de una función pueden tener valores predeterminados, lo que permite llamar a la función sin proporcionar valores para esos parámetros.

```python
# Ejemplo de función con parámetros predeterminados en Python
def saludar(nombre='mundo'):
    return f'Hola, {nombre}!'

print(saludar())      # 'Hola, mundo!'
print(saludar('Alice'))  # 'Hola, Alice!'
```

Las funciones pueden aceptar un número variable de argumentos utilizando `*args` y `**kwargs` para capturar argumentos posicionales y argumentos de palabras clave, respectivamente.

```python
# Ejemplo de función con argumentos variables en Python
def sumar(*args):
    return sum(args)

def imprimir_valores(**kwargs):
    for clave, valor in kwargs.items():
        print(f'{clave}: {valor}')

print(sumar(1, 2, 3, 4, 5))  # 15
imprimir_valores(a=1, b=2, c=3)  # a: 1, b: 2, c: 3
```

Veamos un ejemplo de una función que acepta argumentos mandatorios, opcionales y variables.

```python
# Ejemplo de función con argumentos mandatorios, opcionales y variables en Python
def procesar_datos(mandatorio, opcional='opcional', *args, **kwargs):
    print(f'Mandatorio: {mandatorio}')
    print(f'Opcional: {opcional}')
    print(f'Argumentos: {args}')
    print(f'Palabras clave: {kwargs}')
    
procesar_datos('mandatorio')
procesar_datos('mandatorio', 'nuevo opcional', 1, 2, 3, a=1, b=2, c=3)
```

El primer resultado de la ejecución de este código sería:

```plaintext
Mandatorio: mandatorio
Opcional: opcional
Argumentos: ()
Palabras clave: {}
```

Y el segundo resultado sería:

```plaintext
Mandatorio: mandatorio
Opcional: nuevo opcional
Argumentos: (1, 2, 3)
Palabras clave: {'a': 1, 'b': 2, 'c': 3}
```

#### Módulos

Los módulos en Python son archivos que contienen definiciones de funciones, clases y variables que se pueden importar y utilizar en otros programas. Los módulos permiten organizar y reutilizar el código de forma eficiente y modular.

```python
# Ejemplo de módulo en Python
# módulo.py
def saludar(nombre):
    return f'Hola, {nombre}!'
```

Para importar un módulo en Python, se utiliza la palabra clave `import`, seguida del nombre del módulo.

```python
# Ejemplo de importación de módulo en Python
import modulo

print(modulo.saludar('Alice'))  # 'Hola, Alice!'
```

También se pueden importar funciones específicas de un módulo utilizando la sintaxis `from ... import ...`.

```python
# Ejemplo de importación de función específica en Python
from modulo import saludar

print(saludar('Alice'))  # 'Hola, Alice!'
```

Los módulos en Python pueden contener variables, funciones, clases y otros módulos, y se pueden organizar en paquetes para estructurar y modularizar el código de forma más eficiente.

```python
# Ejemplo de módulo con variables, funciones y clases en Python
# modulo.py
nombre = 'Alice'

def saludar(nombre):
    return f'Hola, {nombre}!'
```

```python
# Ejemplo de uso de módulo con variables, funciones y clases en Python
import modulo

print(modulo.nombre)          # 'Alice'
print(modulo.saludar('Bob'))  # 'Hola, Bob!'
```

#### Alcance de las Variables

El alcance de una variable en Python se refiere a la región del código donde la variable es accesible y puede ser utilizada. Python utiliza reglas de alcance basadas en bloques, lo que significa que una variable definida dentro de un bloque de código solo es accesible dentro de ese bloque.

```python
# Ejemplo de alcance de variables en Python
def funcion():
    variable_local = 'local'
    print(variable_local)

funcion()
print(variable_local)  # NameError: name 'variable_local' is not defined
```

Las variables globales son aquellas definidas fuera de cualquier función o bloque de código y son accesibles desde cualquier parte del programa. Para modificar una variable global dentro de una función, se debe utilizar la palabra clave `global`.

```python
# Ejemplo de variable global en Python
variable_global = 'global'

def funcion():
    global variable_global
    variable_global = 'modificado'

funcion()
print(variable_global)  # 'modificado'
```

Las variables en los módulos de Python son globales por defecto y pueden ser accedidas y modificadas desde cualquier parte del programa. Sin embargo, es importante tener en cuenta las reglas de alcance y evitar el uso excesivo de variables globales para mantener un código claro y mantenible.

### Excepciones y Manejo de Errores

Las excepciones en Python son eventos que interrumpen el flujo normal de ejecución del programa y pueden ser causadas por errores de sintaxis, errores de tiempo de ejecución o condiciones excepcionales. Python proporciona una forma de manejar las excepciones utilizando bloques `try`, `except`, `else` y `finally`.

```python
# Ejemplo de manejo de excepciones en Python
try:
    resultado = 10 / 0
except ZeroDivisionError:
    print('Error: división por cero')
else:
    print('Resultado:', resultado)
finally:
    print('Fin del bloque try-except')
```

El bloque `try` se utiliza para envolver el código que puede generar una excepción. Si se produce una excepción, el bloque `except` se ejecuta y se captura la excepción específica. El bloque `else` se ejecuta si no se produce ninguna excepción, y el bloque `finally` se ejecuta siempre, independientemente de si se produce una excepción o no.

Python proporciona una amplia variedad de excepciones integradas, como `ZeroDivisionError`, `ValueError`, `TypeError`, `IndexError`, `KeyError`, `FileNotFoundError`, entre otras. También es posible definir excepciones personalizadas mediante la creación de clases que hereden de la clase base `Exception`.

```python
# Ejemplo de excepción personalizada en Python
class MiError(Exception):
    pass

try:
    raise MiError('Mensaje de error personalizado')
except MiError as error:
    print('Error:', error)
```

Pyhton también permite capturar múltiples excepciones en un solo bloque `except` utilizando tuplas de excepciones.

```python
# Ejemplo de captura de múltiples excepciones en Python
try:
    raise ValueError('Mensaje de error')
except ValueError as error:
    print('Error de valor:', error)
except TypeError as error:
    print('Error de tipo:', error)
```

Las excepciones en Python se pueden propagar a través de múltiples niveles de llamadas de funciones y se pueden capturar y manejar en diferentes partes del programa. Es importante utilizar el manejo de excepciones de forma adecuada para garantizar la robustez y la fiabilidad del código.

```python
# Ejemplo de propagación de excepciones en Python
def funcion():
    raise ValueError('Mensaje de error')

try:
    funcion()
except ValueError as error:
    print('Error:', error)
```

## Módulo 2: Programación Avanzada en Python

### Programación Orientada a Objetos

La programación orientada a objetos (POO) es un paradigma de programación que se basa en el concepto de "objetos" y permite modelar entidades del mundo real como clases y objetos. Python es un lenguaje de programación orientado a objetos que proporciona soporte para la definición de clases, la creación de objetos y la herencia de clases.

#### Clases y Objetos

Una clase en Python es una plantilla que define las propiedades y el comportamiento de un objeto. Los objetos son instancias de una clase y pueden tener atributos (variables) y métodos (funciones) asociados.

```python
# Ejemplo de clase y objeto en Python
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        return f'Hola, mi nombre es {self.nombre} y tengo {self.edad} años.'

alice = Persona('Alice', 30)
print(alice.saludar())  # 'Hola, mi nombre es Alice y tengo 30 años.'
```

La función `__init__` es un método especial que se llama cuando se crea un objeto de la clase y se utiliza para inicializar los atributos del objeto. Los métodos de una clase deben tener un parámetro `self` que hace referencia al objeto actual y permite acceder a sus atributos y métodos.

```python
# Ejemplo de métodos en una clase en Python
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        return f'Hola, mi nombre es {self.nombre} y tengo {self.edad} años.'

    def cumpleaños(self):
        self.edad += 1
    
    def __str__(self):
        return f'Persona(nombre={self.nombre}, edad={self.edad})'

alice = Persona('Alice', 30)
print(alice.saludar())  # 'Hola, mi nombre es Alice y tengo 30 años.'
alice.cumpleaños()
print(alice.saludar())  # 'Hola, mi nombre es Alice y tengo 31 años.'
print(alice)  # 'Persona(nombre=Alice, edad=31)'
```

Los métodos especiales en Python, como `__init__`, `__str__`, `__repr__`, `__eq__`, `__lt__`, `__gt__`, entre otros, permiten definir el comportamiento de una clase y proporcionan funcionalidades adicionales, como la representación de un objeto como una cadena, la comparación de objetos, entre otros.

Para acceder a los atributos y métodos de un objeto, se utiliza la notación de punto (`.`) seguida del nombre del atributo o método.

```python
# Ejemplo de acceso a atributos y métodos de un objeto en Python
alice = Persona('Alice', 30)
print(alice.nombre)  # 'Alice'
print(alice.edad)    # 30
print(alice.saludar())  # 'Hola, mi nombre es Alice y tengo
```

Para modificar los atributos de un objeto, se puede acceder directamente a los atributos y asignarles un nuevo valor.

```python
# Ejemplo de modificación de atributos de un objeto en Python
alice = Persona('Alice', 30)
alice.edad = 31
print(alice.edad)  # 31
```

Python ofrece la posibilidad de definir propiedades (`property`) en una clase para controlar el acceso y la modificación de los atributos de un objeto.

```python
# Ejemplo de propiedad en una clase en Python
class Persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        self._nombre = valor

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, valor):
        if valor >= 0:
            self._edad = valor
        else:
            raise ValueError('La edad debe ser un número positivo')

alice = Persona('Alice', 30)
print(alice.nombre)  # 'Alice'
alice.nombre = 'Alice Smith'
print(alice.nombre)  # 'Alice Smith'
print(alice.edad)    # 30
alice.edad = 31
print(alice.edad)    # 31
```

En este ejemplo, la propiedad `nombre` permite acceder y modificar el atributo `_nombre` de un objeto de la clase `Persona`, y la propiedad `edad` realiza una validación para asegurarse de que la edad sea un número positivo.

Los atributos de un objeto en Python pueden ser públicos, protegidos o privados, lo que indica su nivel de visibilidad y accesibilidad. Los atributos públicos pueden ser accedidos y modificados desde cualquier parte del programa, los atributos protegidos solo pueden ser accedidos y modificados desde la clase y las subclases, y los atributos privados solo pueden ser accedidos y modificados desde la clase. Para definir un atributo protegido, se utiliza un guion bajo (`_`) al principio del nombre del atributo, y para definir un atributo privado, se utilizan dos guiones bajos (`__`).

```python
# Ejemplo de atributos públicos, protegidos y privados en Python
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre  # Atributo público
        self._edad = edad      # Atributo protegido
        self.__rut = '12345678-5'  # Atributo privado
    
    def __metodo_privado(self):
        return 'Método privado'

alice = Persona('Alice', 30)
print(alice.nombre)  # 'Alice'
print(alice._edad)   # 30
print(alice.__rut)   # AttributeError: 'Persona' object has no attribute '__rut'
print(alice.__metodo_privado())  # AttributeError: 'Persona' object has no attribute '__metodo_privado'
```

#### Herencia y Polimorfismo

La herencia en Python permite que una clase herede atributos y métodos de otra clase, lo que facilita la reutilización de código y la creación de jerarquías de clases.

```python
# Ejemplo de herencia en Python
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        return f'Hola, mi nombre es {self.nombre} y tengo {self.edad} años.'

class Empleado(Persona):
    def __init__(self, nombre, edad, salario):
        super().__init__(nombre, edad)
        self.salario = salario

    def presentarse(self):
        return f'Hola, soy {self.nombre} y mi salario es {self.salario}.'
```

En este ejemplo, la clase `Empleado` hereda de la clase `Persona` y agrega un nuevo atributo `salario` y un nuevo método `presentarse`. La función `super()` se utiliza para llamar a los métodos de la clase base y se utiliza para inicializar los atributos de la clase base en la clase derivada.

El polimorfismo en Python permite que los objetos de diferentes clases respondan a los mismos métodos de forma diferente. Esto se logra mediante la definición de métodos con el mismo nombre en diferentes clases y la capacidad de llamar a estos métodos en objetos de diferentes clases.

```python
# Ejemplo de polimorfismo en Python
class Perro:
    def sonido(self):
        return 'Guau'
    
class Gato:
    def sonido(self):
        return 'Miau'

def hacer_sonar(animal):
    return animal.sonido()

perro = Perro()
gato = Gato()

print(hacer_sonar(perro))  # 'Guau'
print(hacer_sonar(gato))   # 'Miau'
```

En este ejemplo, las clases `Perro` y `Gato` tienen un método `sonido` que devuelve el sonido característico de cada animal. La función `hacer_sonar` toma un objeto de cualquier clase que tenga un método `sonido` y llama a ese método para obtener el sonido del animal.

La herencia y el polimorfismo son conceptos fundamentales en la programación orientada a objetos y permiten crear jerarquías de clases, reutilizar código y crear interfaces comunes para objetos de diferentes clases.

### Programación Funcional

La programación funcional es un paradigma de programación que se basa en el concepto de funciones puras, inmutabilidad y expresiones lambda. Python es un lenguaje de programación multiparadigma que proporciona soporte para la programación funcional a través de funciones integradas y módulos especializados. Algunas de las características de la programación funcional en Python son:

#### Funciones de Orden Superior

Las funciones de orden superior en Python son aquellas que pueden aceptar funciones como argumentos y devolver funciones como resultado. Las funciones de orden superior permiten la composición de funciones y la creación de funciones más generales y reutilizables.

```python
# Ejemplo de función de orden superior en Python
def aplicar(funcion, valor):
    return funcion(valor)

def cuadrado(x):
    return x**2

print(aplicar(cuadrado, 5))  # 25

def sumar(a, b):
    return a + b

print(aplicar(sumar, (2, 3)))  # 5
```

En este ejemplo, la función `aplicar` es una función de orden superior que toma una función y un valor como argumentos y aplica la función al valor. Esto permite reutilizar la función `aplicar` con diferentes funciones y valores.

#### Funciones Lambda

Las funciones lambda en Python son funciones anónimas y de una sola línea que se definen utilizando la palabra clave `lambda`. Las funciones lambda son útiles para definir funciones simples y expresivas en el lugar donde se necesitan.

```python
# Ejemplo de función lambda en Python
cuadrado = lambda x: x**2
print(cuadrado(5))  # 25

sumar = lambda a, b: a + b
print(sumar(2, 3))  # 5
```

Las funciones lambda se utilizan comúnmente en combinación con funciones de orden superior, como `map()`, `filter()`, `reduce()`, para aplicar operaciones a elementos de una secuencia, filtrar elementos de una secuencia y reducir una secuencia a un solo valor, respectivamente.

```python
# Ejemplo de funciones lambda con funciones de orden superior en Python
numeros = [1, 2, 3, 4, 5]

cuadrados = list(map(lambda x: x**2, numeros))
print(cuadrados)  # [1, 4, 9, 16, 25]

pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares)  # [2, 4]

suma = reduce(lambda a, b: a + b, numeros)
print(suma)  # 15
```

En este ejemplo, la función `map()` se utiliza para aplicar la función lambda `lambda x: x**2` a cada elemento de la lista `numeros`, la función `filter()` se utiliza para filtrar los elementos pares de la lista `numeros`, y la función `reduce()` se utiliza para sumar todos los elementos de la lista `numeros`.

#### Comprensiones de Conjuntos y Diccionarios

Las comprensiones de conjuntos y diccionarios en Python son una forma concisa y expresiva de crear conjuntos y diccionarios utilizando una sintaxis similar a las comprensiones de listas.

```python
# Ejemplo de comprensión de conjunto en Python
numeros = {1, 2, 3, 4, 5}
cuadrados = {x**2 for x in numeros}
print(cuadrados)  # {1, 4, 9, 16, 25}

# Ejemplo de comprensión de diccionario en Python
nombres = ['Alice', 'Bob', 'Charlie']
longitudes = {nombre: len(nombre) for nombre in nombres}
print(longitudes)  # {'Alice': 5, 'Bob': 3, 'Charlie': 7}
```

Las comprensiones de conjuntos y diccionarios se utilizan para crear conjuntos y diccionarios de forma eficiente y expresiva, y permiten aplicar transformaciones y filtros a los elementos de una secuencia.

#### Decoradores

Los decoradores en Python son funciones que envuelven otras funciones y permiten agregar funcionalidades adicionales a las funciones sin modificar su código. Los decoradores se utilizan comúnmente para agregar lógica de registro, validación, autorización, entre otras, a las funciones existentes.

```python
# Ejemplo de decorador en Python
def decorador(funcion):
    def envoltura(*args, **kwargs):
        print('Antes de llamar a la función')
        resultado = funcion(*args, **kwargs)
        print('Después de llamar a la función')
        return resultado
    return envoltura

@decorador
def saludar(nombre):
    return f'Hola, {nombre}!'
```

En este ejemplo, el decorador `decorador` envuelve la función `saludar` y agrega lógica de registro antes y después de llamar a la función. El decorador se aplica a la función utilizando la sintaxis `@decorador`.

```python
# Ejemplo de uso de decorador en Python
print(saludar('Alice'))
```

El resultado de la ejecución de este código sería:

```plaintext
Antes de llamar a la función
Después de llamar a la función
Hola, Alice!
```

Los decoradores en Python son una forma poderosa de extender y modificar el comportamiento de las funciones existentes y se utilizan comúnmente en bibliotecas y marcos de aplicaciones para agregar funcionalidades adicionales a las funciones.

### Programación Asíncrona

La programación asíncrona en Python se refiere a la capacidad de ejecutar múltiples tareas de forma concurrente y paralela para mejorar el rendimiento y la eficiencia de un programa. Python proporciona soporte para la programación asíncrona a través de palabras clave y módulos especializados.

#### Hilos (`threading`)

Los hilos en Python se utilizan para ejecutar múltiples tareas de forma simultánea dentro de un mismo proceso. Los hilos comparten el mismo espacio de memoria y pueden acceder y modificar variables compartidas, lo que puede llevar a condiciones de carrera y problemas de concurrencia.

```python
# Ejemplo de hilo en Python
import threading

def imprimir_numeros():
    for i in range(5):
        print(i)

hilo = threading.Thread(target=imprimir_numeros)
hilo.start()
hilo.join()
```

En este ejemplo, se crea un hilo utilizando la clase `Thread` del módulo `threading` y se inicia el hilo utilizando el método `start`. El método `join` se utiliza para esperar a que el hilo termine su ejec

#### Procesos (`multiprocessing`)

Los procesos en Python se utilizan para ejecutar múltiples tareas de forma simultánea en procesos separados. Los procesos tienen su propio espacio de memoria y no comparten variables, lo que evita problemas de concurrencia y condiciones de carrera.

```python
# Ejemplo de proceso en Python
import multiprocessing

def imprimir_numeros():
    for i in range(5):
        print(i)

proceso = multiprocessing.Process(target=imprimir_numeros)
proceso.start()
proceso.join()
```

En este ejemplo, se crea un proceso utilizando la clase `Process` del módulo `multiprocessing` y se inicia el proceso utilizando el método `start`. El método `join` se utiliza para esperar a que el proceso termine su ejecución.

#### Corrutinas (`asyncio`)

Las corrutinas en Python se utilizan para ejecutar tareas asíncronas y permiten que una función se suspenda y se reanude en un momento posterior. Las corrutinas se definen utilizando la palabra clave `async` y se ejecutan utilizando el módulo `asyncio`. Este estilo de desarrollo utiliza las palabras clave `async` y `await` para definir funciones asíncronas y esperar la finalización de tareas asíncronas, respectivamente. Las funciones asíncronas permiten que una función se suspenda y se reanude en un momento posterior, mientras que la palabra clave `await` se utiliza para esperar a que una tarea asíncrona se complete.

```python
# Ejemplo de función asíncrona en Python
import asyncio

async def imprimir_numeros():
    for i in range(5):
        print(i)
        await asyncio.sleep(1)

async def main():
    await imprimir_numeros()

asyncio.run(main())
```

### Programación Orientada a Eventos

La programación orientada a eventos en Python se basa en el concepto de eventos y manejadores de eventos, y se utiliza para desarrollar aplicaciones que responden a eventos y señales del sistema. Python proporciona soporte para la programación orientada a eventos a través de módulos y bibliotecas especializadas. Algunos de los módulos y bibliotecas más utilizados para la programación orientada a eventos en Python son:

#### `tkinter`

`tkinter` es un módulo de Python que proporciona una interfaz gráfica de usuario (GUI) para desarrollar aplicaciones de escritorio. `tkinter` permite crear ventanas, botones, etiquetas, cuadros de texto, menús, entre otros elementos de la interfaz gráfica de usuario.

```python
# Ejemplo de interfaz gráfica de usuario con tkinter en Python
import tkinter as tk

def saludar():
    label.config(text='Hola, mundo!')

app = tk.Tk()
app.title('Aplicación de Saludo')

label = tk.Label(app, text='¡Hola!')
label.pack()

boton = tk.Button(app, text='Saludar', command=saludar)
boton.pack()

app.mainloop()
```

En este ejemplo, se crea una ventana de aplicación utilizando la clase `Tk` del módulo `tkinter` y se agregan una etiqueta y un botón a la ventana. El botón se configura para llamar a la función `saludar` cuando se hace clic en él, y la etiqueta se actualiza con el mensaje `'Hola, mundo!'` cuando se hace clic en el botón.

#### `asyncio`

`asyncio` es un módulo de Python que proporciona soporte para la programación asíncrona y la programación orientada a eventos. `asyncio` permite desarrollar aplicaciones que responden a eventos y señales del sistema de forma eficiente y concurrente.

```python
# Ejemplo de programación orientada a eventos con asyncio en Python
import asyncio

async def saludar():
    print('¡Hola, mundo!')

loop = asyncio.get_event_loop()
loop.run_until_complete(saludar())
loop.close()
```

En este ejemplo, se define una función asíncrona `saludar` que imprime el mensaje `'¡Hola, mundo!'`. La función `run_until_complete` se utiliza para ejecutar la función asíncrona `saludar` y esperar a que se complete.

#### `PyQt`

`PyQt` es una biblioteca de Python que proporciona enlaces para la biblioteca Qt de C++ y permite desarrollar aplicaciones de escritorio con una interfaz gráfica de usuario (GUI) avanzada y personalizable.

```python
# Ejemplo de interfaz gráfica de usuario con PyQt en Python
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget

def saludar():
    label.setText('¡Hola, mundo!')

app = QApplication([])
window = QWidget()
window.setWindowTitle('Aplicación de Saludo')

layout = QVBoxLayout()
label = QLabel('¡Hola!')

button = QPushButton('Saludar')
button.clicked.connect(saludar)

layout.addWidget(label)
layout.addWidget(button)

window.setLayout(layout)
window.show()

app.exec_()
```

En este ejemplo, se crea una ventana de aplicación utilizando la clase `QApplication` y se agregan una etiqueta y un botón a la ventana utilizando las clases `QLabel` y `QPushButton`, respectivamente. El botón se conecta a la función `saludar` utilizando la señal `clicked`, y la etiqueta se actualiza con el mensaje `'¡Hola, mundo!'` cuando se hace clic en el botón.

## Módulo 3: Acceso a Bases de Datos con Python

### Bases de Datos Relacionales

Las bases de datos relacionales son sistemas de gestión de bases de datos (SGBD) que utilizan tablas para almacenar datos y relaciones entre los datos. Las bases de datos relacionales utilizan el lenguaje de consulta estructurado (SQL) para realizar operaciones de consulta, inserción, actualización y eliminación de datos. Python proporciona soporte para acceder y manipular bases de datos relacionales a través de módulos y bibliotecas especializadas. Algunos de los módulos y bibliotecas más utilizados para acceder a bases de datos relacionales en Python son:

#### `sqlite3`

`sqlite3` es un módulo de Python que proporciona una interfaz para trabajar con bases de datos SQLite, que es un sistema de gestión de bases de datos relacional ligero y autónomo. `sqlite3` permite crear, conectar, consultar y modificar bases de datos SQLite utilizando SQL. El módulo `sqlite3` está incluido en la biblioteca estándar de Python y no requiere instalación adicional.

Veamos el siguiente ejemplo de acceso a una base de datos SQLite con `sqlite3` en Python:

```python
# Ejemplo de acceso a base de datos SQLite con sqlite3 en Python
import sqlite3

conexion = sqlite3.connect('ejemplo.db')

cursor = conexion.cursor()
cursor.execute('CREATE TABLE usuarios (id INTEGER PRIMARY KEY, nombre TEXT, edad INTEGER)')
conexion.commit()

cursor.execute('INSERT INTO usuarios (nombre, edad) VALUES (?, ?)', ('Alice', 30))
conexion.commit()

cursor.execute('SELECT * FROM usuarios')
usuarios = cursor.fetchall()
print(usuarios)

conexion.close()
```

En este ejemplo, se crea una base de datos SQLite utilizando la función `connect` del módulo `sqlite3` y se crea una tabla `usuarios` con columnas `id`, `nombre` y `edad`. Se inserta un nuevo usuario en la tabla utilizando la función `execute` y se consulta todos los usuarios utilizando la función `fetchall`.

#### `MySQLdb`

`MySQLdb` es un módulo de Python que proporciona una interfaz para trabajar con bases de datos MySQL, que es un sistema de gestión de bases de datos relacional de código abierto y ampliamente utilizado. `MySQLdb` permite conectar, consultar y modificar bases de datos MySQL utilizando SQL.

Para instalar `MySQLdb`, se puede utilizar el siguiente comando:

```bash
pip install mysqlclient
```

Veamos el siguiente ejemplo de acceso a una base de datos MySQL con `MySQLdb` en Python:

```python
# Ejemplo de acceso a base de datos MySQL con MySQLdb en Python
import MySQLdb

conexion = MySQLdb.connect(host='localhost,
                           user='usuario',
                           password='contraseña',
                           database='ejemplo')

cursor = conexion.cursor()
cursor.execute('CREATE TABLE usuarios (id INT PRIMARY KEY, nombre VARCHAR(50), edad INT)')
conexion.commit()

cursor.execute('INSERT INTO usuarios (nombre, edad) VALUES (%s, %s)', ('Alice', 30))
conexion.commit()

cursor.execute('SELECT * FROM usuarios')
usuarios = cursor.fetchall()
print(usuarios)

conexion.close()
```

En este ejemplo, se crea una conexión a una base de datos MySQL utilizando la función `connect` del módulo `MySQLdb` y se crea una tabla `usuarios` con columnas `id`, `nombre` y `edad`. Se inserta un nuevo usuario en la tabla utilizando la función `execute` y se consulta todos los usuarios utilizando la función `fetchall`.

#### `psycopg2`

`psycopg2` es un módulo de Python que proporciona una interfaz para trabajar con bases de datos PostgreSQL, que es un sistema de gestión de bases de datos relacional de código abierto y ampliamente utilizado. `psycopg2` permite conectar, consultar y modificar bases de datos PostgreSQL utilizando SQL.

Para instalar `psycopg2`, se puede utilizar el siguiente comando:

```bash
pip install psycopg2-binary
```

Veamos el siguiente ejemplo de acceso a una base de datos PostgreSQL con `psycopg2` en Python:

```python
# Ejemplo de acceso a base de datos PostgreSQL con psycopg2 en Python
import psycopg2

conexion = psycopg2.connect(host='localhost',
                           user='usuario',
                           password='contraseña',
                           database='ejemplo')

cursor = conexion.cursor()
cursor.execute('CREATE TABLE usuarios (id SERIAL PRIMARY KEY, nombre VARCHAR(50), edad INT)')
conexion.commit()

cursor.execute('INSERT INTO usuarios (nombre, edad) VALUES (%s, %s)', ('Alice', 30))
conexion.commit()

cursor.execute('SELECT * FROM usuarios')
usuarios = cursor.fetchall()
print(usuarios)

conexion.close()
```

En este ejemplo, se crea una conexión a una base de datos PostgreSQL utilizando la función `connect` del módulo `psycopg2` y se crea una tabla `usuarios` con columnas `id`, `nombre` y `edad`. Se inserta un nuevo usuario en la tabla utilizando la función `execute` y se consulta todos los usuarios utilizando la función `fetchall`.

#### `SQLAlchemy`

`SQLAlchemy` es una biblioteca de Python que proporciona una interfaz de alto nivel para trabajar con bases de datos relacionales y permite interactuar con bases de datos de forma más abstracta y orientada a objetos. `SQLAlchemy` proporciona una capa de abstracción sobre las bases de datos y permite definir modelos de datos, consultas y transacciones de forma más sencilla y eficiente.

Para instalar `SQLAlchemy`, se puede utilizar el siguiente comando:

```bash
pip install sqlalchemy
```

Para utilizar `SQLAlchemy`, se debe contar con el controlador de la base de datos correspondiente instalado. Por ejemplo, para trabajar con PostgreSQL, se puede instalar el controlador `psycopg2`.

Veamos el siguiente ejemplo de acceso a una base de datos SQLite con `SQLAlchemy` en Python:

```python
# Ejemplo de acceso a base de datos SQLite con SQLAlchemy en Python
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    edad = Column(Integer)

engine = create_engine('postgresql://usuario:contraseña@localhost/ejemplo')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
sesion = Session()

alice = Usuario(nombre='Alice', edad=30)
sesion.add(alice)
sesion.commit()

usuarios = sesion.query(Usuario).all()
for usuario in usuarios:
    print(usuario.nombre, usuario.edad)

sesion.close()
```

### Bases de Datos No Relacionales

Las bases de datos no relacionales, también conocidas como bases de datos NoSQL, son sistemas de gestión de bases de datos que utilizan modelos de datos no relacionales para almacenar y recuperar datos. Las bases de datos NoSQL son adecuadas para aplicaciones que requieren escalabilidad, flexibilidad y rendimiento en entornos distribuidos y de alto volumen de datos. Python proporciona soporte para acceder y manipular bases de datos NoSQL a través de módulos y bibliotecas especializadas. Algunos de los módulos y bibliotecas más utilizados para acceder a bases de datos NoSQL en Python son:

#### `pymongo`

`pymongo` es un módulo de Python que proporciona una interfaz para trabajar con bases de datos MongoDB, que es un sistema de gestión de bases de datos NoSQL de código abierto y ampliamente utilizado. `pymongo` permite conectar, consultar y modificar bases de datos MongoDB utilizando operaciones de consulta y actualización.

```python
# Ejemplo de acceso a base de datos MongoDB con pymongo en Python
import pymongo

cliente = pymongo.MongoClient('mongodb://localhost:27017/')
base_de_datos = cliente['ejemplo']
coleccion = base_de_datos['usuarios']

coleccion.insert_one({'nombre': 'Alice', 'edad': 30})

usuarios = coleccion.find()
for usuario in usuarios:
    print(usuario)

cliente.close()
```

En este ejemplo, se crea una conexión a una base de datos MongoDB utilizando la clase `MongoClient` del módulo `pymongo` y se inserta un nuevo usuario en la colección `usuarios` utilizando la función `insert_one`. Se consulta todos los usuarios en la colección utilizando la función `find` y se imprime cada usuario.

#### `redis-py`

`redis-py` es un módulo de Python que proporciona una interfaz para trabajar con bases de datos Redis, que es un sistema de almacenamiento de datos en memoria de código abierto y ampliamente utilizado. `redis-py` permite conectar, consultar y modificar bases de datos Redis utilizando operaciones de almacenamiento y recuperación de datos.

```python
# Ejemplo de acceso a base de datos Redis con redis-py en Python
import redis

conexion = redis.Redis(host='localhost', port=6379, db=0)

conexion.set('nombre', 'Alice')
nombre = conexion.get('nombre')
print(nombre)

conexion.close()
```

En este ejemplo, se crea una conexión a una base de datos Redis utilizando la clase `Redis` del módulo `redis-py` y se almacena un valor en la clave `'nombre'` utilizando la función `set`. Se recupera el valor de la clave `'nombre'` utilizando la función `get` y se imprime el valor.

#### `google-cloud-bigquery`

`google-cloud-bigquery` es una biblioteca de Python que proporciona una interfaz para trabajar con BigQuery, que es un servicio de almacenamiento y análisis de datos en la nube de Google. `google-cloud-bigquery` permite conectar, consultar y modificar bases de datos BigQuery utilizando operaciones de consulta y actualización.

```python
# Ejemplo de acceso a base de datos BigQuery con google-cloud-bigquery en Python
from google.cloud import bigquery

cliente = bigquery.Client()

consulta = 'SELECT * FROM `proyecto.dataset.tabla`'
resultados = cliente.query(consulta)

for fila in resultados:
    print(fila)

cliente.close()
```

En este ejemplo, se crea una conexión a BigQuery utilizando la clase `Client` del módulo `google-cloud-bigquery` y se ejecuta una consulta SQL para recuperar todos los datos de una tabla. Se recorren los resultados de la consulta y se imprimen las filas.
