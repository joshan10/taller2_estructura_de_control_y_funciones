# Ejercicio 4.2 – Directorio de contactos:
# Crear un directorio de contactos utilizando diccionarios, donde cada contacto tenga un nombre (clave) y un número telefónico (valor). El sistema debe permitir agregar nuevos contactos, buscar contactos por nombre y eliminar contactos existentes.

contact = {}
print("\n--- Directorio de contacto ---")

while True:
    print("1. Agregar")
    print("2. buscar")
    print("3. Eliminar")
    print("4. Mostrar")
    print("5. Salir")
    op = input("Elige una opcion: ")

    match op:
        case "1":
            name = input("Digite Nombre: ")
            cel = input("Digite Telefono: ")
            contact[name] = cel  # Agregar al diccionario
            print("Contacto agregado")
        case "2":
            name = input("Digite Nombre a buscador: ")
            if name in contact:
                print(f"contacto encontrado: {contact[name]}")
            else:
                print("contacto no encontrado")
        case "3":
            name = input("Digite nombre a eliminar: ")
            if name in contact:
                del contact[name]
                print("contacto eliminado ")
            else:
                print("Contacto no encontrado")
        case "4":
            if not contact:
                print("contactos vacios")
            else:
                for name, t in contact.items():
                    print(f"{name}: {t}")
        case "5":
            break