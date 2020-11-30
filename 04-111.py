"""
PROBLEMA_ID = 1527
Entrada
Consistirá en un número n que indica el número de alumnos que 
entregaron la práctica. Por cada alumno, habrá un número x que 
indica el número que el alumno escribió para responder la última 
pregunta de la práctica.  (10^2≤x≤10^18)
Salida
Por cada alumno que entregó la práctica, escribe "APLAZADO!" si 
el número que el alumno escribió, contenía algún 96. De lo contrario, 
escribe "TE SALVAS :D"
"""
n = int(input())
for i in range(1,n+1):
    cad = input()
    if '96' in cad:
        print("APLAZADO!")
    else:
        print("TE SALVAS :D")
