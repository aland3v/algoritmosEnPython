"""
Introducir dos números enteros positivos en las variables a y b 
respectivamente. Calcular y
desplegar la cantidad de números pares que existen en el intervalo 
cerrado entre a y b.
"""
def pares_rango(a, b):
    #a, b = [int(x) for x in input().split()]
    pares = (b - (a - 1))//2
    if a%2==0 and b%2==0:
        pares += 1
    elif a%2==1 and b%2==1:
        pares -= 1
    #print("Numero de pares: %d"%pares)
    return pares
