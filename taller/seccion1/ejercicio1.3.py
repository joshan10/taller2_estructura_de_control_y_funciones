#Ejercicio 1.3 – Validación de correo electrónico: Crear un programa que pida al usuario ingresar un correo electrónico y verifique que contenga los caracteres "@" y "." en posiciones válidas. Mostrar mensajes apropiados indicando si el correo tiene un formato básico correcto o si presenta errores.


print("================================")
print("Bienvenido a la validacion de correo.")
print("creado por joshan pereira")
print("================================")

#solicitud de correo electronico

email = input("Ingrese un email: ")

#validacion de correo electronico
if "@" in email and "." in email:
    print("\nEl correo tiene un formato básico correcto.")
else:
    print("\nEl correo presenta errores en su formato.")

