carrera ="ingenieria en computación"
print(carrera)
print(carrera[2])
--------------------------
carrera = "ingeniería en computación"
print(carrera [8])
print(carrera[24])
print(carrera [-1])
print(carrera[-25])


# Adelantando el tema ciclo FOR
for letra in carrera:
  print("-->",letra,"<--")
-----------------------------
carrera = "ingeniería en computación"
print(carrera[0:10:1])
print(carrera[14:25:1])
print(carrera[-11: :1 ])
#solucion previa
print("-------------")
print(carrera[-11:-1:1])
#Ejercicio de incremento
print(carrera[-1:-12:-1])
-----------------------------
frutas =" limon , fresa , manzana , aguacate"
nombre = "Angel"
print(frutas)

print(nombre.capitalize() )
print( nombre.upper())
print(frutas.replace('a','4').replace('e','3').upper())
print(frutas)
print("---------")
frutas = "limon , fresa , manzana , aguacate"
print(frutas.strip())
print(frutas.split(','))

