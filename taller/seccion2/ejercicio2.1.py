#Ejercicio 2.1 – Clasificación de edades:
#Crear un algoritmo que solicite la edad de una persona y la clasifique en una de las siguientes categorías: niño (0-12 años), adolescente (13-17 años), adulto (18-64 años) o adulto mayor (65 años o más). Mostrar la categoría correspondiente.

edad = int(input("Ingrese la edad de la persona: "))
if edad < 0:
    print("Edad no válida. Por favor ingrese una edad positiva.")
elif edad <= 12:
    print("La persona es un niño.")
elif edad <= 17:
    print("La persona es un adolescente.")
elif edad <= 64:
    print("La persona es un adulto.")
else:
    print("La persona es un adulto mayor.")