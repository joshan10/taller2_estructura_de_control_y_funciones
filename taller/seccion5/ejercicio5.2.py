#  Ejercicio 5.2 – Calculadora de promedios:
# Implementar una función llamada calcular_promedio que reciba una lista de números como parámetro y retorne el promedio de esos números. Incluir validación para listas vacías.

print("--- Calculadora de promedios ---\n")

def calcular_promedio(numeros):
    if len(numeros) == 0:
        return "La lista está vacía. No se puede calcular el promedio."
    else:
        promedio = sum(numeros) / len(numeros)
        return f"El promedio es: {promedio}"
    
print(calcular_promedio([10, 20, 30, 40, 50]))

    

