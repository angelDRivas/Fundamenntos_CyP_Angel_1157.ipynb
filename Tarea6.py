#Problema 2.1

N = int(input("Sonidos emitidos por minuto:"))
T = N/4 + 40
if N>0 :
    print(f"La temperatura es de {T} grados fahrenheit")
else:
    print("Error el numero es igual menor a cero ")
print("FIN DEL PROGRAMA")
#Problema 2.2

P = int(input("Ingresa un valor entero (P) :"))
Q = int(input("Ingresa otro valor entero (Q) :"))
EXP = P**3 + Q**4 - 2*P**2
if EXP  < 680:
    print(f"P es igual a: {P} y Q es igual a: {Q}")
else:
    print("Rango superado")
    print("FIN DEL PROGRAMA")
#Problema 2.3

A = float(input("Ingresa el valor de A:"))
B = float(input("Ingresa el valor de B:"))
C = float(input("Ingresa el valor de C:"))
DIS = B**2 - 4*A*C
if DIS >= 0:
    X1= ((-B)+DIS**0.5)/2*A
    X2= ((-B)-DIS**0.5)/2*A
    print("Raices reales")
    print(f"X1= {X1}, X2 = {X2}")
else:
    print("FIN DEL PROGRAMA")
#Problema 2.4

MAT = int(input("Matricula del alumno :"))
CAL1 = float(input("Calificación 1 :"))
CAL2 = float(input("Calificación 2 :"))
CAL3 = float(input("Calificación 3 :"))
CAL4 = float(input("Calificación 4 :"))
CAL5 = float(input("Calificación 5 :"))
PRO = (CAL1 + CAL2 + CAL3 + CAL4 + CAL5)/5
if PRO >= 6 :
    print(f"{MAT},{PRO} aprobado")
else:
     print(f"{MAT},{PRO} reprobado")
#Problema 2.5

NUM = int(input("Dame un valor entero"))
if NUM>0:
    print("Valor positivo")
    if NUM==0:
        print("Valor nulo")
else:
        NUM<0
        print("Valor negativo")
#Problema 2.6

A = int(input("Ingresa valor entero"))
if A==0:
    print("NULO")
    if -1**A>0:
        print("PAR")
else:
    print("IMPAR")
print("FIN")
#Problema 2.7

A = int(input("Ingrese un valor"))
B = int(input("Ingrese un valor distinto"))
C = int(input("Ingrese otro valor distinto"))
if A<B :
    if B<C:
        print("Los numeros  estan en orden creciente")
    else:
        print("Los numeros no estan en orden creciente")       
else:
    print("Los numeros no estan en orden creciente")
#Problema 2.8

NUM = float(input("Ingrese la cantidad de compra:"))
COMPRA = NUM
PAGAR = COMPRA

if COMPRA < 500:
    print(f"Total a pagar:{PAGAR}")
elif COMPRA<= 1000:
    PAGAR = COMPRA-(COMPRA*0.05)
    print(f"Total a pagar:{PAGAR}")
elif COMPRA<= 7000:
    PAGAR = COMPRA-(COMPRA*0.11)
    print(f"Total a pagar:{PAGAR}")
elif COMPRA<= 15000:
    PAGAR = COMPRA-(COMPRA*0.18)
    print(f"Total a pagar:{PAGAR}")
else:
    PAGAR = COMPRA-(COMPRA*0.25)
    print(f"Total a pagar:{PAGAR}")
#Problema 2.9

PREBAS =float(input("Ingresa precio"))
if PREBAS>500:
    IMP = 20*0.3+(PREBAS-40)*0.5
    PRETOT= PREBAS + IMP
    print((PREBAS,PRETOT))
elif PREBAS>40:
    IMP = 20*0.3+(PREBAS-40)*0.4
    PRETOT= PREBAS + IMP
    print((PREBAS,PRETOT))
elif PREBAS>20:
    IMP = 20*0.3+(PREBAS-40)*0.3
    PRETOT= PREBAS + IMP
    print((PREBAS,PRETOT))
else:
    IMP = 0
    PRETOT= PREBAS + IMP
    print((PREBAS,PRETOT))
#Problema 2.10

A = int(input("ingresa un valor A"))
B = int(input("ingresa otro valor B"))
C = int(input("ingresa otro valor C"))

if A>B:
    if A>C:
        print("A es el mayor")
    else:
        if A==C:
            print("A y C son los mayores")
        else:
            print("C es el mayor")
else:
    if A==B:
        if A>C:
            print("A y B son los mayores")
        else:
            if A==C:
                print("A,B y C son iguales")
            else:
                print("C es el mayor")
    else:
        if B>C:
            print("B es el mayor")
        else:
            if B==C:
                print("B y C son los mayores")
            else:
                print("C es el mayor")
