#Ejercicio 1.4 – Validador de contraseña segura: Implementar un sistema que valide la fortaleza de una contraseña. El usuario debe ingresar una contraseña y el algoritmo debe verificar que cumpla con los siguientes criterios: tener al menos 8 caracteres, contener al menos una letra mayúscula, un número y un carácter especial (!@#$%^&*). Informar específicamente qué criterios no se cumplen.

pasword = input("Ingrese una contraseña: ")
character = ["!", "@", "#", "$", "%", "^", "&", "*"]

if len(pasword) < 8:
    print("La contraseña debe tener al menos 8 caracteres.")
elif not any(char.isupper() for char in pasword):
    print("La contraseña debe contener al menos una letra mayúscula.")
elif not any(char.isdigit() for char in pasword):
    print("La contraseña debe contener al menos un número.")
elif not any(char in character for char in pasword):
    print("La contraseña debe contener al menos un carácter especial (!@#$%^&*).")
else:
    print("La contraseña es segura.")

