"""
Descripción
Se tiene una lista de números y te piden hallar la suma de todos los numeros que estan entre las posiciones a y b (incluidos a y b). Se sabe que la suma no excede un numero entero.

Entrada
La entrada consiste de múltiples casos de prueba. La primera línea contiene un numero N que indica el numero de casos de prueba.
Cada caso de prueba consiste de dos líneas, la primera linea tiene un numero M que representa la cantidad de números que hay que leer y los números a,b que son menores a M.
La segunda línea contiene los M números separados por un espacio.
Salida
Por cada caso de prueba escrita en una linea la suma de los números que están entre a y b inclusive.

Ejemplo Entrada
3
7 1 3
1 2 3 4 5 6 7 
10 8 9
9 8 7 6 5 4 3 2 1 -5
5 0 0
-1 -3 5 3 1
Ejemplo Salida
9
-4
-1
"""
def main():
    n = int(input())
    j = 1
    while j <= n:    
        m,a,b = input().split()
        m,a,b = int(m),int(a),int(b)
        v = [int(x) for x in input().split()]
        sum = 0
        for i in v[a:b+1]:
            sum += i
        print(sum)
        j += 1

if __name__ == '__main__':
    main()