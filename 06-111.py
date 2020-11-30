"""
Problema ID: 1291 Problem  C	
Entrada
La entrada consiste de múltiples casos de prueba. La entrada termina cuando no hay más casos, es decir fin de archivo.
Cada caso de prueba consiste de una secuencia que viene en una línea con números separados por un espacio. Todas las secuencias terminan con un numero cero.
Salida
Por cada caso de prueba escrita en una linea la suma de los números.

Ejemplo Entrada
1 2 3 4 0
9 8 7 6 5 4 3 2 1 -5 0
-1 -3 5 3 1 0

Ejemplo Salida
10
40
5

"""
import sys

def main(elems):
    i = 0
    for x in elems:
        i += x
    print(i)

if __name__ == '__main__':
    for line in sys.stdin:
        elems = [int(x) for x in line.split()]
        main(elems)