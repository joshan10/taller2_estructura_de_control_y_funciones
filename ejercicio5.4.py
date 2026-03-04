# Ejercicio 5.4 – Detector de palíndromos:
# Crear una función llamada es_palindromo que reciba un texto como parámetro y retorne True si es un palíndromo (se lee igual al derecho y al revés) o False en caso contrario. La función debe ignorar espacios, mayúsculas/minúsculas y signos de puntuación.

print("--- Detector de palíndromos ---\n")
#pedir al usuario la palabra
palabra = input("Ingrese una palabra: ")

def es_palindromo(palabra):
    # Convertir a minúsculas y quitar espacios
    p = palabra.lower().replace(" ", "")
    # Comparar con su inversa
    return p == p[::-1]

print(es_palindromo(palabra))