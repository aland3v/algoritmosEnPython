"""
Dados tres números calcule:
    - La suma de los tres
    - El promedio de los tres
    - El producto de los tres
    - El menor de los tres
"""

def main():
    num1 = int(input("Número 1: "))
    num2 = int(input("Número 2: "))
    num3 = int(input("Número 3: "))

    suma = num1 + num2 + num3

    promedio = (num1 + num2 + num3)/3
    producto = num1*num2*num3

    if num1 <= num2:
        if num1 <= num3:
            menor = num1
        else: 
            menor = num3
    else:
        if num2 <= num3:
            menor = num2
        else:
            menor = num3

    print("La suma es: %s"%(str(suma)))
    print("El producto es: %s"%(str(producto)))
    print("El promedio es: %s"%(str(promedio)))
    print("El número menor es: %s"%(str(menor)))

main()