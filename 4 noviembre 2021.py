
#Para solicitar los datos del usuario se emplea la funcion input La cual regresa siempre,un tipo de dato stirng
nombre = input("Ingresa tu nombre")
print("Tecleaste:", nombre)
entrada = input("Dame tu edad")
edad = int(entrada)
edad += 1
print("Tu edad es:", edad)

# Lo mismo pero con menos codigo

edad = int(input("Dame tu edad:"))
print("Tu edad es:",edad)

estatura = float(input("Dame tu estatura:"))
print("Tu estatura es:",estatura)


#Tipos de datos estructurados de python
numeros = [10,5,2,3,1]
print(numeros)

numeros2 = list()
numeros2.append(10)
numeros2.append(5)
numeros2.append(2)
numeros2.append(3)
numeros2.append(1)

print(numeros2)

# tipos diversos

cosas = [12,2,True,"Jose",1.57,["pera","Kiwi","Uva"]]
print(cosas)
print(cosas[1])
print(cosas[4])
print(cosas[5])
print( cosas[5][1])

numeros= [4,1,15,8,22,34,50]
print(numeros)
numeros.append(99)
print(numeros)
numeros = []

frutas = ["uvas","kiwi","manzana"]
copia = frutas
print(frutas)
print(copia)
frutas.append("Naranja")
copia2 = frutas.copy()
print(frutas)
print(copia2)

nombre = ["jose","pedro","Karina"]
otrosnombres = ["josue","diana","dalia"]
print(nombre)
print(otrosnombres)
nombre = nombre + otrosnombres
print(nombre)
print(otrosnombres)
otrosnombres.extend(["jesus","maria","Jose"])
print(otrosnombres)
otrosnombres.insert(4,"Espiritu santo")
print(otrosnombres)
