"""
Entrada
La entrada consiste de varios casos de prueba.
Cada caso contiene dos numero enteros n y k  1 <= k <= n <= 10^12. n La cantidad
de numeros que tiene matilde, k que numero se encuentra en la k esima 
poscion. 

Salida
Imprima el numero que queda en la K esima posicion.

Ejemplo Entrada
10 3
Ejemplo Salida
5

Ayuda
En el ejemplo tenemos 10 numero ordenados de la forma
1 3 5 7 9 2 4 6 8 10
k = 3
en la posicion 3 esta 5
"""
while True:
    try:
        n,k = input().split()
    except EOFError:
        break
    except ValueError:
        break
    n = int(n)
    k = int(k)
    if n%2==1:
        n+=1
    div = n//2
    if k <= div:
        i = 2*k-1
    else:
        k = k-div
        i = 2*k
    print(i)