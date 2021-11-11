edad = int(input("Dame tu edad"))
print(f"Tecleaste {edad} años")
if edad >= 18:
   print("Eres mayor de edad")
   print("Algo")
   print("Otra cosa")
print("Fin de programa")

CAL = int(input("Dame tu calificacion"))
print(f"Tecleaste {CAL} ")
if CAL > 8:
  print("aprobado")
  
  SUE = float(input("Dame el valor de tu sueldo"))
AUM = 0
MSUE = 0
if SUE < 1000:
 AUM = SUE*0.15
 MSUE= SUE +AUM
 print(MSUE)
