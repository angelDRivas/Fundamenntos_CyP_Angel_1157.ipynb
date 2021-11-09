#Tuplas
info = ("angel","angel","123.232.1.12")
print(info)
print(info[1])
#info[1]= "patito23"

numeros = (0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)
print(numeros)
print(numeros[5:11])

cosas = (info, numeros)
print(cosas)
print(cosas[1][5:11])
print(cosas[0][2][4:7])
#DICCIONARIOS
alumno ={"nombre": "Jose "}
print(alumno)
print(alumno["nombre"])
alumno = {"nombre":"Jose","nc":"319172081","edad":18}
print("Edad del alumno =", alumno["edad"])
print("Nombre del alumno =", alumno["nombre"].upper())

alumno2 = dict() #{}
alumno2["nombre"]= "jose"
print(alumno2)
alumno2["nc"]= "319172081"
alumno2["edad"] = 18
print(alumno2)
alumno2["edad"]= alumno2["edad"]+1
print(alumno2)
#-------------------------------
cliente = {"id":"CT2121","nombre":"Angel de Jesus Rivas Rodriguez","telefono":"5527544171"}
print(cliente)
cliente ={"id":"CT2121",
"nombre" : {
"nombres":["Jose","Eduardo"],
"paterno": "Pedroza",
"materno":"Rosales"},
"telefonos":{
    "casa":"5522282154",
    "celular":"5527544171"
} ,
"productos":{
    "ahorro":{"numero_cuenta":"319172081", "ahorro":2500},
    "tarjetas":[ {"tipo":"debito","saldo":10000},
                 {"tipo":"credito","limite":250000}
                 ]
 }
}
print(cliente["telefonos"]["casa"])
print(cliente)

print(cliente["productos"]["ahorro"]["ahorro"])
