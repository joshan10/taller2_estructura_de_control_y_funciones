# Ejercicio 4.1 – Sistema de lista de compras:
# Implementar un sistema de lista de compras que permita al usuario agregar productos, eliminar productos específicos y mostrar todos los productos actuales. Utilizar una lista para almacenar los elementos.

print("\n====== Sistema de lista de compras ======")

list_product = []

while True:
    print("1. Agregar Producto")
    print("2. Eliminar")
    print("3. Mostrar")
    print("4. Salir")
    op = input("\nElige una opcion: ")

    match op:
        case "1":
            name_product = input("Ingrese un producto para agregarlo: ")
            list_product.append(name_product)
            print(f"Producto {name_product} agregado. \n")


        case "2":
            name_product = input("Ingrese un producto para eliminarlo: ")
            if name_product in list_product:
                list_product.remove(name_product)
                print(f"Producto {name_product} eliminido.\n")
            else:
                print("Producto no encontado. Así que no es posibles eliminar.\n")
        
        case "3":
            if not list_product:
                print("Lista de productos vacios\n")
            else:
                for name_product in list_product:
                    print(f"- {name_product}\n")
        case "4":
            break



