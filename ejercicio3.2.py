#  Ejercicio 3.2 – Acumulador numérico:
# Implementar un algoritmo que permita al usuario ingresar números de manera continua. El programa debe sumar todos los números ingresados hasta que el usuario ingrese el valor 0, momento en el cual mostrará la suma total acumulada.

# solicitud al usuario
suma = 0
while True:
    num = int(input("Ingrese un numero (0 para finalizar): "))
    if num == 0:
        break
    suma += num
print("La suma total acumulada es:", suma)