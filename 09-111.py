'''
Generar la serie compuesta formada por los números fibonacci, 
números primos y números impares, en ese orden: 
1, 2, 1, 1, 3, 3, 2, 5, 5, 3, 7, 7, 5, 11, 9, 8, 13, 11....
'''
def main():
    n = int(input('Ingrese n: '))

    # contador de serie: 1->n
    c = 1

    # variables fibo
    a = 1
    b = 1
    aux = 0

    # variables de primos
    div = 1
    primo = 1    
    c_div = 0
    sw_p = 1
    # variable de control sw = 1,2,3
    sw = 1

    # variable de inpares
    inpar = 1

    while c <= n:
        if sw == 1:
            # fibos
            print(a,end=',')
            c += 1
            aux = b
            b = a + b
            a = aux
            sw = 2
        elif sw == 2:
            # primos
            while sw_p:
                for div in range(1,primo+1):
                    if primo % div == 0:
                        c_div += 1
                if c_div == 2:
                    print(primo,end=',')                    
                    c += 1                    
                    sw_p = 0
                c_div = 0
                primo += 1      
            sw_p = 1
            sw = 3
        else:
            print(inpar,end=',')
            c += 1
            inpar += 2
            sw = 1
    print()

if __name__ == '__main__':
    main()