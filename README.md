# 🐍 Taller 2: Ejercicios de Python

Este repositorio contiene una colección de ejercicios de Python diseñados para practicar conceptos fundamentales de programación. Los ejercicios están organizados en secciones temáticas, que van desde el manejo básico de variables hasta la creación de un mini-proyecto integrador.


## ⚙️ Requisitos previos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)

---


## 🚀 Instalación y uso

### 1. Clonar el repositorio

```bash
git clone https://github.com/joshan10/taller2_python.git
cd taller2_python
```

### 2. (Opcional) Crear un entorno virtual

```bash
python -m venv venv
source venv/bin/activate        # En Linux/macOS
venv\Scripts\activate           # En Windows
```
## 3. Cómo Ejecutar los Scripts

Para ejecutar cualquiera de los ejercicios, navegue al directorio del repositorio en su terminal y use el comando `python` seguido de la ruta del archivo que desea ejecutar.

```bash
# Ejemplo para ejecutar el primer ejercicio de la sección 1
python taller/seccion1/ejercicio1.1.py

# Ejemplo para ejecutar el sistema de biblioteca
python taller/seccion6/sistema_gestion_biblioteca.py
```


---

## 🗂️ Estructura del proyecto

```text
taller2_Estructuras de control y Funciones/
├─ README.md                    # Documentación del proyecto
├─ requirements.txt             # Enunciados de los ejercicios
├─ taller/                      # Paquete principal (código fuente)
│  ├─ seccion1/                 # MANEJO DE VARIABLES Y ENTRADA DE DATOS
│  │  ├─ ejercicio_1.1.py
│  │  ├─ ejercicio_1.2.py
│  │  ├─ ejercicio_1.3.py
│  │  ├─ ejercicio_1.4.py
│  │  └─ ejercicio_1.5.py
│  ├─ seccion2/                 # IMPLEMENTACIÓN DE CONDICIONALES
│  │  ├─ ejercicio_2.1.py
│  │  ├─ ejercicio_2.2.py
│  │  ├─ ejercicio_2.3.py
│  │  ├─ ejercicio_2.4.py
│  │  └─ ejercicio_2.5.py
│  ├─ seccion3/                 # USO DE CICLOS FOR Y WHILE
│  │  ├─ ejercicio_3.1.py
│  │  ├─ ejercicio_3.2.py
│  │  ├─ ejercicio_3.3.py
│  │  ├─ ejercicio_3.4.py
│  │  └─ ejercicio_3.5.py
│  ├─ seccion4/                 # GESTIÓN DE LISTAS Y DICCIONARIOS
│  │  ├─ ejercicio_4.1.py
│  │  ├─ ejercicio_4.2.py
│  │  ├─ ejercicio_4.3.py
│  │  ├─ ejercicio_4.4.py
│  │  └─ ejercicio_4.5.py
│  └─ seccion5/                 # CREACIÓN Y USO DE FUNCIONES
│     ├─ ejercicio_5.1.py
│     ├─ ejercicio_5.2.py
│     ├─ ejercicio_5.3.py
│     ├─ ejercicio_5.4.py
│     └─ ejercicio_5.5.py
└─ seccion6/                    # MINI-TALLER INTEGRADOR
   └─ biblioteca.py
```

---

## 📚 Contenido por sección

| Sección | Tema |
|---------|------|
| `seccion1` | Manejo de variables y entrada de datos |
| `seccion2` | Implementación de condicionales |
| `seccion3` | Uso de ciclos `for` y `while` |
| `seccion4` | Gestión de listas y diccionarios |
| `seccion5` | Creación y uso de funciones |
| `seccion6` | Mini-taller integrador (`biblioteca.py`) |

---

## Listado de Ejercicios

A continuación se detalla el contenido de cada sección.

### Sección 1: Manejo de Variables y Entrada de Datos

-   **ejercicio1.1.py:** Pide nombre, edad y ciudad del usuario y los muestra en un mensaje. Valida que la edad sea un número positivo.
-   **ejercicio1.2.py:** Una calculadora básica que pide dos números y una operación (+, -, \*, /) y valida la división por cero.
-   **ejercicio1.3.py:** Valida que un correo electrónico ingresado contenga los caracteres "@" y "." en posiciones válidas.
-   **ejercicio1.4.py:** Un validador de contraseñas que verifica longitud mínima, mayúsculas, números y caracteres especiales.
-   **ejercicio1.5.py:** Un convertidor de unidades con un menú para Celsius a Fahrenheit, kilómetros a millas y kilogramos a libras.

### Sección 2: Implementación de Condicionales

-   **ejercicio2.1.py:** Clasifica la edad de una persona en niño, adolescente, adulto o adulto mayor.
-   **ejercicio2.2.py:** Un menú básico con opciones para saludar, despedirse o salir del programa.
-   **ejercicio2.3.py:** Una versión mejorada de la calculadora que permite realizar múltiples operaciones sin salir.
-   **ejercicio2.4.py:** Convierte una calificación numérica (0-100) a su equivalente en letras (A, B, C, D, F).
-   **ejercicio2.5.py:** Simula descuentos en compras según la categoría del cliente (A, B, C).

### Sección 3: Uso de Ciclos `for` y `while`

-   **ejercicio3.1.py:** Pide un número N y muestra todos los números pares desde 1 hasta N.
-   **ejercicio3.2.py:** Suma números ingresados por el usuario hasta que se introduce el número 0.
-   **ejercicio3.3.py:** Busca un nombre en una lista predefinida y muestra si existe y su posición.
-   **ejercicio3.4.py:** Genera la tabla de multiplicar de un número y pregunta al usuario si desea generar otra.
-   **ejercicio3.5.py:** Pide 10 números al usuario y muestra una lista sin los elementos duplicados.

### Sección 4: Gestión de Listas y Diccionarios

-   **ejercicio4.1.py:** Sistema para gestionar una lista de compras (agregar, eliminar y mostrar productos).
-   **ejercicio4.2.py:** Directorio de contactos que usa un diccionario para almacenar nombres y teléfonos (agregar, buscar, eliminar).
-   **ejercicio4.3.py:** Gestor de inventario que permite actualizar el precio de un producto buscándolo por su nombre en una lista de diccionarios.
-   **ejercicio4.4.py:** Analizador estadístico que calcula el máximo, mínimo, promedio y suma de una lista de números.
-   **ejercicio4.5.py:** Compara dos listas y muestra elementos comunes y elementos únicos de cada una.

### Sección 5: Creación y Uso de Funciones

-   **ejercicio5.1.py:** Una función que genera saludos personalizados ("Buenos días", "Buenas tardes", "Buenas noches") según el nombre y la hora.
-   **ejercicio5.2.py:** Una función que calcula el promedio de una lista de números y valida si la lista está vacía.
-   **ejercicio5.3.py:** Refactorización de la calculadora, separando cada operación matemática en su propia función.
-   **ejercicio5.4.py:** Una función que detecta si un texto es un palíndromo, ignorando espacios y mayúsculas.
-   **ejercicio5.5.py:** Una función recursiva para calcular el factorial de un número, con validación para números negativos.

### Sección 6: Mini-Taller Integrador - Sistema de Gestión de Biblioteca

El archivo `sistema_gestion_biblioteca.py` es un programa completo que simula la gestión de una biblioteca.

**Características Principales:**

-   **Gestión de Libros:** Utiliza una lista de diccionarios para almacenar la información de los libros (ID, título, autor, año, disponibilidad).
-   **Agregar Libro:** Permite registrar nuevos libros en el catálogo.
-   **Mostrar Libros:** Muestra una lista formateada de todos los libros existentes.
-   **Buscar Libro:** Busca libros por título o autor, mostrando coincidencias parciales.
-   **Prestar y Devolver:** Cambia el estado de disponibilidad de un libro por su ID.
-   **Eliminar Libro:** Elimina un libro del catálogo si no está prestado.
-   **Estadísticas:** Muestra la cantidad total de libros, cuántos están disponibles y cuántos están prestados.
-   **Exportar a TXT:** Guarda el catálogo completo de la biblioteca en un archivo `biblioteca.txt`.

  ## 👨‍🏫 Autor
**joshan ire pereira cabrera**  
Aprendiz – Desarrollo de Software


## 📄 Licencia

Este proyecto fue desarrollado con fines académicos.
