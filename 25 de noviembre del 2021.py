for x in range(1,20,1):
    print(x)
print("fin del programa")

for x in range(19,0,-1):
    print(x)
print("fin del programa")


CUECER = 0
NUM =0 
N = int(input("un valor numerico mayor que 1:"))
for I in range (1, N+1 ,1):
    N = int(input("un valor numerico :"))
    if N == 0:
        CUECER +=1
print("CUECER=",CUECER)


for f in range(1,11): print(f'7 x {f} = {7 * f}')
print(f) 

N1=int(input('ingresa un valor entre 1 y 5: '))

if N1>0 and N1<6:
    N2=int(input(f'ingresa un valor entre el {N1} y 10: '))
    if N2>= N1 and N2<11:

        for i in range( N1, N2+1):
            for j in range(0,11):
                print(f"{i} x {j} = ", i*j)
    
    else:
        print('El valor ingresado no esta dentro del rango')
else:
    print('El valor ingresado no esta dentro del rango')
    
    numeros = [0,0,0,0]
print(numeros)
numeros = [0 for x in range(5)]
print(numeros)

numeros = [x for x in range (5)]
print(numeros)
numeros=[(x+1)*10 for x in range(10)]
print(numeros)

SUM = 0
edades = [0 for x in range(5)]
for x in range(5):
    edades[x]= int(input("Introduce una edad: "))
    SUM = SUM + edades[x]
    PROM = SUM/5
pri1nt(edades)
print("El promedio de edades es: ", PROM)
