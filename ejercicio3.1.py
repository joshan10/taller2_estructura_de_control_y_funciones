# Ejercicio 3.1 – Generador de números pares:
# Crear un programa que solicite al usuario un número entero positivo N y muestre todos los números pares desde 1 hasta N utilizando un ciclo for.

# solicitud al usuario 
num = int(input("Ingrese un numero entero: "))

# ciclo for para generar los numeros pares
print("Los numeros pares desde 1 hasta", num, "son:")
for i in range(1, num + 1):
    if i % 2 == 0:
        print(i)
        