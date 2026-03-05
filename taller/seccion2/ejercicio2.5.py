# Ejercicio 2.5 – Simulador de descuentos por categoría:
# Crear un simulador de descuentos que solicite al usuario su categoría (A, B, C) y el monto de compra. Aplicar los siguientes descuentos según categoría: A=20%, B=15%, C=10%. Para cualquier otra categoría no aplicar descuento. Mostrar el monto final a pagar y la cantidad ahorrada.

print("================================")
print("Bienvenido al simulador de descuentos.")
print("creado por joshan pereira")
print("================================")
categoria = input("Ingrese su categoría (A, B, C): ").upper()
monto_compra = float(input("Ingrese el monto de compra: "))
if categoria == "A":
    descuento = monto_compra * 0.20
elif categoria == "B":
    descuento = monto_compra * 0.15
elif categoria == "C":
    descuento = monto_compra * 0.10
else:
    descuento = 0