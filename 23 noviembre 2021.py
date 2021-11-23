A=int(input("Dame un primer numero entero: "))
B=int(input("Dame un segundo numero entero diferente: "))
C=int(input("Dame un tercer numero entero diferente: "))

if A==B==C or A==B or A==C or B==C:
    print("algunos numeros se repiten")
if A>B:
    if A>C: 
        if B>C:
            print("orden mayor a menor : ",A, B, C)
        else:
            print("orden mayor a menor : ",A, C, B)
    else: print("orden mayor a menor : ",C, A, B)
else:
    if B>C: 
    
        if A>C:
            print("orden mayor a menor : ",B, A, C)
        else:
            print("orden mayor a menor : ",B, C, A)
    else: print("orden mayor a menor : ",C, B, A)

print("-- fin --")
#_____________________________________________
TIPOENF = int(input("Introduce el tipo de enfermedad"))
EDAD = int(input("Introduce la edad"))
DIAS = int(input("Introduce el número de dias"))
COSTO = 0.0

if TIPOENF ==1 :
    COSTO = DIAS  * 25.0
elif TIPOENF==2:
    COSTO = DIAS * 16.0
elif TIPOENF ==3:
    COSTO = DIAS * 20.0
elif TIPOENF ==4:
    COSTO = DIAS * 32.00
if EDAD >= 14 and EDAD <= 22:
    COSTO = DIAS * 1.10 
print(f"Costo total = {COSTO}$") 
#______________________________
frutas = ["uva","manzana","pera","aguacate","sandia"]

for  in  range(5):
    print(frutas[index])
