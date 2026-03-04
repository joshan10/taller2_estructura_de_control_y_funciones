# Ejercicio 3.5 – Eliminador de duplicados en lista:
# Crear un algoritmo que permita al usuario ingresar 10 números (que pueden repetirse) y luego muestre una lista sin elementos duplicados. Implementar la lógica de eliminación de duplicados usando ciclos y una lista auxiliar, sin utilizar funciones de conjuntos.

print("====== Eliminador de duplicados en lista ======")

numbers = []
for i in range(10):
    number_user = int(input(f"Ingrese el número {i + 1}: "))
    numbers.append(number_user)
unique_numbers = []
for number in numbers:
    if number not in unique_numbers:
        unique_numbers.append(number)
print("Lista sin elementos duplicados:")
print(unique_numbers)