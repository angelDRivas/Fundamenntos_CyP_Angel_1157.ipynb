#Problema 3.1

SUMPAR = 0
SUMIMP = 0
CUEPAR = 0
NUM = 0
I = 1
while I<=270:
    NUM = I  
    if NUM>0:
        if  NUM%2!=0:
            SUMPAR = SUMPAR + CUEPAR 
            CUEPAR = CUEPAR + 1
        else: SUMIMP = SUMIMP + NUM
    I = I + 1
PROPAR = SUMPAR / CUEPAR
print(f"Este es el promedio de los numeros pares {PROPAR} y esta es la suma de los numeros  impares {SUMIMP}")

#Problema 3.2

BAND = 'T'
SUMSER = 0
I = 2
while I <= 1800:
    SUMSER = SUMSER + I
    print(I)
    if BAND == 'T':
        BAND = 'F'
        I = I + 3
    else:
        BAND = 'T'
        I = I + 2
print(f"La suma es {SUMSER}")

#Problema 3.3

SERIE = 0
N = int(input("Ingresa un numero entero: "))
BAND = 'T'
I = 1
while I <= N:
    if BAND == 'T':
        SERIE = SERIE + (1/I) 
        BAND = 'F'
    else: 
        SERIE = SERIE - (1/I)
        BAND = 'T'
    I = I + 1
print(SERIE)

#Problema 3.4

NOM = 0
SUE = [855,760.32,1100.2,614,2600,817.5,1280.3,687,-1]
I = 0
while SUE[I] > -1:
    if SUE[I] < 1000:
        NSUE = round(SUE[I]*1.15,2)
    else:
        NSUE = round(SUE[I]*1.12,2)
    NOM = round(NOM + NSUE,2)
    I = I + 1
    print(f"El nuevo sueldo  es de ${NSUE}")
print(f"La nomina total es de  ${NOM}")
