def comanda(comensal1 = 1,prime = "Consome",segundo = "Arroz rojo",tercero = "Enchilad"):
    print(f"El comensal {comensal} quiere:")
    print(f"Entrada:{primer}")
    print(f"Medio:{segundo}")
    print(f"Plato fuerte:{tercero}")

comanda()

comanda(3,"Ensalada","arroz blanco","Esparragos al horno")

comanda(segundo = "arroz blanco",tercero = "Esparragos al horno",primer = "Ensalada",)   

def comanda2(*opciones):
    #print(opciones)
    print(f"El comensal {opciones[0]} pidio:")
    print(f"Entrada:{opciones[1]")
    print(f"Medio:{opciones[2]}")
    print(f"Plato fuerte:{opciones[3]}")
    print("indicaciones extra:")
    for
     
comanda2(1, "sopa de fideo", "Pechuga asada","Arrachera")

def comanda3(**opciones):
    print(opciones)
    print(f"el comensal {opciones['comensal']} pidio:")
    

comanda3(segundo="arroz blanco",tercero="Esparragos al horno",primer="Ensalada",comensal=3)

def comanda3(**opciones):
    ops = opciones.keys()
    for key in ops:
        print(f"{key} = {opciones[key]}")
    
    

comanda3(segundo="arroz blanco",tercero="Esparragos al horno",primer="Ensalada",comensal=3)

from simple_chalk import chalk, yellow
print(chalk.yellow("Hola mundo"))

def sumar(a,b):
    return a + b
def mi_print(texto , final):
    print()

import mi_modulo

res = mi_modulo .sumar(7,5)
print(res)

mi_modulo.mi_print("Jesus", "\n")

from mi_modulo import sumar , mi_print
res = sumar(5,3)
print(res)
mi_print("Jesus", "'\n")

archivo = open("salida.txt","wt")
archivo.write("Hola mundo")
archivo.close

!cat salida.txt
