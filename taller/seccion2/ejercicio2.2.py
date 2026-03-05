# Ejercicio 2.2 – Menú de opciones básico:
# Implementar un menú interactivo con tres opciones: 1. Saludar, 2. Despedirse, 3. Salir. El programa debe mostrar el menú, leer la opción seleccionada y ejecutar la acción correspondiente utilizando estructuras condicionales if-elif-else.

print("================================")
print("Bienvenido al menú de opciones.")
print("creado por joshan pereira")
print("================================")
print("Seleccione una opción:")
print("1. Saludar")
print("2. Despedirse")
print("3. Salir")
opcion = input("Ingrese el número de la opción deseada: ")
if opcion == "1":
    print("¡Hola! ¿Cómo estás?")
elif opcion == "2":
    print("¡Adiós! Que tengas un buen día.")
elif opcion == "3":
    print("Saliendo del programa. ¡Hasta luego!")
else:
    print("Opción no válida. Por favor, seleccione una opción del 1 al 3.")
