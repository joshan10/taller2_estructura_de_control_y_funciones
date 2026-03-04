# Ejercicio 5.3 – Refactorización de menú de calculadora:
# Tomar el menú de calculadora desarrollado en ejercicios anteriores y refactorizarlo, convirtiendo cada operación matemática en una función separada. El menú principal debe llamar a estas funciones según la opción seleccionada.

print("--- Refactorización de menú de calculadora ---\n")

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: No se puede dividir por cero."
    
def menu_calculadora():
    while True:
        print("Seleccione una operación:")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Salir")
        
        opcion = input("Ingrese el número de la operación que desea realizar: ")
        
        if opcion == '5':
            print("Saliendo del programa...")
            break
        elif opcion in ['1', '2', '3', '4']:
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))
            
            if opcion == '1':
                resultado = sumar(num1, num2)
                print(f"El resultado de la suma es: {resultado}")
            elif opcion == '2':
                resultado = restar(num1, num2)
                print(f"El resultado de la resta es: {resultado}")
            elif opcion == '3':
                resultado = multiplicar(num1, num2)
                print(f"El resultado de la multiplicación es: {resultado}")
            elif opcion == '4':
                resultado = dividir(num1, num2)
                print(f"El resultado de la división es: {resultado}")
        else:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 5.")

menu_calculadora()