"""
e necesita un programa que permita la captura de cinco valores correspondientes a radios de círculos.
Para cada uno de esos cinco valores se requiere que se calcule y muestre en pantalla los siguientes datos del círculo:
1. Diámetro. Se calcula multiplicando el radio por 2
2. Circunferencia. Se calcula multiplicando el diámetro por pi (3.1416).
"""

PI = 3.1416

print("Bienvenido introduzca los radios de los circulos:")

resultados = []

for i in range(1,6):
    r = float(input("Radio %d: "%i))
    resultados.append((r,r*2,r*PI))

for par in resultados:
    print("Radio: %.2f\t Diametro: %.2f\t Circunferencia: %.2f"%(par[0],par[1],par[2]))

