# Ejercicio 1.2 – Calculadora básica: Desarrollar una calculadora simple que solicite al usuario dos números y una operación matemática (+, -, *, /). El algoritmo debe realizar la operación correspondiente y mostrar el resultado. Incluir validación para evitar la división por cero, mostrando un mensaje de error en ese caso.


print("================================")
print("Bienvenido al programa de calculadora.")
print("creado por joshan pereira")
print("================================")

#solictud de datos de usuario
num1 = float(input("Ingrese un número: "))
num2 = float(input("Ingrese un segundo número: "))
operacion = input("Ingrese la operación que desea realizar ( + (para sumar) , - (para restar), * (para multiplicar), / (para dividir)): ") 


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
    