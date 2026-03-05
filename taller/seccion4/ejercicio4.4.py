# Ejercicio 4.4 – Analizador estadístico de listas numéricas:
# Desarrollar un programa que solicite al usuario ingresar una lista de números separados por comas. El algoritmo debe calcular y mostrar: el valor máximo, el valor mínimo, el promedio y la suma total de todos los números.
print("--- Analizador estadístico de listas numéricas ---\n")

numbers = input("Ingrese una lista de números separados por comas: ")

# Convertir la entrada en una lista de números, eliminando espacios adicionales
num_list = [float(num.strip()) for num in numbers.split(",")]
if num_list:
    max_value = max(num_list)
    min_value = min(num_list)
    average = sum(num_list) / len(num_list)
    total_sum = sum(num_list)

    print(f"Valor máximo: {max_value}")
    print(f"Valor mínimo: {min_value}")
    print(f"Promedio: {average}")
    print(f"Suma total: {total_sum}")
else:
    print("No se ingresaron números válidos.")
