# Ejercicio 5.5 – Calculadora factorial recursiva:
# Implementar una función llamada factorial que calcule el factorial de un número usando recursión. La función debe recibir un número entero positivo y retornar su factorial. Incluir validación para números negativos.

print("--- Calculadora factorial recursiva ---\n")

def factorial(n):
    if n < 0:
        return "Error: El número debe ser un entero positivo."
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
# Pedir al usuario un número para calcular su factorial
numero = int(input("Ingrese un número entero positivo para calcular su factorial: "))
print(f"El factorial de {numero} es: {factorial(numero)}")

