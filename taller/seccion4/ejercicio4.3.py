#  Ejercicio 4.3 – Gestor de inventario de productos:
# Dada una lista de diccionarios donde cada diccionario representa un producto con las claves "nombre", "precio" y "stock", crear un programa que permita actualizar el precio de un producto específico buscándolo por su nombre.

print("--- Gestor de inventario de productos ---\n")
print("Lista de productos:")
print("Nombre      Precio     Stock")
print("-" * 30)

products = [
    {"nombre": "Producto A", "precio": 10.0, "stock": 100},
    {"nombre": "Producto B", "precio": 20.0, "stock": 50},
    {"nombre": "Producto C", "precio": 15.0, "stock": 75},
]

while True:
    for product in products:
        print(f"{product['nombre']}\t{product['precio']}\t{product['stock']}")

    name = input("\nIngrese el nombre del producto para actualizar su precio (o 'salir' para terminar): ")
    if name.lower() == "salir":
        break

    found = False
    for product in products:
        if product["nombre"].lower() == name.lower():
            new_price = float(input("Ingrese el nuevo precio: "))
            product["precio"] = new_price
            print(f"Precio de {product['nombre']} actualizado a {new_price}.\n")
            found = True
            break

    if not found:
        print("Producto no encontrado. Intente nuevamente.")