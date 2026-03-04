# Ejercicio 4.5 – Comparador avanzado de listas:
# Implementar un programa que permita al usuario ingresar dos listas de elementos. El algoritmo debe mostrar: los elementos comunes a ambas listas, los elementos únicos de la primera lista y los elementos únicos de la segunda lista, implementando esta lógica con ciclos sin usar funciones de conjuntos.

print("--- Comparador avanzado de listas ---\n")
# Solicitar al usuario ingresar dos listas de elementos separados por comas
list1 = input("Ingrese la primera lista de elementos separados por comas: ")
list2 = input("Ingrese la segunda lista de elementos separados por comas: ")

# Convertir las entradas en listas de elementos, eliminando espacios adicionales
list1 = [item.strip() for item in list1.split(",")]
list2 = [item.strip() for item in list2.split(",")]

# Elementos comunes
common_elements = []
for item in list1:
    if item in list2 and item not in common_elements:
        common_elements.append(item)

print(f"Elementos comunes: {common_elements}")

# Elementos únicos de la primera lista
unique_to_list1 = []
for item in list1:
    if item not in list2:
        unique_to_list1.append(item)

print(f"Elementos únicos de la primera lista: {unique_to_list1}")

# Elementos únicos de la segunda lista
unique_to_list2 = []
for item in list2:
    if item not in list1:
        unique_to_list2.append(item)

print(f"Elementos únicos de la segunda lista: {unique_to_list2}")