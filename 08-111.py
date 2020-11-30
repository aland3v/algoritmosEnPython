'''
                    SE USA METODO QUICKSORT
Descripción
Dado un vector A de enteros se le pide ordenar todos los elementos del vector 
que se encuentran entre los indices I y J (incluidos los que se encuentran en I y J). 
Los indices del vector se manejan desde 0.

Entrada
En la primera linea de la entrada se encuentran 3 enteros N, I, J (1<=N<=100, 0<=I<=J<=N−1)
separados por un espacio.
En la segunda linea de la entrada N numeros enteros Ai separados por un espacio 
que son los elementos del vector A. (0 <= Ai <= 1000000)

Salida
Los N elementos del vector A separados por un espacio despues de ordenar los elementos 
que se encuentran entre los indices I y J. Y un salto de linea al final de todos los numeros.

Ejemplo Entrada
10 4 8
3 1 2 4 5 6 2 7 1 0
Ejemplo Salida
3 1 2 4 1 2 5 6 7 0

'''

def main():
    n, a, b = input().split()# 
    n, a, b = int(n),int(a),int(b)
    
    v = [int(x) for x in input().split()]
    
    Quicksort(v, a, b)

    salida = ""
    for i in v:
        salida += str(i) + " "
    print(salida.rstrip())

def Quicksort(v, a, b):
    matris = [0]*len(v)    
    buf = 0
    frm = a
    to = b
    pivote = v[(frm+to)//2]
    while True:
        while v[frm] < pivote:
            frm += 1
        while v[to] > pivote:
            to -= 1
        if frm <= to:
            buf = v[frm]
            v[frm] = v[to]
            v[to] = buf
            frm += 1
            to -= 1
        if frm > to:
            break
    if a < to:
        Quicksort(v, a, to)
    if frm < b:
        Quicksort(v, frm, b)
    matris = v

if __name__ == '__main__':
    main()