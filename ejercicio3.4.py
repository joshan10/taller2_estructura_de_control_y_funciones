# Ejercicio 3.4 – Generador de tablas de multiplicar interactivo:
# Desarrollar un programa que solicite al usuario un número y genere su tabla de multiplicar del 1 al 10. Luego, debe preguntar si desea generar otra tabla, continuando este proceso hasta que el usuario decida salir.


print("====== Generador de tablas de multiplicar interactivo ======")
print("====== Ingrese 0 para salir ======")

while True:
    number_user= int(input("Ingrese un numero para crear una tabla de multiplcar: "))
    print(f"Tabla del {number_user}\n")
    for i in range(1, 11):
        print(f"{number_user} x {i} = {i * number_user}\n")
    
    if number_user == 0:
        print("Saliendo...")
        break