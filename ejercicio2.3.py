# Ejercicio 2.3 – Calculadora con menú mejorado:
# Expandir la calculadora básica del ejercicio 1.2 agregando un menú que permita al usuario realizar múltiples operaciones sin salir del programa. El menú debe incluir las cuatro operaciones básicas y una opción para salir.

print("================================")
print("Bienvenido al programa de calculadora.")
print("creado por joshan pereira")
print("================================")

#solictud de datos de usuario
num1 = float(input("Ingrese un número: "))
num2 = float(input("Ingrese un segundo número: "))
operacion = input("Ingrese la operación que desea realizar ( + (para sumar) , - (para restar), * (para multiplicar), / (para dividir)): ") 
salir = input("¿Desea salir del programa? (s/n): ")

#validacion de operacion
while operacion not in ["+", "-", "*", "/"]:
    print("Operación no válida. Por favor, ingrese una operación válida (+, -, *, /).")
    operacion = input("\nIngrese la operación que desea realizar ( + (para sumar) , - (para restar), * (para multiplicar), / (para dividir)): ")
    match operacion:
        case "+":
            resultado = num1 + num2
            print(f"La suma de {num1} y {num2} es: {resultado}")
        case "-":
            resultado = num1 - num2
            print(f"La resta de {num1} y {num2} es: {resultado}")
        case "*":
            resultado = num1 * num2
            print(f"La multiplicación de {num1} y {num2} es: {resultado}")
        case "/":
            if num2 != 0:
                resultado = num1 / num2
                print(f"La división de {num1} entre {num2} es: {resultado}")
            else:
                print("Error: No se puede dividir entre cero.")
        case _:
            print("Operación no válida. Por favor, ingrese una operación válida (+, -, *, /).")
    salir = input("¿Desea salir del programa? (s/n): ")
    if salir.lower() == "s":
        print("Saliendo del programa. ¡Hasta luego!")
        break

    