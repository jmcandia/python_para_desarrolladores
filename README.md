# PYTHON PARA DESARROLLADORES

## Introducción

Este documento es una guía para desarrolladores que desean aprender Python desde cero o que desean profundizar en sus conocimientos. Se asume que el lector tiene conocimientos previos de programación y que está familiarizado con los conceptos básicos de programación.

Este proceso de aprendizaje estará basado en la práctica, por lo que iremos desarrollando un pequeño programa, en el que itemos avanzando desde los conceptos más básicos hasta los más avanzados.

## Contenido

- [PYTHON PARA DESARROLLADORES](#python-para-desarrolladores)
  - [Introducción](#introducción)
  - [Contenido](#contenido)
  - [Ejercicio](#ejercicio)
    - [Objetivos del Ejercicio](#objetivos-del-ejercicio)
    - [Conocimientos Esperados](#conocimientos-esperados)

## Ejercicio

Este ejercicio integra de forma práctica los fundamentos y herramientas avanzadas de Python, abarcando desde la programación orientada a objetos hasta el manejo de bases de datos. A través de este problema, el estudiante desarrollará una comprensión sólida del lenguaje, con un enfoque en buenas prácticas, eficiencia en el manejo de datos y estructuración del código.

### Objetivos del Ejercicio

1. **Aplicar conocimientos de programación estructurada y modular** en Python.
   - Comprender y aplicar el uso de variables, operadores, estructuras de control, y funciones.
   - Utilizar correctamente las estructuras de datos como listas y diccionarios.

2. **Implementar la Programación Orientada a Objetos (POO)**:
   - Diseñar clases para representar entidades del mundo real (productos e inventario).
   - Definir atributos y métodos que permitan encapsular y manipular datos de forma estructurada.
   - Implementar el concepto de **decoradores** para añadir funcionalidades adicionales a los métodos.

3. **Introducir la Programación Funcional**:
   - Utilizar funciones de orden superior como `filter()` y `reduce()` para búsquedas y cálculos.
   - Implementar funciones lambda para operaciones simples.

4. **Desarrollar habilidades en Programación Asíncrona**:
   - Utilizar el módulo `asyncio` para simular operaciones costosas (por ejemplo, el cálculo del valor total del inventario).

5. **Gestionar Bases de Datos Relacionales**:
   - Conectar y manipular una base de datos SQLite mediante el módulo `sqlite3`.
   - Crear, leer, buscar y calcular información almacenada en la base de datos (operaciones CRUD).
   - Garantizar la persistencia de los datos a través del almacenamiento en la base de datos.

### Conocimientos Esperados

Al resolver el ejercicio, se espera que el estudiante demuestre los siguientes conocimientos:

1. **Fundamentos de Python**:
   - Uso de **sintaxis básica**, estructuras de control (`if`, `for`, `while`), y entrada/salida estándar (`input`, `print`).
   - Manejo de **tipos de datos** como cadenas, números, listas y diccionarios.

2. **Programación Orientada a Objetos (POO)**:
   - Creación de clases y objetos.
   - Implementación de métodos y atributos.
   - Uso de **decoradores** para extender la funcionalidad de métodos.

3. **Programación Funcional**:
   - Aplicación de funciones lambda y de orden superior (`filter`, `reduce`).

4. **Programación Asíncrona**:
   - Introducción al módulo `asyncio` para operaciones concurrentes.

5. **Bases de Datos con SQLite**:
   - Creación y manipulación de tablas con SQL.
   - Realización de operaciones CRUD:
     - **C**: Crear registros (añadir productos).
     - **R**: Leer registros (mostrar inventario).
     - **U**: Actualizar registros (extensión opcional).
     - **D**: Eliminar registros (extensión opcional).
   - Ejecución de consultas SQL con parámetros.

6. **Buenas Prácticas de Programación**:
   - Modularización del código.
   - Uso de **decoradores** para registro de operaciones.
   - Implementación de métodos que mantienen la claridad y la legibilidad del programa.
