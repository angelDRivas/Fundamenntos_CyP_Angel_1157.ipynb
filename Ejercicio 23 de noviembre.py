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
