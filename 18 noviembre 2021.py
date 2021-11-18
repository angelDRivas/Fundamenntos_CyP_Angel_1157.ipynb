edad = int(input("Dame tu edad:"))
print(f"Tecleaste{edad} años")
if edad >= 18: 
    print("eres mayor de edad, ten tu cheve")
else:
    print("Eres menor de edad, ten tu boing")
print("fin del programa")
#---------------------------------------
edad = int (input("Dame tu edad:"))
dinero = int (input("¿Cuánto dinero tienes?"))
print(f"Tecleaste {edad} años")
print(f"Tecleaste {dinero} pesos")
if edad >= 18:
    if dinero >=35:
        print("Eres mayor de edad y tienes dinero, ten tu cheve")
    else:
        print("No tienes suficiente dinero")
else:
    print("Eres menor de edad, ten tu Boing")
print("Fin del programa")
#-------------------------------------------
CAL= float(input("Escribe tu calificiación: "))
if CAL >= 8 :
    print("Aprobado")
else: 
    print("Reprobado")
    #-------------------------------------
    SUE = float(input("Escribe el sueldo: "))
AUM = 0 
NSUE = 0

if SUE < 1000 :
    AUM = SUE* 0.15
    NSUE = SUE + AUM
    print(NSUE)
else:
    AUM= SUE*0.12
    NSUE = SUE + AUM
    print(MSUE)
    #------------------------------------
    dia = int(input("dame un valor numerico correspondiente a un dia de la semana 1-7:"))
if dia > 7 or dia < 1:
 print("El numero ha salido del rango")
else:
    if dia == 1:
        print("Lunes")
    elif dia == 2:
        print("Martes")
    elif dia == 3:
        print("Miércoles")
    elif dia == 4:
        print("Jueves")
    elif dia == 5:
        print("Viernes")
    elif dia == 6:       
        print("Sábado")
    elif dia == 7:
        print("Domingo")
