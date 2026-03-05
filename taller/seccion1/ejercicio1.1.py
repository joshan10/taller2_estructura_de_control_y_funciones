print("================================")
print("Bienvenido al programa de registro de usuarios.")
print("creado por joshan pereira")
print("================================")


#solictud de datos de usuario
nombre = input("Ingrese su nombre: ")
ciudad_residencia = input("Ingrese su ciudad de residencia: ")

#validacion de edad
while True:
    try:
        edad = int(input("Ingrese su edad: "))
        if edad <= 0:
           
            print("La edad no puede ser negativa.")
        else:
            break
    except ValueError:
        print("Por favor, ingrese un número válido.")

print(f"Hola {nombre}, tienes {edad} años y vives en {ciudad_residencia}.")

