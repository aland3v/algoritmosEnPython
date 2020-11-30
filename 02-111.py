"""
Se necesita un programa que permita manejar transacciones de una cuenta.
El saldo inicial de la cuenta debe ser de Bs 0.00
El programa debe solicitar al usuario que indique si desea realizar un depósito o un retiro.
Si el usuario elige hacer un retiro, se solicita un valor y debe verificarse que haya saldo suficiente para retirar. De no ser
así se envía un mensaje al usuario notificando esa situación. Si hay saldo suficiente, se resta el valor ingresado al saldo.
Si el usuario elige hacer un depósito se solicita un valor y ese valor se suma al saldo.
Al final de cada transacción se pregunta al usuario si desea realizar otra transacción. Si contesta afirmativamente, se
repiten las acciones anteriores.
"""

print("Bienvenido a tu cuenta personal")
saldo = 0.00
respuesta = 'si'
while respuesta == 'si':    
    print("Que desea realizar?")
    print("1. Retirar dinero")
    print("2. Depositar dinero")

    opcion = int(input("opcion > "))
    if opcion == 1:
        if saldo == 0.0:
            print("Lo siento su saldo es insuficientes: %.2f"%saldo)
        else:
            sw = True
            while sw:
                monto = float(input("Monto a retirar? > "))
                if monto <= saldo:
                    print("Muy bien, ahora puede retirar su dinero")                    
                    saldo -= monto
                    print("Su saldo actual es: %.2f"%saldo)
                    sw = False
                else:
                    print("Lo siento pero su saldo es insuficiente: %.2f"%saldo)
                    print("Escoja otro monto")
    else:
        monto = float(input("Bien, monto a depositar > "))
        saldo += monto
        print("Ahora su saldo es: %.2f"%saldo)
    respuesta = input("Desea realizar otra transacción? si/no > ")

print("Muchas gracias vuelva pronto...")
