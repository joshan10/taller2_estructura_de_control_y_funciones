#  Ejercicio 3.3 – Búsqueda en lista de nombres:
# Dada una lista predefinida de nombres, crear un programa que permita al usuario buscar un nombre específico. El algoritmo debe recorrer la lista e indicar si el nombre se encuentra o no en ella, mostrando su posición en caso afirmativo.

print("====== Búsqueda en lista de nombres ======")
print("====== Ingrese 0 para salir ======")


list_name = ["raul", "pepito", "carlos", "mario", "santiago"]
salir = 0

while True:
    nombre = input("Ingrese un nombre para verficar si esta en la lista: ")
    try:
        indice = list_name.index(nombre)
        for i in list_name:
            if i == nombre:
                print(f"\nEl nombre {nombre} esta en la lista y su posición esta en {indice} \n ")
    except ValueError:
        print("El nombre no se encuentra en la lista")
    if nombre == "0":
        print("\nSaliendo del programa...")
        break
