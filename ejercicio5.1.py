#  Ejercicio 5.1 – Generador de saludos personalizados:
# Crear una función llamada saludar que reciba dos parámetros: nombre y hora del día. La función debe retornar un saludo apropiado según la hora: "Buenos días [nombre]" (5-12), "Buenas tardes [nombre]" (13-19), "Buenas noches [nombre]" (20-4).

print("--- Generador de saludos personalizados ---\n")

def saludar(nombre, hora):
    if hora >= 5 and hora <= 12:
        return (f"Buenos días {nombre}")
    elif hora >= 13 and hora <= 19:
        return (f"Buenos tardes {nombre}")
    elif hora >= 20 or hora <= 4:
        return (f"Buenos noches {nombre}")


print(saludar("joshan", 2))